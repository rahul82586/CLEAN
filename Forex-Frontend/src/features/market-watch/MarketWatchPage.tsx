import * as React from 'react';
import { API } from '../../services/api';
import { wsStreamService } from '../../services/api/ticksStream';

interface QuoteRow {
    symbol: string;
    // null means the server has NO price for this symbol. It must never be
    // rendered as 0, which is what previously turned an absent quote into a 0.00
    // price - a fabricated value on the one screen whose job is prices.
    bid: number | null;
    ask: number | null;
    /** Seconds since the tick, or Infinity when there has never been one. */
    age: number;
    spread: number | null;
    /** 'open' | 'closed' | 'no_data' - from the server, not inferred here. */
    marketState?: 'open' | 'closed' | 'no_data';
    isMarketOpen?: boolean;
    /** The quote is older than this symbol's own Max quote delay. */
    isTickStale?: boolean;
    maxQuoteDelay?: number;
    prevBid?: number;
    prevAsk?: number;
    flashBid?: 'up' | 'down';
    flashAsk?: 'up' | 'down';
}

/**
 * A price, or an em dash when there is none.
 *
 * null/undefined means the server has no quote for this symbol. It must NOT render as
 * 0.00 - that is a fabricated price - and it must not crash. An em dash says "no value".
 */
function formatPrice(v: number | null | undefined): string {
    if (v == null || !Number.isFinite(v)) return '\u2014';
    if (v >= 10000) return v.toFixed(2);
    if (v >= 100)   return v.toFixed(3);
    return v.toFixed(5);
}

function formatAge(s: number): string {
    if (s < 1) return '<1s';
    if (s < 60) return `${Math.round(s)}s`;
    if (s < 3600) return `${Math.floor(s / 60)}m ${Math.round(s % 60)}s`;
    return `${Math.floor(s / 3600)}h`;
}

/**
 * Age colour for a quote.
 *
 * A CLOSED market is not a fault: the last price is the last real price and is expected
 * to be hours old. Colouring that red is exactly what made a shut weekend look like a
 * dead feed, so closed symbols get a neutral colour and only an OPEN symbol can be
 * alarming.
 *
 * While open, the symbol's own Max quote delay decides "stale" - the same value the
 * order path enforces - falling back to a plain age threshold when it is not configured.
 */
function ageColor(age: number, row?: QuoteRow): string {
    const neutral = 'var(--theia-descriptionForeground, #8b8b8b)';

    if (row && row.marketState === 'closed') return neutral;

    if (row?.isTickStale) return 'var(--theia-errorForeground, #e74c3c)';

    const limit = row?.maxQuoteDelay && row.maxQuoteDelay > 0 ? row.maxQuoteDelay : 30;
    if (age < 5) return 'var(--theia-successForeground, #2ecc71)';
    if (age < limit) return 'var(--theia-warningForeground, #f1c40f)';
    return 'var(--theia-errorForeground, #e74c3c)';
}

/** The label and colour for a row's market state. */
function marketStateBadge(state?: string): { label: string; color: string } {
    switch (state) {
        case 'open':
            return { label: 'Open', color: 'var(--theia-successForeground, #2ecc71)' };
        case 'no_data':
            return { label: 'No data', color: 'var(--theia-errorForeground, #e74c3c)' };
        case 'closed':
        default:
            return { label: 'Closed', color: 'var(--theia-descriptionForeground, #8b8b8b)' };
    }
}

export function MarketWatchPage(): React.ReactElement {
    const [quotes, setQuotes] = React.useState<QuoteRow[]>([]);
    const [error, setError] = React.useState<string | null>(null);
    const [lastUpdate, setLastUpdate] = React.useState<Date | null>(null);
    const [filter, setFilter] = React.useState('');
    const prevRef = React.useRef<Record<string, { bid: number; ask: number }>>({});
    const flashTimers = React.useRef<Record<string, ReturnType<typeof setTimeout>>>({});


    // One line summarising the market, derived from the SAME rows the table shows.
    //
    // Counted from market_state, which the server derives from each symbol's real trading
    // sessions - so this cannot disagree with the per-row badge or with the order gate.
    const marketSummary = React.useMemo(() => {
        const total = quotes.length;
        const open = quotes.filter(q => q.marketState === 'open').length;
        const noData = quotes.filter(q => q.marketState === 'no_data').length;
        const closed = total - open - noData;
        let text: string;
        let color: string;
        if (total === 0) {
            text = 'Waiting for market data...';
            color = 'var(--theia-descriptionForeground, #8b8b8b)';
        } else if (open === 0) {
            // Every symbol shut is NORMAL at the weekend. Saying so plainly is the point:
            // the earlier screen made this look like a failure.
            text = `Market closed - 0 of ${total} symbols tradeable`
                + (noData > 0 ? `, ${noData} with no price` : '')
                + '. FX reopens around 21:00-22:00 UTC on Sunday.';
            color = 'var(--theia-descriptionForeground, #8b8b8b)';
        } else {
            text = `Market open - ${open} of ${total} symbols tradeable`
                + (closed > 0 ? `, ${closed} closed` : '')
                + (noData > 0 ? `, ${noData} with no price` : '') + '.';
            color = 'var(--theia-successForeground, #2ecc71)';
        }
        return { text, color, total, open, closed, noData };
    }, [quotes]);
    const fetchQuotes = React.useCallback(async () => {
        try {
            const data = await API.getTicks();
            setError(null);
            setLastUpdate(new Date());

            setQuotes(prev => {
                const prevMap: Record<string, QuoteRow> = {};
                prev.forEach(r => { prevMap[r.symbol] = r; });

                const rows: QuoteRow[] = Object.entries(data)
                    .map(([symbol, q]) => {
                        const old = prevRef.current[symbol];
                        let flashBid: 'up' | 'down' | undefined;
                        let flashAsk: 'up' | 'down' | undefined;

                        const haveOld = !!old && old.bid != null && old.ask != null;
                        const haveNew = q.bid != null && q.ask != null;
                        if (haveOld && haveNew) {
                            const prev = old as { bid: number; ask: number };
                            if (q.bid > prev.bid) flashBid = 'up';
                            else if (q.bid < prev.bid) flashBid = 'down';
                            if (q.ask > prev.ask) flashAsk = 'up';
                            else if (q.ask < prev.ask) flashAsk = 'down';
                        }

                        prevRef.current[symbol] = { bid: q.bid, ask: q.ask };

                        const rawSpread = q.spread != null
                            ? q.spread
                            : (q.ask != null && q.bid != null ? q.ask - q.bid : null);
                          const spreadVal = rawSpread == null
                              ? null
                              : (q.ask < 10
                                  ? Math.round(rawSpread * 100000) / 10
                                  : Math.round(rawSpread * 100) / 100);

                        return {
                            symbol,
                            bid: q.bid,
                            ask: q.ask,
                              age: q.age != null ? q.age : Number.POSITIVE_INFINITY,
                              marketState: q.marketState ?? 'no_data',
                              isMarketOpen: q.isMarketOpen,
                              isTickStale: q.isTickStale,
                              maxQuoteDelay: q.maxQuoteDelay,
                            spread: spreadVal,
                            prevBid: old?.bid,
                            prevAsk: old?.ask,
                            flashBid,
                            flashAsk,
                        };
                    })
                    .sort((a, b) => a.symbol.localeCompare(b.symbol));

                return rows;
            });
        } catch (e: any) {
            setError(e?.message || 'Failed to fetch quotes');
        }
    }, []);

    React.useEffect(() => {
        // Initial fetch
        fetchQuotes();

        // Realtime low-latency WebSocket stream subscription (/ws/stream)
        const unsubscribe = wsStreamService.subscribeTicks((incomingTicks) => {
            setError(null);
            setLastUpdate(new Date());

            setQuotes(prev => {
                const map: Record<string, QuoteRow> = {};
                prev.forEach(r => { map[r.symbol] = { ...r }; });

                for (const [symbol, q] of Object.entries(incomingTicks)) {
                    const old = prevRef.current[symbol];
                    let flashBid: 'up' | 'down' | undefined;
                    let flashAsk: 'up' | 'down' | undefined;

                    const haveOld = !!old && old.bid != null && old.ask != null;
                    const haveNew = q.bid != null && q.ask != null;
                    if (haveOld && haveNew) {
                        const p = old as { bid: number; ask: number };
                        if (q.bid! > p.bid) flashBid = 'up';
                        else if (q.bid! < p.bid) flashBid = 'down';
                        if (q.ask! > p.ask) flashAsk = 'up';
                        else if (q.ask! < p.ask) flashAsk = 'down';
                    }

                    prevRef.current[symbol] = { bid: q.bid, ask: q.ask };

                    const rawSpread = q.spread != null
                        ? q.spread
                        : (q.ask != null && q.bid != null ? q.ask - q.bid : null);
                    const spreadVal = rawSpread == null
                        ? null
                        : (q.ask < 10
                            ? Math.round(rawSpread * 100000) / 10
                            : Math.round(rawSpread * 100) / 100);

                    const existing = map[symbol];
                    map[symbol] = {
                        symbol,
                        bid: q.bid,
                        ask: q.ask,
                        age: q.age != null ? q.age : 0,
                        marketState: q.marketState ?? existing?.marketState ?? 'open',
                        isMarketOpen: q.isMarketOpen ?? true,
                        isTickStale: q.isTickStale ?? false,
                        maxQuoteDelay: q.maxQuoteDelay ?? existing?.maxQuoteDelay,
                        spread: spreadVal,
                        prevBid: old?.bid,
                        prevAsk: old?.ask,
                        flashBid,
                        flashAsk,
                    };
                }

                return Object.values(map).sort((a, b) => a.symbol.localeCompare(b.symbol));
            });
        });

        // Secondary fallback sync (5s) for full list reconciliation
        const fallbackIv = setInterval(fetchQuotes, 5000);

        return () => {
            unsubscribe();
            clearInterval(fallbackIv);
        };
    }, [fetchQuotes]);

    // Clean flash states in single batched 400ms interval without setting cascading timers
    React.useEffect(() => {
        const iv = setInterval(() => {
            setQuotes(prev => {
                if (!prev || prev.length === 0) return prev;
                let hasFlash = false;
                for (const r of prev) {
                    if (r.flashBid || r.flashAsk) {
                        hasFlash = true;
                        break;
                    }
                }
                if (!hasFlash) return prev;
                return prev.map(r => (r.flashBid || r.flashAsk ? { ...r, flashBid: undefined, flashAsk: undefined } : r));
            });
        }, 400);
        return () => clearInterval(iv);
    }, []);

    const filtered = filter.trim()
        ? quotes.filter(r => r.symbol.toLowerCase().includes(filter.toLowerCase()))
        : quotes;

    const connected = quotes.length > 0 && quotes.some(r => r.age < 30);

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
            {/* Header bar */}
            <div style={{
                display: 'flex', alignItems: 'center', gap: 12, padding: '8px 12px',
                borderBottom: '1px solid var(--theia-panel-border)',
                background: 'var(--theia-editor-background)',
                flexShrink: 0
            }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                    <span style={{
                        width: 8, height: 8, borderRadius: '50%', display: 'inline-block',
                        background: connected ? '#2ecc71' : (error ? '#e74c3c' : '#95a5a6'),
                        boxShadow: connected ? '0 0 6px #2ecc7188' : 'none',
                        animation: connected ? 'pulse 2s infinite' : 'none'
                    }} />
                    <span style={{ fontWeight: 600, fontSize: 13 }}>Market Watch</span>
                    <span style={{
                        fontSize: 10, padding: '1px 6px', borderRadius: 3,
                        background: 'var(--theia-badge-background)',
                        color: 'var(--theia-badge-foreground)'
                    }}>DEBUG</span>
                </div>

                <input
                    type="text"
                    placeholder="Filter symbols..."
                    value={filter}
                    onChange={e => setFilter(e.target.value)}
                    style={{
                        flex: 1, maxWidth: 200,
                        padding: '3px 8px', fontSize: 12,
                        background: 'var(--theia-input-background)',
                        color: 'var(--theia-input-foreground)',
                        border: '1px solid var(--theia-input-border)',
                        borderRadius: 4, outline: 'none'
                    }}
                />

                <span style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)', marginLeft: 'auto' }}>
                    {quotes.length} symbol{quotes.length !== 1 ? 's' : ''}
                    {lastUpdate && ` · updated ${lastUpdate.toLocaleTimeString()}`}
                </span>

                <button
                    onClick={fetchQuotes}
                    style={{
                        padding: '3px 10px', fontSize: 11, cursor: 'pointer',
                        background: 'var(--theia-button-background)',
                        color: 'var(--theia-button-foreground)',
                        border: 'none', borderRadius: 4
                    }}
                >↻ Refresh</button>
            </div>

            {error && (
                <div style={{
                    padding: '6px 12px', fontSize: 12,
                    background: 'var(--theia-inputValidation-errorBackground, #5a1d1d)',
                    color: 'var(--theia-errorForeground)',
                    borderBottom: '1px solid var(--theia-inputValidation-errorBorder)',
                    flexShrink: 0
                }}>
                    ⚠ {error}
                </div>
            )}

            {/* Market status, stated once at the top. The page previously gave no
                indication of market state, so a correctly-closed weekend looked like a
                broken feed. */}
            <div style={{
                padding: '5px 12px', fontSize: 11, flexShrink: 0,
                color: marketSummary.color,
                borderBottom: '1px solid var(--theia-border)',
                background: 'var(--theia-sideBarSectionHeader-background)',
            }}>
                {marketSummary.text}
            </div>

            {/* Table */}
            <div style={{ flex: 1, overflow: 'auto' }}>
                {filtered.length === 0 ? (
                    <div style={{
                        display: 'flex', flexDirection: 'column', alignItems: 'center',
                        justifyContent: 'center', height: '100%', gap: 8,
                        color: 'var(--theia-descriptionForeground)', fontSize: 13
                    }}>
                        <span style={{ fontSize: 32 }}>📊</span>
                        <span>{filter ? `No symbols matching "${filter}"` : 'No live quotes yet.'}</span>
                        <span style={{ fontSize: 11 }}>
                            {!filter && 'Make sure the Data Feed is connected and symbols are configured.'}
                        </span>
                    </div>
                ) : (
                    <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 12 }}>
                        <thead>
                            <tr style={{
                                background: 'var(--theia-sideBarSectionHeader-background)',
                                position: 'sticky', top: 0, zIndex: 1
                            }}>
                                <th style={thStyle}>Symbol</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Bid</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Ask</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Spread</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Last Update</th>
                                <th style={{ ...thStyle, textAlign: 'center' }}>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filtered.map(row => (
                                <tr key={row.symbol} style={{
                                    borderBottom: '1px solid var(--theia-panel-border)',
                                    transition: 'background 0.2s'
                                }}>
                                    <td style={{ ...tdStyle, fontWeight: 600, letterSpacing: '0.5px' }}>
                                        {row.symbol}
                                    </td>
                                    <td style={{
                                        ...tdStyle, textAlign: 'right', fontFamily: 'monospace',
                                        fontWeight: 600, fontSize: 13,
                                        color: row.flashBid === 'up' ? '#2ecc71'
                                            : row.flashBid === 'down' ? '#e74c3c'
                                            : 'var(--theia-foreground)',
                                        transition: 'color 0.3s'
                                    }}>
                                        {row.flashBid === 'up' ? '▲ ' : row.flashBid === 'down' ? '▼ ' : ''}
                                        {formatPrice(row.bid)}
                                    </td>
                                    <td style={{
                                        ...tdStyle, textAlign: 'right', fontFamily: 'monospace',
                                        fontWeight: 600, fontSize: 13,
                                        color: row.flashAsk === 'up' ? '#2ecc71'
                                            : row.flashAsk === 'down' ? '#e74c3c'
                                            : 'var(--theia-foreground)',
                                        transition: 'color 0.3s'
                                    }}>
                                        {row.flashAsk === 'up' ? '▲ ' : row.flashAsk === 'down' ? '▼ ' : ''}
                                        {formatPrice(row.ask)}
                                    </td>
                                    <td style={{ ...tdStyle, textAlign: 'right', color: 'var(--theia-descriptionForeground)', fontFamily: 'monospace' }}>
                                          {row.spread == null ? '\u2014' : (row.bid != null && row.bid > 100 ? row.spread.toFixed(2) : row.spread.toFixed(1))}
                                    </td>
                                    <td style={{ ...tdStyle, textAlign: 'right', color: ageColor(row.age, row), fontFamily: 'monospace' }}>
                                        {formatAge(row.age)}
                                    </td>
                                      {/* The real market state, as a labelled badge. This column used to
                                          be a bare dot driven only by age, so a correctly-closed weekend
                                          and a dead feed looked identical. */}
                                      <td style={{ ...tdStyle, textAlign: 'center' }}>
                                          {(() => {
                                              const badge = marketStateBadge(row.marketState);
                                              return (
                                                  <span
                                                      title={
                                                          row.marketState === 'closed'
                                                              ? "Outside this symbol's trading session. The last price is the last real price."
                                                              : row.marketState === 'no_data'
                                                                  ? 'No quote has been received for this symbol.'
                                                                  : 'Inside the trading session.'
                                                      }
                                                      style={{
                                                          display: 'inline-flex', alignItems: 'center', gap: 5,
                                                          fontSize: 10, color: badge.color, whiteSpace: 'nowrap',
                                                      }}
                                                  >
                                                      <span style={{
                                                          display: 'inline-block', width: 7, height: 7,
                                                          borderRadius: '50%', background: badge.color,
                                                          boxShadow: row.marketState === 'open' ? '0 0 5px #2ecc7188' : 'none',
                                                      }} />
                                                      {badge.label}
                                                  </span>
                                              );
                                          })()}
                                      </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>

            <style>{`
                @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }
            `}</style>
        </div>
    );
}

const thStyle: React.CSSProperties = {
    padding: '6px 10px',
    textAlign: 'left',
    fontWeight: 600,
    fontSize: 11,
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
    color: 'var(--theia-descriptionForeground)',
    borderBottom: '1px solid var(--theia-panel-border)',
    whiteSpace: 'nowrap'
};

const tdStyle: React.CSSProperties = {
    padding: '5px 10px',
    whiteSpace: 'nowrap'
};
