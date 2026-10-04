import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';
import { enumOptions, fieldsForTab, labelForValue, useSymbolSchema } from '../useSymbolSchema';
import {
    showsConvertProfit,
    showsTickSizeAndValue,
} from './tradeFieldVisibility';

// Calculation and Trade mode options come from GET /admin/symbols/schema, which
// the backend generates from core.domains.instruments.enums. The lists that used
// to sit here were stale in the same way the backend's map was:
//
//   'Forex No Leverage' was listed for the position MT5 gives to CalcMode 1
//   (Futures), and 'Exchange Stocks' for CalcMode 5 (which is actually
//   Forex No Leverage — 54 symbols in the live export).
//
// Deriving them means a mode cannot be shown under the wrong name, and the list
// cannot contain a value the API would reject.
//
// The fallbacks below are only used until the schema resolves. They carry the
// CORRECTED MT5 values, never the old ones.
const CALC_MODE_FALLBACK = [
    'Forex', 'Futures', 'CFD', 'CFD Index', 'CFD Leverage', 'Forex No Leverage',
    'Exchange Stocks', 'Exchange Futures', 'Exchange FORTS Futures',
    'Exchange Option', 'Exchange Margin Option', 'Exchange Bonds',
    'Exchange MOEX Stocks', 'Exchange MOEX Bonds', 'Collateral',
];

const TRADE_MODE_FALLBACK = [
    { value: 'disabled', label: 'Disabled (no trading)' },
    { value: 'long_only', label: 'Long only (buys allowed)' },
    { value: 'short_only', label: 'Short only (sells allowed)' },
    { value: 'close_only', label: 'Close only (liquidation only)' },
    { value: 'full', label: 'Full access (long & short)' },
];

//: MT5 EnOrderFlags. Named in one place so the checkboxes and the schema agree.
const ORDER_FLAG_BITS: Record<string, number> = {
    MARKET: 1, LIMIT: 2, STOP: 4, STOP_LIMIT: 8, SL: 16, TP: 32, CLOSEBY: 64,
};

function flagBit(name: string): number {
    return ORDER_FLAG_BITS[String(name).toUpperCase()] ?? 0;
}

export function TradeTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();
    const { schema } = useSymbolSchema();

    // --- options from the schema -------------------------------------------
    const calcField = fieldsForTab(schema, 'trade').find(f => f.field === 'calc_mode');
    const calcModes = calcField
        ? enumOptions(calcField).map(o => o.label)
        : CALC_MODE_FALLBACK;

    const tradeField = fieldsForTab(schema, 'trade').find(f => f.field === 'trade_mode');
    const tradeModes = tradeField
        ? enumOptions(tradeField).map(o => ({
              // the draft stores the long-standing string form
              value: String(o.label).toLowerCase().replace(/[^a-z]+/g, '_').replace(/^_|_$/g, ''),
              label: String(o.label),
          }))
        : TRADE_MODE_FALLBACK;

    // The MT5 enum member names, so a saved value can be matched back to its label.
    const calcLabelByEnumName = new Map(
        (calcField?.enum_values ?? []).map(v => [v.name, labelForValue(v.name)]),
    );

    // --- which fields this calculation mode shows --------------------------
    // See tradeFieldVisibility.ts for the two documented rules and their sources.
    const mode = draft.calculation;
    const showTickFields = showsTickSizeAndValue(mode);
    const showConvertProfit = showsConvertProfit(mode);

    // The order types a symbol accepts (MT5 Orders). Every symbol in the reference
    // export carries all seven bits, so the fallback is MT5's own ORDER_FLAGS_ALL.
    const orderField = fieldsForTab(schema, 'trade').find(f => f.field === 'order_flags');
    const orderOptions = orderField
        ? (orderField.enum_values ?? []).map(v => ({ name: v.name, label: labelForValue(v.name) }))
        : [
              { name: 'MARKET', label: 'Market' },
              { name: 'LIMIT', label: 'Limit' },
              { name: 'STOP', label: 'Stop' },
              { name: 'STOP_LIMIT', label: 'Stop Limit' },
              { name: 'SL', label: 'Stop Loss' },
              { name: 'TP', label: 'Take Profit' },
              { name: 'CLOSEBY', label: 'Close By' },
          ];

    // MT5's own single-value flags, for the toggle below.
    const ORDERS_ARE_DERIVED = false;

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const handleCheckboxArrayChange = (field: 'expiration_flags' | 'orders_allowed' | 'filling_flags', value: string, checked: boolean) => {
        const current = (draft[field] as string[]) || [];
        const next = checked ? [...current, value] : current.filter(item => item !== value);
        updateField(field, next);
    };

    const isForex = String(draft.calculation ?? '').startsWith('Forex');

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#e74c3c', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    T
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Set up contract size, calculation models, trade session modes, and volume order parameters.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1 }}>
                
                {/* Left Column (Contract Details) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Contract size:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.contract_size} onChange={e => updateField('contract_size', parseFloat(e.target.value) || 0.0)} />
                    </div>

                    {/* Tick size / Tick value are used by the CFD Index and Futures
                        formulas, so MT5 shows them for every mode EXCEPT Forex and
                        Forex No Leverage - where the live export confirms TickValue
                        is 0 on every symbol. The stored values are left untouched
                        while hidden; MT5 hides the inputs, it does not reject them. */}
                    {showTickFields && (
                        <>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Tick size:</span>
                                <input className="adm-input" type="number" step="0.00001" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.tick_size} onChange={e => updateField('tick_size', parseFloat(e.target.value) || 0.00001)} />
                            </div>

                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Tick value:</span>
                                <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.tick_value} onChange={e => updateField('tick_value', parseFloat(e.target.value) || 1.0)} />
                            </div>
                        </>
                    )}

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Calculation:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.calculation} onChange={e => updateField('calculation', e.target.value)}>
                            {calcModes.map(c => <option key={c} value={c}>{c}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Trade mode:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.trade_mode} onChange={e => updateField('trade_mode', e.target.value)}>
                            {tradeModes.map(m => <option key={m.value} value={m.value}>{m.label}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Limit/Stop level:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.stops_level ?? draft.limit_stop_level} onChange={e => {
                            const val = parseInt(e.target.value) || 0;
                            updateField('stops_level', val);
                            updateField('limit_stop_level', val);
                        }} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Freeze level:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.freeze_level} onChange={e => updateField('freeze_level', parseInt(e.target.value) || 0)} />
                    </div>
                </div>

                {/* Right Column (Permissions & Volume bounds) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>GTC mode:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.gtc_mode} onChange={e => updateField('gtc_mode', parseInt(e.target.value) || 0)}>
                            <option value={0}>Day canceled</option>
                            <option value={1}>Kept GTC</option>
                            <option value={2}>Kept except SL/TP</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Max quote delay:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.max_quote_delay} onChange={e => updateField('max_quote_delay', parseInt(e.target.value) || 15)} />
                    </div>

                    <div style={{ display: 'flex', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Filling flags:</span>
                        <div style={{ display: 'flex', gap: 8, fontSize: 10 }}>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                                <input
                                    type="checkbox"
                                    checked={(draft.filling_flags || []).includes('fok')}
                                    onChange={e => handleCheckboxArrayChange('filling_flags', 'fok', e.target.checked)}
                                /> FOK
                            </label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                                <input
                                    type="checkbox"
                                    checked={(draft.filling_flags || []).includes('ioc')}
                                    onChange={e => handleCheckboxArrayChange('filling_flags', 'ioc', e.target.checked)}
                                /> IOC
                            </label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                                <input
                                    type="checkbox"
                                    checked={(draft.filling_flags || []).includes('boc')}
                                    onChange={e => handleCheckboxArrayChange('filling_flags', 'boc', e.target.checked)}
                                /> BOC / Return
                            </label>
                        </div>
                    </div>

                    <div style={{ display: 'flex', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Expirations:</span>
                        <div style={{ display: 'flex', gap: 8, fontSize: 10 }}>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.expiration_flags.includes('gtc')} onChange={e => handleCheckboxArrayChange('expiration_flags', 'gtc', e.target.checked)} /> GTC</label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.expiration_flags.includes('day')} onChange={e => handleCheckboxArrayChange('expiration_flags', 'day', e.target.checked)} /> Day</label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.expiration_flags.includes('time')} onChange={e => handleCheckboxArrayChange('expiration_flags', 'time', e.target.checked)} /> Time</label>
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Volumes (min/max):</span>
                        <div style={{ flex: 1, display: 'flex', gap: 4 }}>
                            <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.min_volume} onChange={e => updateField('min_volume', parseFloat(e.target.value) || 0.01)} />
                            <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.max_volume} onChange={e => updateField('max_volume', parseFloat(e.target.value) || 100.0)} />
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Volume step:</span>
                        <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.step_volume} onChange={e => updateField('step_volume', parseFloat(e.target.value) || 0.01)} />
                    </div>

                    {/* MT5 Volume Limit: the maximum cumulative open volume in ONE
                        direction. It was in the draft and the API but never rendered,
                        so it could not be set. */}
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Volume limit:</span>
                        <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.limit_volume} onChange={e => updateField('limit_volume', parseFloat(e.target.value) || 0)} />
                    </div>

                    {/* MT5: "Convert profit - this option is available only for the
                        Forex type symbols", with exactly two values: by deal and by
                        market. It was previously both bound to `limit_volume` (so
                        choosing an option overwrote the VOLUME LIMIT) and offering
                        two labels that are not MT5's.

                        It writes TRADE_FLAGS_PROFIT_BY_MARKET, bit 1 of TradeFlags. */}
                    {showConvertProfit && (
                        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Convert profit:</span>
                            <select
                                className="adm-select"
                                style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                                value={Number(draft.trade_flags ?? 0) & 1 ? 1 : 0}
                                onChange={e => {
                                    const mask = Number(draft.trade_flags ?? 0);
                                    const next = e.target.value === '1' ? (mask | 1) : (mask & ~1);
                                    updateField('trade_flags', next);
                                }}
                            >
                                <option value={0}>By deal</option>
                                <option value={1}>By market</option>
                            </select>
                        </div>
                    )}

                    {/* MT5 Orders: which order types this symbol accepts. Present in
                        the draft, the schema and the API, but the tab never rendered
                        it - so the permission could not be configured at all. MT5
                        lists it for every calculation mode. */}
                    <div style={{ display: 'flex', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Orders:</span>
                        <div style={{ display: 'flex', gap: 6, fontSize: 10, flexWrap: 'wrap', flex: 1 }}>
                            {orderOptions.map(option => (
                                <label key={option.name} style={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                                    <input
                                        type="checkbox"
                                        checked={((Number(draft.order_flags ?? 127) & flagBit(option.name)) !== 0)}
                                        onChange={e => {
                                            const mask = Number(draft.order_flags ?? 127);
                                            const bit = flagBit(option.name);
                                            updateField('order_flags', e.target.checked ? (mask | bit) : (mask & ~bit));
                                        }}
                                    />
                                    {option.label}
                                </label>
                            ))}
                        </div>
                    </div>
                </div>

            </div>
        </div>
    );
}
