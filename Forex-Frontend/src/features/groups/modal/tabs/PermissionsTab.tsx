import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const HISTORY_OPTIONS = [
    'Entire history',
    '1 month',
    '3 months',
    '6 months',
    '1 year',
    '3 years',
];

const LEVERAGE_OPTIONS = [
    { value: 1, label: '1:1' },
    { value: 10, label: '1:10' },
    { value: 25, label: '1:25' },
    { value: 50, label: '1:50' },
    { value: 100, label: '1:100' },
    { value: 200, label: '1:200' },
    { value: 400, label: '1:400' },
    { value: 500, label: '1:500' },
    { value: 1000, label: '1:1000' },
];

const SIGNALS_OPTIONS = [
    { value: 'disabled', label: 'Disabled' },
    { value: 'all', label: 'Enable all signals' },
    { value: 'own_only', label: 'From my servers only' },
];

const TRANSFER_OPTIONS = [
    { value: 'disabled', label: 'Disabled' },
    { value: 'same_details', label: 'Between accounts with identical name and email' },
    { value: 'subgroup', label: 'Within group' },
    { value: 'subgroup_name', label: 'Within group and identical name' },
];

export function PermissionsTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 14, fontSize: 11 }}>
            {/* Top MT5 Group Header Banner */}
            <div style={{ display: 'flex', gap: 14, alignItems: 'flex-start', paddingBottom: 6 }}>
                <svg width="42" height="42" viewBox="0 0 48 48" fill="none" style={{ flexShrink: 0, marginTop: 2 }}>
                    <circle cx="18" cy="14" r="7" fill="#2ecc71" />
                    <path d="M6 38 C6 27, 30 27, 30 38 Z" fill="#2ecc71" />
                    <circle cx="32" cy="15" r="6" fill="#27ae60" />
                    <path d="M23 38 C23 29, 42 29, 42 38 Z" fill="#27ae60" />
                </svg>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.4, fontSize: 11 }}>
                    Please specify the group permissions for symbols, orders, use of Expert Advisors, etc.
                </div>
            </div>

            {/* MT5 Permissions Form Fields */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 7, maxWidth: 540 }}>
                {/* Row 1: Maximum symbols & Available history */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: '1 1 270px' }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Maximum symbols:</span>
                        <input
                            className="adm-input"
                            type="number"
                            min={0}
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            placeholder="0 (Unlimited)"
                            value={draft.max_symbols || ''}
                            onChange={e => updateField('max_symbols', parseInt(e.target.value) || 0)}
                        />
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: 220 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Available history:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.available_history}
                            onChange={e => updateField('available_history', e.target.value)}
                        >
                            {HISTORY_OPTIONS.map(h => (
                                <option key={h} value={h}>{h}</option>
                            ))}
                        </select>
                    </div>
                </div>

                {/* Row 2: Maximum positions & Maximum orders */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: '1 1 270px' }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Maximum positions:</span>
                        <input
                            className="adm-input"
                            type="number"
                            min={0}
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            placeholder="0 (Unlimited)"
                            value={draft.max_positions || ''}
                            onChange={e => updateField('max_positions', parseInt(e.target.value) || 0)}
                        />
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: 220 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Maximum orders:</span>
                        <input
                            className="adm-input"
                            type="number"
                            min={0}
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            placeholder="0 (Unlimited)"
                            value={draft.max_orders || ''}
                            onChange={e => updateField('max_orders', parseInt(e.target.value) || 0)}
                        />
                    </div>
                </div>

                {/* Row 3: Deposit by default & Leverage by default */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: '1 1 270px' }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Deposit by default:</span>
                        <input
                            className="adm-input"
                            type="number"
                            min={0}
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.default_deposit || ''}
                            onChange={e => updateField('default_deposit', parseFloat(e.target.value) || 0)}
                        />
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: 220 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Leverage by default:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.default_leverage}
                            onChange={e => updateField('default_leverage', parseInt(e.target.value) || 100)}
                        >
                            {LEVERAGE_OPTIONS.map(l => (
                                <option key={l.value} value={l.value}>{l.label}</option>
                            ))}
                        </select>
                    </div>
                </div>

                {/* Row 4: Annual interest rate */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Annual interest rate:</span>
                    <input
                        className="adm-input"
                        type="number"
                        step="0.01"
                        style={{ width: 90, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.interest_rate}
                        onChange={e => updateField('interest_rate', parseFloat(e.target.value) || 0)}
                    />
                    <span>%</span>
                </div>

                {/* Row 5: Trading Signals (wide) */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Trading Signals:</span>
                    <select
                        className="adm-select"
                        style={{ width: 280, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.trade_signals_mode}
                        onChange={e => updateField('trade_signals_mode', e.target.value)}
                    >
                        {SIGNALS_OPTIONS.map(s => (
                            <option key={s.value} value={s.value}>{s.label}</option>
                        ))}
                    </select>
                </div>

                {/* Row 6: Transfer of funds (wide) */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Transfer of funds:</span>
                    <select
                        className="adm-select"
                        style={{ width: 340, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.transfer_funds_mode}
                        onChange={e => updateField('transfer_funds_mode', e.target.value)}
                    >
                        {TRANSFER_OPTIONS.map(t => (
                            <option key={t.value} value={t.value}>{t.label}</option>
                        ))}
                    </select>
                </div>

                {/* Checkbox Grid (2 parallel columns aligned below inputs) */}
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 20px', marginTop: 10, paddingLeft: 148 }}>
                    {/* Left Column */}
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 7 }}>
                        <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                            <input
                                type="checkbox"
                                checked={draft.enable_ea_trading}
                                onChange={e => updateField('enable_ea_trading', e.target.checked)}
                            />
                            <span>Enable trading by Expert Advisors</span>
                        </label>

                        <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                            <input
                                type="checkbox"
                                checked={draft.enable_trailing_stops}
                                onChange={e => updateField('enable_trailing_stops', e.target.checked)}
                            />
                            <span>Enable trailing stops</span>
                        </label>

                        <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                            <input
                                type="checkbox"
                                checked={draft.enable_swaps}
                                onChange={e => updateField('enable_swaps', e.target.checked)}
                            />
                            <span>Enable charge of swaps</span>
                        </label>
                    </div>

                    {/* Right Column */}
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 7 }}>
                        <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                            <input
                                type="checkbox"
                                checked={draft.fifo_rule}
                                onChange={e => updateField('fifo_rule', e.target.checked)}
                            />
                            <span>Enable position closing according to FIFO rule</span>
                        </label>

                        <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                            <input
                                type="checkbox"
                                checked={draft.prohibit_hedge}
                                onChange={e => updateField('prohibit_hedge', e.target.checked)}
                            />
                            <span>Prohibit hedge positions</span>
                        </label>

                        <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                            <input
                                type="checkbox"
                                checked={draft.deal_cost_calc}
                                onChange={e => updateField('deal_cost_calc', e.target.checked)}
                            />
                            <span>Enable deal cost calculation</span>
                        </label>
                    </div>
                </div>
            </div>
        </div>
    );
}

