import * as React from 'react';
import { FloatingWindow } from '../../shared/FloatingWindow';

export interface RuleDealer {
    login: string | number;
    name: string;
}

interface DealerPickerModalProps {
    initial?: RuleDealer | null;
    onSave: (dealer: RuleDealer) => void;
    onClose: () => void;
}

const PRESET_DEALERS: RuleDealer[] = [
    { login: 1000, name: 'First Admin' },
    { login: 1001, name: 'Dealer Desk 1' },
    { login: 1002, name: 'Senior Dealer' },
    { login: 'ECN', name: 'ECN Order Matching' },
    { login: '1', name: 'MetaTrader 5 Gateway clone (1)' },
    { login: '2', name: 'FT MT5 Gateway (2)' },
    { login: '3', name: 'MetaTrader 5 Gateway clone (3)' },
    { login: 'LP-1', name: 'LP-Centroid-Primary' },
    { login: 'LP-2', name: 'LP-Backup-Bridge' },
];

export function DealerPickerModal({ initial, onSave, onClose }: DealerPickerModalProps): React.ReactElement {
    const [login, setLogin] = React.useState<string>(initial ? String(initial.login) : '1000');
    const [name, setName] = React.useState<string>(initial ? initial.name : 'First Admin');

    const handleSelectPreset = (d: RuleDealer) => {
        setLogin(String(d.login));
        setName(d.name);
    };

    const handleOk = () => {
        onSave({ login, name: name.trim() || `Dealer ${login}` });
        onClose();
    };

    return (
        <FloatingWindow width={420} height={260} onClose={onClose}>
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
                    <span>{initial ? 'Edit Dealer / Gateway' : 'Add Dealer / Gateway'}</span>
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
                        <span style={{ width: 85, textAlign: 'right', opacity: 0.85 }}>Select Preset:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 23, fontSize: 11 }}
                            onChange={(e) => {
                                const found = PRESET_DEALERS.find(p => String(p.login) === e.target.value);
                                if (found) handleSelectPreset(found);
                            }}
                            value={login}
                        >
                            <optgroup label="Dealers & Managers">
                                <option value="1000">1000 — First Admin</option>
                                <option value="1001">1001 — Dealer Desk 1</option>
                                <option value="1002">1002 — Senior Dealer</option>
                            </optgroup>
                            <optgroup label="Gateways & Bridges">
                                <option value="1">1 — MetaTrader 5 Gateway clone (1)</option>
                                <option value="2">2 — FT MT5 Gateway (2)</option>
                                <option value="3">3 — MetaTrader 5 Gateway clone (3)</option>
                                <option value="LP-1">LP-1 — LP-Centroid-Primary</option>
                                <option value="LP-2">LP-2 — LP-Backup-Bridge</option>
                            </optgroup>
                            <optgroup label="Execution Engines">
                                <option value="ECN">ECN — ECN Order Matching</option>
                            </optgroup>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                        <span style={{ width: 85, textAlign: 'right', opacity: 0.85 }}>Login / ID:</span>
                        <input
                            className="adm-input"
                            style={{ flex: 1, height: 23, fontSize: 11 }}
                            value={login}
                            onChange={(e) => setLogin(e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                        <span style={{ width: 85, textAlign: 'right', opacity: 0.85 }}>Dealer Name:</span>
                        <input
                            className="adm-input"
                            style={{ flex: 1, height: 23, fontSize: 11 }}
                            value={name}
                            onChange={(e) => setName(e.target.value)}
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
