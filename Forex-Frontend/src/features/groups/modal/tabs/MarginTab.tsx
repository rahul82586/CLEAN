import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const RISK_MODELS = [
    { value: 'netting', label: 'Retail Forex, CFD, Futures (netting)' },
    { value: 'hedging', label: 'Retail Forex, CFD, Futures (hedging)' },
    { value: 'discount', label: 'Exchange (margin discount rates)' },
];

export function MarginTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const isHedging = draft.risk_management_model === 'hedging';

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
                    Please set up the mechanism of margin calculation for the group: choose the method of calculation and margin requirements.
                </div>
            </div>

            {/* Form Fields arranged exactly like MT5 */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 7, maxWidth: 540 }}>
                {/* Row 1: Risk management (wide) */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Risk management:</span>
                    <select
                        className="adm-select"
                        style={{ width: 280, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.risk_management_model}
                        onChange={e => updateField('risk_management_model', e.target.value)}
                    >
                        {RISK_MODELS.map(m => (
                            <option key={m.value} value={m.value}>{m.label}</option>
                        ))}
                    </select>
                </div>

                {/* Row 2: Margin call level & Stop out level & in (percent/money) */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Margin call level:</span>
                    <input
                        className="adm-input"
                        type="number"
                        style={{ width: 65, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.margin_call}
                        onChange={e => updateField('margin_call', parseFloat(e.target.value) || 0)}
                    />
                    <span style={{ opacity: 0.85, marginLeft: 8, whiteSpace: 'nowrap' }}>Stop out level:</span>
                    <input
                        className="adm-input"
                        type="number"
                        style={{ width: 65, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.margin_stop_out}
                        onChange={e => updateField('margin_stop_out', parseFloat(e.target.value) || 0)}
                    />
                    <span style={{ opacity: 0.85, marginLeft: 8 }}>in</span>
                    <select
                        className="adm-select"
                        style={{ width: 75, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.stop_out_mode}
                        onChange={e => updateField('stop_out_mode', e.target.value)}
                    >
                        <option value="percent">%</option>
                        <option value="money">USD</option>
                    </select>
                </div>

                {/* Checkboxes below */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginTop: 4, paddingLeft: 148 }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer', opacity: isHedging ? 1 : 0.6 }}>
                        <input
                            type="checkbox"
                            disabled={!isHedging}
                            checked={isHedging && draft.stop_out_hedged}
                            onChange={e => updateField('stop_out_hedged', e.target.checked)}
                        />
                        <span>Stop out fully hedged accounts</span>
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                        <input
                            type="checkbox"
                            checked={draft.compensate_negative_balance}
                            onChange={e => updateField('compensate_negative_balance', e.target.checked)}
                        />
                        <span>Compensate negative balance after stop out</span>
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer', opacity: draft.compensate_negative_balance ? 1 : 0.6 }}>
                        <input
                            type="checkbox"
                            disabled={!draft.compensate_negative_balance}
                            checked={draft.compensate_negative_balance && draft.withdraw_credit_after_comp}
                            onChange={e => updateField('withdraw_credit_after_comp', e.target.checked)}
                        />
                        <span>Withdraw credit after negative balance compensation</span>
                    </label>
                </div>

                {/* Profit/loss in free margin Groupbox fieldset */}
                <fieldset style={{
                    marginTop: 8,
                    marginLeft: 148,
                    border: '1px solid var(--theia-border)',
                    borderRadius: 4,
                    padding: '8px 12px 10px 12px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: 7
                }}>
                    <legend style={{ padding: '0 4px', opacity: 0.9, fontSize: 11, fontWeight: 'bold' }}>
                        Profit/loss in free margin
                    </legend>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Unrealized profit:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.unrealized_profit_mode}
                            onChange={e => updateField('unrealized_profit_mode', parseInt(e.target.value))}
                        >
                            <option value={0}>Do not use unrealized profit/loss</option>
                            <option value={1}>Use both profit and loss</option>
                            <option value={2}>Use unrealized loss only</option>
                            <option value={3}>Use unrealized profit only</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Daily fixed profit:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.daily_fixed_profit_mode}
                            onChange={e => updateField('daily_fixed_profit_mode', parseInt(e.target.value))}
                        >
                            <option value={0}>Do not use daily fixed profit/loss</option>
                            <option value={1}>Use daily fixed profit/loss</option>
                        </select>
                    </div>

                    <div style={{ paddingLeft: 118 }}>
                        <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer', opacity: draft.daily_fixed_profit_mode === 1 ? 1 : 0.6 }}>
                            <input
                                type="checkbox"
                                disabled={draft.daily_fixed_profit_mode !== 1}
                                checked={draft.daily_fixed_profit_mode === 1 && draft.release_fixed_profit}
                                onChange={e => updateField('release_fixed_profit', e.target.checked)}
                            />
                            <span>Release fixed profit at the end of day</span>
                        </label>
                    </div>
                </fieldset>

                {/* Virtual credit row below groupbox */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Virtual credit:</span>
                    <input
                        className="adm-input"
                        type="number"
                        style={{ width: 90, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="0.00"
                        value={draft.virtual_credit || ''}
                        onChange={e => updateField('virtual_credit', parseFloat(e.target.value) || 0)}
                    />
                    <span style={{ opacity: 0.75, fontSize: 11 }}>(applies only to opening new positions)</span>
                </div>
            </div>
        </div>
    );
}
