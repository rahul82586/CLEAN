// @ts-nocheck
// Day session editor.
//
// The time fields were bound directly to `{ start, end }` strings seeded with
// '24:00'. HTML `<input type="time">` accepts only 00:00–23:59, so '24:00' was
// discarded by the browser and the field showed 12:00 AM.
//
// Ranges are now held as MINUTES, so 1440 (= 24:00, MT5's end of day) is a real,
// storable value. The native input renders it as 23:59 for display only, and an
// explicit hint says what that means, because a 12-hour locale would otherwise
// show 00:00 as "12:00 AM" and the operator would have no way to tell a
// midnight-open session from a noon one.
import * as React from 'react';
import {
    END_OF_DAY,
    SessionRange,
    labelToMinutes,
    minutesToLabel,
    minutesToTimeInput,
    isFullDay,
} from './sessionModel';

interface DayScheduleEditorProps {
    day: string;
    schedule: {
        quotes: SessionRange[];
        trade: SessionRange[];
        separateTrade: boolean;
    };
    onClose: () => void;
    onSave: (schedule: any) => void;
}

export function DayScheduleEditor({ day, schedule, onClose, onSave }: DayScheduleEditorProps): React.ReactElement {
    const [quotes, setQuotes] = React.useState<SessionRange[]>([...schedule.quotes]);
    const [trade, setTrade] = React.useState<SessionRange[]>([...schedule.trade]);
    const [separateTrade, setSeparateTrade] = React.useState(schedule.separateTrade);

    const handleAddBlock = (type: 'quotes' | 'trade', fullDay = false) => {
        // A new block defaults to the whole day, which is what an operator setting
        // up a 24-hour instrument wants; a partial day is then edited in place.
        const block: SessionRange = fullDay ? { open: 0, close: END_OF_DAY } : { open: 480, close: 1020 };
        if (type === 'quotes') setQuotes([...quotes, block]);
        else setTrade([...trade, block]);
    };

    const handleRemoveBlock = (type: 'quotes' | 'trade', index: number) => {
        if (type === 'quotes') setQuotes(quotes.filter((_, i) => i !== index));
        else setTrade(trade.filter((_, i) => i !== index));
    };

    const handleTimeChange = (
        type: 'quotes' | 'trade',
        index: number,
        field: 'open' | 'close',
        label: string,
    ) => {
        const minutes = labelToMinutes(label);
        if (minutes === null) return;
        const apply = (ranges: SessionRange[]) => {
            const next = [...ranges];
            next[index] = { ...next[index], [field]: minutes };
            return next;
        };
        if (type === 'quotes') setQuotes(apply(quotes));
        else setTrade(apply(trade));
    };

    const handleSave = () => {
        onSave({
            quotes,
            trade: separateTrade ? trade : [...quotes],
            separateTrade,
        });
    };

    const renderBlocks = (type: 'quotes' | 'trade', ranges: SessionRange[]) => (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
            {ranges.map((block, idx) => {
                const wide = isFullDay(block);
                return (
                    <div key={idx} style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                        <input
                            className="adm-input"
                            type="time"
                            style={{ width: 110, fontSize: 11, padding: 3, height: 22 }}
                            value={minutesToTimeInput(block.open)}
                            onChange={e => handleTimeChange(type, idx, 'open', e.target.value)}
                        />
                        <span>to</span>
                        <input
                            className="adm-input"
                            type="time"
                            style={{ width: 110, fontSize: 11, padding: 3, height: 22 }}
                            value={minutesToTimeInput(block.close)}
                            onChange={e => handleTimeChange(type, idx, 'close', e.target.value)}
                        />
                        {wide ? (
                            <span style={{ fontSize: 10, opacity: 0.75, minWidth: 78 }}>
                                24:00 (full day)
                            </span>
                        ) : (
                            <span style={{ fontSize: 10, opacity: 0.45, minWidth: 78 }}>
                                {minutesToLabel(block.open)}–{minutesToLabel(block.close)}
                            </span>
                        )}
                        <button type="button" className="adm-icon-btn" onClick={() => handleRemoveBlock(type, idx)}>
                            <i className="codicon codicon-trash" style={{ color: 'var(--theia-errorForeground)' }} />
                        </button>
                    </div>
                );
            })}
        </div>
    );

    return (
        <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={onClose}>
            <div className="adm-modal" style={{ width: 500 }} onClick={e => e.stopPropagation()}>
                <div className="adm-modal-header">
                    <h2>Edit Time Sessions — {day}</h2>
                    <button type="button" className="adm-modal-close" onClick={onClose}>×</button>
                </div>
                <div className="adm-modal-body" style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>

                    <div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                            <span style={{ fontSize: 12, fontWeight: 'bold' }}>Quotes Sessions</span>
                            <span style={{ display: 'flex', gap: 6 }}>
                                <button type="button" className="adm-btn" style={{ fontSize: 10, padding: '2px 8px' }} onClick={() => handleAddBlock('quotes', true)}>
                                    <i className="codicon codicon-add" /> 24h
                                </button>
                                <button type="button" className="adm-btn" style={{ fontSize: 10, padding: '2px 8px' }} onClick={() => handleAddBlock('quotes')}>
                                    <i className="codicon codicon-add" /> Session
                                </button>
                            </span>
                        </div>

                        {quotes.length === 0 ? (
                            <div style={{ padding: 12, background: 'var(--theia-sideBarSectionHeader-background)', fontSize: 11, textAlign: 'center', opacity: 0.6 }}>
                                No quotes session — the market is closed all day and no ticks are collected.
                            </div>
                        ) : renderBlocks('quotes', quotes)}
                    </div>

                    <div className="adm-form-row" style={{ flexDirection: 'row', alignItems: 'center', gap: 8, borderTop: '1px solid var(--theia-border)', paddingTop: 10 }}>
                        <input type="checkbox" id="sep-trade" checked={separateTrade} onChange={e => setSeparateTrade(e.target.checked)} />
                        <label htmlFor="sep-trade" style={{ cursor: 'pointer', margin: 0, fontSize: 12 }}>
                            Enable separate trading sessions (different from quotes)
                        </label>
                    </div>

                    {separateTrade && (
                        <div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                                <span style={{ fontSize: 12, fontWeight: 'bold' }}>Trade Sessions</span>
                                <span style={{ display: 'flex', gap: 6 }}>
                                    <button type="button" className="adm-btn" style={{ fontSize: 10, padding: '2px 8px' }} onClick={() => handleAddBlock('trade', true)}>
                                        <i className="codicon codicon-add" /> 24h
                                    </button>
                                    <button type="button" className="adm-btn" style={{ fontSize: 10, padding: '2px 8px' }} onClick={() => handleAddBlock('trade')}>
                                        <i className="codicon codicon-add" /> Session
                                    </button>
                                </span>
                            </div>

                            {trade.length === 0 ? (
                                <div style={{ padding: 12, background: 'var(--theia-sideBarSectionHeader-background)', fontSize: 11, textAlign: 'center', opacity: 0.6 }}>
                                    No trading session — clients cannot execute trades, though quotes may still arrive.
                                </div>
                            ) : renderBlocks('trade', trade)}
                        </div>
                    )}

                    <div style={{ fontSize: 10, opacity: 0.65, borderTop: '1px solid var(--theia-border)', paddingTop: 8 }}>
                        Times are the trade server&apos;s local time. Leave a day with no session to close it.
                        A session that ends at <strong>24:00</strong> is stored as 1440 minutes, i.e. the end of the day.
                    </div>
                </div>
                <div className="adm-modal-footer">
                    <button type="button" className="adm-btn adm-btn-primary" onClick={handleSave}>Save changes</button>
                    <button type="button" className="adm-btn" onClick={onClose}>Cancel</button>
                </div>
            </div>
        </div>
    );
}
