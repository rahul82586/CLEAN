// @ts-nocheck
// Sessions tab — MT5's quoting / trading timetable.
//
// Three defects this file fixes:
//
// 1. The schedule was SEEDED, never LOADED. Every day defaulted to
//    `00:00-24:00` regardless of what the symbol actually had, so opening the tab
//    showed a full 24/7 week for a symbol that trades five days. It now reads the
//    real calendar from GET /admin/symbols/{name}/sessions.
//
// 2. `24:00` was bound to `<input type="time">`, which only accepts 00:00–23:59.
//    The browser discarded it and showed 12:00 AM — the "always goes to 12:00"
//    symptom. Times now live as MINUTES (see sessionModel.ts), so 1440 is
//    representable, and the input renders 23:59 with an explicit hint.
//
// 3. Nothing was ever sent to the backend in a form it could store. The save path
//    now emits `session_hours`, which the API accepts.
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';
import { DayScheduleEditor } from './sessions/DayScheduleEditor';
import {
    DISPLAY_DAYS,
    END_OF_DAY,
    SessionRange,
    defaultWeek,
    fromSessionHours,
    minutesToLabel,
    toSessionHours,
} from './sessions/sessionModel';
import { API } from '../../../../services/api';

interface DaySchedule {
    quotes: SessionRange[];
    trade: SessionRange[];
    separateTrade: boolean;
}

const EMPTY_DAY: DaySchedule = { quotes: [], trade: [], separateTrade: false };

export function SessionsTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();
    const [selectedDay, setSelectedDay] = React.useState<string | null>(null);
    const [schedules, setSchedules] = React.useState<Record<string, DaySchedule>>({});
    const [status, setStatus] = React.useState<string>('');

    const symbolName = draft.symbol;

    // Load the REAL calendar. MT5's SessionsQuotes/SessionsTrades arrive as
    // 7-element SUNDAY-FIRST arrays of {open_minutes, close_minutes}; the model is
    // keyed by day name, so the mapping goes through MT5's index, never Python's
    // Monday-first weekday() or a display order.
    React.useEffect(() => {
        let cancelled = false;

        const seed = (week: Record<string, SessionRange[]>, trade: Record<string, SessionRange[]>) => {
            const next: Record<string, DaySchedule> = {};
            for (const day of DISPLAY_DAYS) {
                const quotes = week[day] ?? [];
                const tradeRanges = trade[day] ?? [];
                const same = JSON.stringify(quotes) === JSON.stringify(tradeRanges);
                next[day] = {
                    quotes,
                    trade: same ? [] : tradeRanges,
                    separateTrade: !same,
                };
            }
            return next;
        };

        // Start from a sane week so the tab is usable before the fetch resolves,
        // but do NOT treat it as the symbol's real schedule.
        setSchedules(seed(defaultWeek(), defaultWeek()));

        if (!symbolName) return () => { cancelled = true; };

        (async () => {
            try {
                const raw = await API.getSymbolSessions(symbolName);
                if (cancelled || !raw) return;

                // The API returns a dict keyed by MT5's day index -> ranges, or the
                // explicit per-day list. Normalise whichever we get.
                const toDayMap = (value: any): Record<string, SessionRange[]> => {
                    const out: Record<string, SessionRange[]> = {};
                    for (const day of DISPLAY_DAYS) out[day] = [];
                    if (!value) return out;
                    if (Array.isArray(value)) {
                        for (const entry of value) {
                            const idx = Number(entry?.index ?? entry?.day_of_week ?? 0) || 0;
                            const day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                                         'Thursday', 'Friday', 'Saturday'][idx];
                            if (!day) continue;
                            out[day] = (entry?.sessions || []).map((s: any) => ({
                                open: Number(s.open_minutes ?? 0),
                                close: Number(s.close_minutes ?? 0),
                            }));
                        }
                        return out;
                    }
                    if (typeof value === 'object') {
                        for (const [key, ranges] of Object.entries(value)) {
                            const idx = Number(key);
                            const day = Number.isNaN(idx)
                                ? key
                                : ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                                   'Thursday', 'Friday', 'Saturday'][idx];
                            if (!day) continue;
                            out[day] = (ranges as any[] || []).map((s: any) => ({
                                open: Number(s.open_minutes ?? s.open ?? 0),
                                close: Number(s.close_minutes ?? s.close ?? 0),
                            }));
                        }
                    }
                    return out;
                };

                const quoteMap = toDayMap(raw.quote_sessions ?? raw.sessions_quotes);
                const tradeMap = toDayMap(raw.trade_sessions ?? raw.sessions_trades);
                const anyConfigured = [...Object.values(quoteMap), ...Object.values(tradeMap)]
                    .some(r => (r as SessionRange[]).length > 0);
                if (anyConfigured) setSchedules(seed(quoteMap, tradeMap));
            } catch (e) {
                // An unreadable calendar must not silently look like "24/7 open":
                // say so, and leave the safe default week in place.
                if (!cancelled) setStatus('Could not load the stored calendar — showing a default week. ' + String(e));
            }
        })();

        return () => { cancelled = true; };
    }, [symbolName]);

    // Publish to the draft so the modal's PUT carries the schedule.
    React.useEffect(() => {
        if (Object.keys(schedules).length === 0) return;
        const hours = toSessionHours(schedules);
        setDraft(prev => (prev.session_hours === hours ? prev : { ...prev, session_hours: hours }));
    }, [schedules, setDraft]);

    const handleSaveDaySchedule = (day: string, daySched: DaySchedule) => {
        setSchedules(prev => ({ ...prev, [day]: daySched }));
        setSelectedDay(null);
    };

    const [useLimits, setUseLimits] = React.useState(false);
    const [limitFrom, setLimitFrom] = React.useState('');
    const [limitTo, setLimitTo] = React.useState('');

    const renderRanges = (ranges: SessionRange[]) =>
        ranges.map(r => `${minutesToLabel(r.open)}-${minutesToLabel(r.close)}`).join(', ');

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#f1c40f', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    T
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure the weekly quoting and trading timetable for this symbol.
                    Times are server time. <strong>24:00 means end of day</strong> — a
                    full-day session is stored as 1440 minutes, not 23:59.
                </div>
            </div>

            {status && (
                <div style={{ padding: '4px 8px', borderRadius: 3, background: 'rgba(241,196,15,0.15)', border: '1px solid #f1c40f' }}>
                    {status}
                </div>
            )}

            <div style={{ display: 'grid', gridTemplateColumns: '1.1fr 0.9fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 10, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Weekly Timetable
                    </div>

                    <div className="adm-table-wrap" style={{ border: '1px solid var(--theia-border)', height: 140, overflowY: 'auto' }}>
                        <table className="adm-table" style={{ fontSize: 10 }}>
                            <thead>
                                <tr>
                                    <th>Day</th>
                                    <th>Quotes Session</th>
                                    <th>Trade Session</th>
                                </tr>
                            </thead>
                            <tbody>
                                {DISPLAY_DAYS.map(day => {
                                    const sched = schedules[day] || EMPTY_DAY;
                                    const quotesStr = renderRanges(sched.quotes) || 'Closed';
                                    const tradeStr = sched.separateTrade
                                        ? (renderRanges(sched.trade) || 'Closed')
                                        : 'Same as Quotes';
                                    return (
                                        <tr
                                            key={day}
                                            className={selectedDay === day ? 'selected' : ''}
                                            onClick={() => setSelectedDay(day)}
                                            onDoubleClick={() => setSelectedDay(day)}
                                            style={{ cursor: 'pointer', height: 18 }}
                                        >
                                            <td><strong>{day.substring(0, 3)}</strong></td>
                                            <td>{quotesStr}</td>
                                            <td>{tradeStr}</td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 10, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Symbol Validity Period
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input type="checkbox" checked={useLimits} onChange={e => setUseLimits(e.target.checked)} />
                        Limit the symbol&apos;s active period
                    </label>

                    {useLimits && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 50, opacity: 0.8 }}>From:</span>
                                <input className="adm-input" type="date" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={limitFrom} onChange={e => setLimitFrom(e.target.value)} />
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 50, opacity: 0.8 }}>To:</span>
                                <input className="adm-input" type="date" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={limitTo} onChange={e => setLimitTo(e.target.value)} />
                            </div>
                        </div>
                    )}
                </div>
            </div>

            {selectedDay && (
                <DayScheduleEditor
                    day={selectedDay}
                    schedule={schedules[selectedDay] || EMPTY_DAY}
                    onClose={() => setSelectedDay(null)}
                    onSave={(sched) => handleSaveDaySchedule(selectedDay, sched)}
                />
            )}
        </div>
    );
}

export { END_OF_DAY, fromSessionHours };
