import * as React from 'react';
import { FloatingWindow } from '../../shared/FloatingWindow';

export interface RuleCondition {
    type: string;
    condition: string;
    value: string;
}

interface ConditionModalProps {
    initial?: RuleCondition | null;
    onSave: (condition: RuleCondition) => void;
    onClose: () => void;
}

const CONDITION_TYPES = [
    // Account
    { category: 'Account', value: 'Group', label: 'Group' },
    { category: 'Account', value: 'Login', label: 'Login' },
    { category: 'Account', value: 'Country', label: 'Country' },
    { category: 'Account', value: 'City', label: 'City' },
    { category: 'Account', value: 'ZIP code', label: 'ZIP code' },
    { category: 'Account', value: 'Color', label: 'Color' },
    { category: 'Account', value: 'Leverage', label: 'Leverage' },
    { category: 'Account', value: 'Comment', label: 'Comment' },
    { category: 'Account', value: 'Status', label: 'Status' },
    { category: 'Account', value: 'Margin', label: 'Margin' },
    { category: 'Account', value: 'Margin level', label: 'Margin level' },
    { category: 'Account', value: 'Free margin', label: 'Free margin' },
    { category: 'Account', value: 'Equity', label: 'Equity' },
    { category: 'Account', value: 'Balance', label: 'Balance' },
    { category: 'Account', value: 'Client ID', label: 'Client ID' },

    // Request
    { category: 'Request', value: 'Symbols', label: 'Symbols' },
    { category: 'Request', value: 'Request volume', label: 'Request volume' },
    { category: 'Request', value: 'Deviation from market (points)', label: 'Deviation from market (points)' },
    { category: 'Request', value: 'Deviation from market (spreads)', label: 'Deviation from market (spreads)' },
    { category: 'Request', value: 'Request price', label: 'Request price' },
    { category: 'Request', value: 'Value', label: 'Value' },
    { category: 'Request', value: 'Date and time', label: 'Date and time' },
    { category: 'Request', value: 'Time', label: 'Time' },
    { category: 'Request', value: 'Day of week', label: 'Day of week' },
    { category: 'Request', value: 'Request comment', label: 'Request comment' },
    { category: 'Request', value: 'Placed by expert', label: 'Placed by expert' },
    { category: 'Request', value: 'Placed by signal', label: 'Placed by signal' },
    { category: 'Request', value: 'Dealer processed request', label: 'Dealer processed request' },
    { category: 'Request', value: 'Dealer placed request', label: 'Dealer placed request' },

    // Position
    { category: 'Position', value: 'Position volume', label: 'Position volume' },
    { category: 'Position', value: 'Position profit', label: 'Position profit' },
    { category: 'Position', value: 'Position symbol', label: 'Position symbol' },
    { category: 'Position', value: 'Position type', label: 'Position type' },
];

const OPERATORS = [
    'Equal (=)',
    'Not equal (!=)',
    'Greater (>)',
    'Greater or equal (>=)',
    'Less (<)',
    'Less or equal (<=)',
];

export function ConditionModal({ initial, onSave, onClose }: ConditionModalProps): React.ReactElement {
    const [type, setType] = React.useState(initial?.type ?? 'Group');
    const [condition, setCondition] = React.useState(initial?.condition ?? 'Equal (=)');
    const [value, setValue] = React.useState(initial?.value ?? '*');

    const handleOk = () => {
        onSave({ type, condition, value: value.trim() || '*' });
        onClose();
    };

    return (
        <FloatingWindow width={400} height={230} onClose={onClose}>
            <div className="adm-modal" style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column', background: 'var(--theia-editor-background)', color: 'var(--theia-foreground)', fontSize: 11 }}>
                {/* Header */}
                <div
                    className="adm-modal-header"
                    style={{
                        padding: '6px 12px',
                        fontWeight: 600,
                        borderBottom: '1px solid var(--theia-border)',
                        background: 'var(--theia-sideBarSectionHeader-background)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        cursor: 'move',
                        userSelect: 'none'
                    }}
                >
                    <span>{initial ? 'Edit Condition' : 'Add Condition'}</span>
                    <button
                        type="button"
                        onClick={onClose}
                        style={{ background: 'none', border: 'none', color: 'var(--theia-foreground)', cursor: 'pointer', opacity: 0.7 }}
                    >
                        ✕
                    </button>
                </div>

                {/* Body */}
                <div style={{ flex: 1, padding: '16px 20px', display: 'flex', flexDirection: 'column', gap: 10 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                        <span style={{ width: 70, textAlign: 'right', opacity: 0.85 }}>Type:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 23, fontSize: 11 }}
                            value={type}
                            onChange={(e) => setType(e.target.value)}
                        >
                            {['Account', 'Request', 'Position'].map(cat => (
                                <optgroup key={cat} label={cat}>
                                    {CONDITION_TYPES.filter(t => t.category === cat).map(t => (
                                        <option key={t.value} value={t.value}>{t.label}</option>
                                    ))}
                                </optgroup>
                            ))}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                        <span style={{ width: 70, textAlign: 'right', opacity: 0.85 }}>Condition:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 23, fontSize: 11 }}
                            value={condition}
                            onChange={(e) => setCondition(e.target.value)}
                        >
                            {OPERATORS.map(op => (
                                <option key={op} value={op}>{op}</option>
                            ))}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                        <span style={{ width: 70, textAlign: 'right', opacity: 0.85 }}>Value:</span>
                        <input
                            className="adm-input"
                            style={{ flex: 1, height: 23, fontSize: 11 }}
                            value={value}
                            onChange={(e) => setValue(e.target.value)}
                            placeholder="e.g. *, real\*, EURUSD*, 10"
                            autoFocus
                            onKeyDown={(e) => {
                                if (e.key === 'Enter') handleOk();
                                if (e.key === 'Escape') onClose();
                            }}
                        />
                    </div>
                </div>

                {/* Footer */}
                <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'flex-end',
                    gap: 8,
                    padding: '8px 12px',
                    borderTop: '1px solid var(--theia-border)',
                    background: 'var(--theia-sideBarSectionHeader-background)'
                }}>
                    <button type="button" className="wb-btn" style={{ minWidth: 65, height: 23, fontSize: 11 }} onClick={handleOk}>
                        OK
                    </button>
                    <button type="button" className="wb-btn secondary" style={{ minWidth: 65, height: 23, fontSize: 11 }} onClick={onClose}>
                        Cancel
                    </button>
                </div>
            </div>
        </FloatingWindow>
    );
}
