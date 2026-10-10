import * as React from 'react';
import { FloatingWindow } from '../../shared/FloatingWindow';
import { ConditionModal, RuleCondition } from './ConditionModal';
import { DealerPickerModal, RuleDealer } from './DealerPickerModal';

export interface RoutingRuleItem {
    id: number;
    name: string;
    priority?: number;
    is_enabled: boolean;
    action: string;
    action_type?: string;
    delay_ms?: number;
    delay_ticks?: number;
    reject_reason?: string;
    skip_if_no_dealers?: boolean;
    request_type?: string;
    order_type?: string;
    conditions?: RuleCondition[];
    dealers?: RuleDealer[];
}

interface RoutingRuleModalProps {
    rule?: RoutingRuleItem | null;
    isNew?: boolean;
    onClose: () => void;
    onSave: (rule: RoutingRuleItem) => void;
}

const MT5_ACTIONS = [
    'Process to dealers',
    'Process to online dealers',
    'Confirm by request price',
    'Confirm by market price',
    'Delay in milliseconds',
    'Delay in ticks',
    'Clear TP',
    'Clear SL',
    'Clear SLTP',
    'Reject',
    'Requote',
    'Cancel order',
];

const REQUEST_TYPES = [
    'All',
    'Request Execution, Instant Execution, Market Execution, Exchange Execution',
    'Price',
    'Request execution',
    'Instant execution',
    'Market execution',
    'Exchange execution',
    'Pending order',
    'SL & TP modification',
    'Order modification',
    'Order removal',
    'Close By',
    'Order activation',
    'Stop Limit activation',
    'SL activation',
    'TP activation',
    'Stop-Out order',
    'Stop-Out position',
    'Order expiration',
    'Execution by dealer',
    'Pending order by dealer',
    'Position modification by dealer',
    'Order modification by dealer',
    'Order removing by dealer',
    'Pending order activation by dealer',
    'Stop-Limit activation by dealer',
    'Close By by dealer',
];

const ORDER_TYPES = [
    'All',
    'Buy, Sell',
    'Buy',
    'Sell',
    'Buy Limit',
    'Sell Limit',
    'Buy Stop',
    'Sell Stop',
    'Buy Stop Limit',
    'Sell Stop Limit',
];

export function RoutingRuleModal({ rule, isNew, onClose, onSave }: RoutingRuleModalProps): React.ReactElement {
    const [activeTab, setActiveTab] = React.useState<'Common' | 'Dealers'>('Common');

    // Form draft
    const [draft, setDraft] = React.useState<RoutingRuleItem>({
        id: rule?.id ?? Date.now(),
        name: rule?.name ?? 'New Rule',
        priority: rule?.priority ?? 1,
        is_enabled: rule?.is_enabled ?? true,
        action: rule?.action ?? 'Confirm by request price',
        action_type: rule?.action_type ?? (rule?.action?.includes('dealer') ? 'Process to dealers' : 'Confirm by request price'),
        delay_ms: rule?.delay_ms ?? 0,
        delay_ticks: rule?.delay_ticks ?? 0,
        reject_reason: rule?.reject_reason ?? '',
        skip_if_no_dealers: rule?.skip_if_no_dealers ?? (rule?.action?.includes('skip') ?? true),
        request_type: rule?.request_type ?? 'All',
        order_type: rule?.order_type ?? 'All',
        conditions: rule?.conditions ? [...rule.conditions] : [{ type: 'Group', condition: 'Equal (=)', value: '*' }],
        dealers: rule?.dealers ? [...rule.dealers] : [{ login: '1000', name: 'First Admin' }],
    });

    // Condition sub-modal
    const [selectedCondIndex, setSelectedCondIndex] = React.useState<number | null>(0);
    const [condModalOpen, setCondModalOpen] = React.useState(false);
    const [editingCond, setEditingCond] = React.useState<RuleCondition | null>(null);

    // Dealer sub-modal
    const [selectedDealerIndex, setSelectedDealerIndex] = React.useState<number | null>(0);
    const [dealerModalOpen, setDealerModalOpen] = React.useState(false);
    const [editingDealer, setEditingDealer] = React.useState<RuleDealer | null>(null);

    const handleSave = () => {
        // Construct display action text matching MT5
        let displayAction = draft.action_type || draft.action;
        if (draft.action_type === 'Process to dealers' && draft.skip_if_no_dealers) {
            displayAction = 'Process to dealers, skip if no dealers online';
        } else if (draft.action_type === 'Delay in milliseconds') {
            displayAction = `Delay for ${draft.delay_ms ?? 0} milliseconds`;
        } else if (draft.action_type === 'Delay in ticks') {
            displayAction = `Delay for ${draft.delay_ticks ?? 1} ticks`;
        } else if (draft.action_type === 'Reject' && draft.reject_reason) {
            displayAction = `Reject (${draft.reject_reason})`;
        }

        onSave({
            ...draft,
            action: displayAction,
        });
        onClose();
    };

    // Dealers reordering
    const moveDealer = (up: boolean) => {
        if (selectedDealerIndex === null) return;
        const dealers = [...(draft.dealers ?? [])];
        const target = up ? selectedDealerIndex - 1 : selectedDealerIndex + 1;
        if (target < 0 || target >= dealers.length) return;
        const tmp = dealers[selectedDealerIndex];
        dealers[selectedDealerIndex] = dealers[target];
        dealers[target] = tmp;
        setDraft({ ...draft, dealers });
        setSelectedDealerIndex(target);
    };

    return (
        <FloatingWindow width={590} height={490} onClose={onClose}>
            <div className="adm-modal" style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column', background: 'var(--theia-editor-background)', color: 'var(--theia-foreground)', fontSize: 11, overflow: 'hidden' }}>
                
                {/* ── Title Bar (draggable) ─────────────────────────────── */}
                <div
                    className="adm-modal-header"
                    style={{
                        padding: '6px 12px',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        fontWeight: 600,
                        borderBottom: '1px solid var(--theia-border)',
                        background: 'var(--theia-sideBarSectionHeader-background)',
                        cursor: 'move',
                        userSelect: 'none'
                    }}
                >
                    <span>Routing: {draft.name || (isNew ? 'New Rule' : 'Rule')}</span>
                    <button
                        type="button"
                        onClick={onClose}
                        style={{ background: 'none', border: 'none', color: 'var(--theia-foreground)', cursor: 'pointer', opacity: 0.7 }}
                    >
                        ✕
                    </button>
                </div>

                {/* ── Tab Bar ───────────────────────────────────────────── */}
                <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    borderBottom: '1px solid var(--theia-border)',
                    background: 'var(--theia-editorGroupHeader-tabsBackground)',
                    padding: '0 8px',
                    flexShrink: 0
                }}>
                    {(['Common', 'Dealers'] as const).map((t) => {
                        const isActive = activeTab === t;
                        return (
                            <button
                                key={t}
                                type="button"
                                onClick={() => setActiveTab(t)}
                                style={{
                                    background: isActive ? 'var(--theia-editor-background)' : 'transparent',
                                    border: 'none',
                                    borderBottom: isActive ? '2px solid var(--theia-focusBorder)' : '2px solid transparent',
                                    color: isActive ? 'var(--theia-foreground)' : 'var(--theia-descriptionForeground)',
                                    padding: '6px 14px',
                                    fontSize: 11,
                                    cursor: 'pointer',
                                    fontWeight: isActive ? 600 : 400,
                                    outline: 'none',
                                    borderTopLeftRadius: 3,
                                    borderTopRightRadius: 3
                                }}
                            >
                                {t}
                            </button>
                        );
                    })}
                </div>

                {/* ── Tab Body Content ──────────────────────────────────── */}
                <div style={{ flex: 1, minHeight: 0, overflowY: 'auto', padding: '14px 18px', display: 'flex', flexDirection: 'column' }}>

                    {/* ════ TAB 1: COMMON ═════════════════════════════════ */}
                    {activeTab === 'Common' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            
                            {/* Blue Circular Routing Icon & Header Notice */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14, marginBottom: 4 }}>
                                <svg width="44" height="44" viewBox="0 0 48 48" style={{ flexShrink: 0 }}>
                                    <circle cx="24" cy="24" r="22" fill="#0078d4" />
                                    {/* 4 Inward/Outward crossing arrows */}
                                    <path d="M14 14 L21 21 M21 16 L21 21 L16 21" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                    <path d="M34 34 L27 27 M27 32 L27 27 L32 27" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                    <path d="M34 14 L27 21 M32 21 L27 21 L27 16" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                    <path d="M14 34 L21 27 M16 27 L21 27 L21 32" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                </svg>
                                <div style={{ fontSize: 11, lineHeight: 1.45, opacity: 0.9 }}>
                                    Using routing rules, one can adjust processing of trade requests by different conditions. Please specify conditions, for which the rule will be applied.
                                </div>
                            </div>

                            {/* Enable Checkbox */}
                            <div style={{ paddingLeft: 125, margin: '2px 0' }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.is_enabled}
                                        onChange={(e) => setDraft({ ...draft, is_enabled: e.target.checked })}
                                    />
                                    <span>Enable this rule</span>
                                </label>
                            </div>

                            {/* Name */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                <span style={{ width: 115, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Name:</span>
                                <input
                                    className="adm-input"
                                    style={{ width: 230, height: 22, fontSize: 11 }}
                                    value={draft.name}
                                    onChange={(e) => setDraft({ ...draft, name: e.target.value })}
                                />
                            </div>

                            {/* Perform Action */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                <span style={{ width: 115, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Perform action:</span>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <select
                                        className="adm-select"
                                        style={{ width: 230, height: 22, fontSize: 11 }}
                                        value={draft.action_type || draft.action}
                                        onChange={(e) => setDraft({ ...draft, action_type: e.target.value })}
                                    >
                                        {MT5_ACTIONS.map(a => (
                                            <option key={a} value={a}>{a}</option>
                                        ))}
                                    </select>

                                    {/* Action Sub-options */}
                                    {draft.action_type === 'Process to dealers' && (
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 4, cursor: 'pointer', fontSize: 10.5 }}>
                                            <input
                                                type="checkbox"
                                                checked={draft.skip_if_no_dealers}
                                                onChange={(e) => setDraft({ ...draft, skip_if_no_dealers: e.target.checked })}
                                            />
                                            <span>skip if no dealers online</span>
                                        </label>
                                    )}

                                    {draft.action_type === 'Delay in milliseconds' && (
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                            <input
                                                className="adm-input"
                                                type="number"
                                                style={{ width: 65, height: 22, fontSize: 11 }}
                                                value={draft.delay_ms ?? 0}
                                                onChange={(e) => setDraft({ ...draft, delay_ms: Number(e.target.value) })}
                                            />
                                            <span>ms</span>
                                        </div>
                                    )}

                                    {draft.action_type === 'Delay in ticks' && (
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                            <input
                                                className="adm-input"
                                                type="number"
                                                style={{ width: 55, height: 22, fontSize: 11 }}
                                                value={draft.delay_ticks ?? 1}
                                                onChange={(e) => setDraft({ ...draft, delay_ticks: Number(e.target.value) })}
                                            />
                                            <span>ticks (max 60)</span>
                                        </div>
                                    )}

                                    {draft.action_type === 'Reject' && (
                                        <input
                                            className="adm-input"
                                            placeholder="Reason (max 31 chars)"
                                            maxLength={31}
                                            style={{ flex: 1, height: 22, fontSize: 11 }}
                                            value={draft.reject_reason ?? ''}
                                            onChange={(e) => setDraft({ ...draft, reject_reason: e.target.value })}
                                        />
                                    )}
                                </div>
                            </div>

                            {/* Where Request Is */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                <span style={{ width: 115, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Where request is:</span>
                                <select
                                    className="adm-select"
                                    style={{ flex: 1, height: 22, fontSize: 11 }}
                                    value={draft.request_type}
                                    onChange={(e) => setDraft({ ...draft, request_type: e.target.value })}
                                >
                                    {REQUEST_TYPES.map(r => (
                                        <option key={r} value={r}>{r}</option>
                                    ))}
                                </select>
                            </div>

                            {/* Where Order Is */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                <span style={{ width: 115, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Where order is:</span>
                                <select
                                    className="adm-select"
                                    style={{ flex: 1, height: 22, fontSize: 11 }}
                                    value={draft.order_type}
                                    onChange={(e) => setDraft({ ...draft, order_type: e.target.value })}
                                >
                                    {ORDER_TYPES.map(o => (
                                        <option key={o} value={o}>{o}</option>
                                    ))}
                                </select>
                            </div>

                            {/* Where Conditions Are */}
                            <div style={{ display: 'flex', gap: 10, marginTop: 4 }}>
                                <span style={{ width: 115, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap', paddingTop: 4 }}>
                                    Where conditions are:
                                </span>

                                <div style={{ display: 'flex', gap: 8, flex: 1 }}>
                                    {/* Action Buttons Left */}
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 5, width: 75 }}>
                                        <button
                                            type="button"
                                            className="wb-btn secondary"
                                            style={{ height: 22, fontSize: 11 }}
                                            onClick={() => {
                                                setEditingCond(null);
                                                setCondModalOpen(true);
                                            }}
                                        >
                                            Add
                                        </button>
                                        <button
                                            type="button"
                                            className="wb-btn secondary"
                                            style={{ height: 22, fontSize: 11 }}
                                            disabled={selectedCondIndex === null || !draft.conditions?.length}
                                            onClick={() => {
                                                if (selectedCondIndex !== null && draft.conditions?.[selectedCondIndex]) {
                                                    setEditingCond(draft.conditions[selectedCondIndex]);
                                                    setCondModalOpen(true);
                                                }
                                            }}
                                        >
                                            Edit
                                        </button>
                                        <button
                                            type="button"
                                            className="wb-btn secondary"
                                            style={{ height: 22, fontSize: 11 }}
                                            disabled={selectedCondIndex === null || !draft.conditions?.length}
                                            onClick={() => {
                                                if (selectedCondIndex !== null) {
                                                    const updated = (draft.conditions ?? []).filter((_, i) => i !== selectedCondIndex);
                                                    setDraft({ ...draft, conditions: updated });
                                                    setSelectedCondIndex(updated.length ? 0 : null);
                                                }
                                            }}
                                        >
                                            Delete
                                        </button>
                                    </div>

                                    {/* Conditions Table Right */}
                                    <div style={{ flex: 1, border: '1px solid var(--theia-border)', borderRadius: 2, height: 130, overflowY: 'auto' }}>
                                        <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                            <thead>
                                                <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                                                    <th style={{ padding: '3px 6px', borderRight: '1px solid var(--theia-border)' }}>Type</th>
                                                    <th style={{ padding: '3px 6px', borderRight: '1px solid var(--theia-border)' }}>Condition</th>
                                                    <th style={{ padding: '3px 6px' }}>Value</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {(draft.conditions ?? []).map((c, idx) => (
                                                    <tr
                                                        key={idx}
                                                        onClick={() => setSelectedCondIndex(idx)}
                                                        onDoubleClick={() => {
                                                            setSelectedCondIndex(idx);
                                                            setEditingCond(c);
                                                            setCondModalOpen(true);
                                                        }}
                                                        style={{
                                                            background: selectedCondIndex === idx ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                            color: selectedCondIndex === idx ? 'var(--theia-list-activeSelectionForeground)' : 'inherit',
                                                            cursor: 'pointer'
                                                        }}
                                                    >
                                                        <td style={{ padding: '3px 6px', borderRight: '1px solid var(--theia-border)' }}>
                                                            <span style={{ color: '#4fc1ff', marginRight: 4, fontSize: 10 }}>ab</span> {c.type}
                                                        </td>
                                                        <td style={{ padding: '3px 6px', borderRight: '1px solid var(--theia-border)' }}>{c.condition}</td>
                                                        <td style={{ padding: '3px 6px' }}>{c.value}</td>
                                                    </tr>
                                                ))}
                                                {(!draft.conditions || draft.conditions.length === 0) && (
                                                    <tr>
                                                        <td colSpan={3} style={{ padding: '16px', textAlign: 'center', opacity: 0.6 }}>
                                                            No specific conditions set (applies to all)
                                                        </td>
                                                    </tr>
                                                )}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                        </div>
                    )}

                    {/* ════ TAB 2: DEALERS ════════════════════════════════ */}
                    {activeTab === 'Dealers' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                            
                            {/* Blue Circular Routing Icon & Header Notice */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <svg width="44" height="44" viewBox="0 0 48 48" style={{ flexShrink: 0 }}>
                                    <circle cx="24" cy="24" r="22" fill="#0078d4" />
                                    <path d="M14 14 L21 21 M21 16 L21 21 L16 21" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                    <path d="M34 34 L27 27 M27 32 L27 27 L32 27" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                    <path d="M34 14 L27 21 M32 21 L27 21 L27 16" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                    <path d="M14 34 L21 27 M16 27 L21 27 L21 32" stroke="#ffffff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                                </svg>
                                <div style={{ fontSize: 11, lineHeight: 1.45, opacity: 0.9 }}>
                                    Please specify dealers who will process requests that meet the rule conditions.
                                </div>
                            </div>

                            {/* Dealers Table with Left Toolbar */}
                            <div style={{ display: 'flex', gap: 12, marginTop: 4 }}>
                                
                                {/* Left Toolbar: Up, Down, Add, Edit, Delete */}
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, width: 75 }}>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedDealerIndex === null || selectedDealerIndex === 0}
                                        onClick={() => moveDealer(true)}
                                    >
                                        Up
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedDealerIndex === null || selectedDealerIndex === (draft.dealers?.length ?? 1) - 1}
                                        onClick={() => moveDealer(false)}
                                    >
                                        Down
                                    </button>

                                    <div style={{ height: 18 }} />

                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() => {
                                            setEditingDealer(null);
                                            setDealerModalOpen(true);
                                        }}
                                    >
                                        Add
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedDealerIndex === null || !draft.dealers?.length}
                                        onClick={() => {
                                            if (selectedDealerIndex !== null && draft.dealers?.[selectedDealerIndex]) {
                                                setEditingDealer(draft.dealers[selectedDealerIndex]);
                                                setDealerModalOpen(true);
                                            }
                                        }}
                                    >
                                        Edit
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedDealerIndex === null || !draft.dealers?.length}
                                        onClick={() => {
                                            if (selectedDealerIndex !== null) {
                                                const updated = (draft.dealers ?? []).filter((_, i) => i !== selectedDealerIndex);
                                                setDraft({ ...draft, dealers: updated });
                                                setSelectedDealerIndex(updated.length ? 0 : null);
                                            }
                                        }}
                                    >
                                        Delete
                                    </button>
                                </div>

                                {/* Right Dealers Table */}
                                <div style={{ flex: 1, border: '1px solid var(--theia-border)', borderRadius: 2, height: 220, overflowY: 'auto' }}>
                                    <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                        <thead>
                                            <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                                                <th style={{ padding: '4px 8px', width: 140, borderRight: '1px solid var(--theia-border)' }}>Login</th>
                                                <th style={{ padding: '4px 8px' }}>Name</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {(draft.dealers ?? []).map((d, idx) => (
                                                <tr
                                                    key={idx}
                                                    onClick={() => setSelectedDealerIndex(idx)}
                                                    onDoubleClick={() => {
                                                        setSelectedDealerIndex(idx);
                                                        setEditingDealer(d);
                                                        setDealerModalOpen(true);
                                                    }}
                                                    style={{
                                                        background: selectedDealerIndex === idx ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                        color: selectedDealerIndex === idx ? 'var(--theia-list-activeSelectionForeground)' : 'inherit',
                                                        cursor: 'pointer'
                                                    }}
                                                >
                                                    <td style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>
                                                        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                                            {/* Blue dealer/manager icon */}
                                                            <svg width="13" height="13" viewBox="0 0 16 16" fill="#0078d4" style={{ flexShrink: 0 }}>
                                                                <path d="M8 8a3 3 0 100-6 3 3 0 000 6zm-5 7a5 5 0 0110 0H3z" />
                                                            </svg>
                                                            <span>{d.login}</span>
                                                        </div>
                                                    </td>
                                                    <td style={{ padding: '4px 8px' }}>{d.name}</td>
                                                </tr>
                                            ))}
                                            {(!draft.dealers || draft.dealers.length === 0) && (
                                                <tr>
                                                    <td colSpan={2} style={{ padding: '24px', textAlign: 'center', opacity: 0.6 }}>
                                                        No dealers or gateways assigned to this rule
                                                    </td>
                                                </tr>
                                            )}
                                        </tbody>
                                    </table>
                                </div>

                            </div>
                        </div>
                    )}

                </div>

                {/* ── Modal Footer Bar ──────────────────────────────────── */}
                <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'flex-end',
                    gap: 8,
                    padding: '8px 14px',
                    borderTop: '1px solid var(--theia-border)',
                    background: 'var(--theia-sideBarSectionHeader-background)',
                    flexShrink: 0
                }}>
                    <button
                        type="button"
                        className="wb-btn"
                        style={{ height: 23, minWidth: 65, fontSize: 11 }}
                        onClick={handleSave}
                    >
                        OK
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 23, minWidth: 65, fontSize: 11 }}
                        onClick={onClose}
                    >
                        Cancel
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 23, minWidth: 60, fontSize: 11 }}
                        onClick={() => alert('MetaTrader 5 Order Routing Rules.\nConfigure actions and conditions to process client requests, or route orders to dealers/gateways.')}
                    >
                        Help
                    </button>
                </div>

                {/* Condition Sub-modal */}
                {condModalOpen && (
                    <ConditionModal
                        initial={editingCond}
                        onClose={() => setCondModalOpen(false)}
                        onSave={(saved) => {
                            if (editingCond && selectedCondIndex !== null) {
                                const updated = [...(draft.conditions ?? [])];
                                updated[selectedCondIndex] = saved;
                                setDraft({ ...draft, conditions: updated });
                            } else {
                                setDraft({ ...draft, conditions: [...(draft.conditions ?? []), saved] });
                                setSelectedCondIndex((draft.conditions ?? []).length);
                            }
                        }}
                    />
                )}

                {/* Dealer Sub-modal */}
                {dealerModalOpen && (
                    <DealerPickerModal
                        initial={editingDealer}
                        onClose={() => setDealerModalOpen(false)}
                        onSave={(saved) => {
                            if (editingDealer && selectedDealerIndex !== null) {
                                const updated = [...(draft.dealers ?? [])];
                                updated[selectedDealerIndex] = saved;
                                setDraft({ ...draft, dealers: updated });
                            } else {
                                setDraft({ ...draft, dealers: [...(draft.dealers ?? []), saved] });
                                setSelectedDealerIndex((draft.dealers ?? []).length);
                            }
                        }}
                    />
                )}

            </div>
        </FloatingWindow>
    );
}
