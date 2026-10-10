import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'AUD', 'CAD'];
const AUTH_METHODS = ['Normal', '1024-bit RSA SSL', '2048-bit RSA SSL', 'Custom SSL certificate'];
const SERVERS = ['Main Trade Server, 1', 'MetaQuotes-Demo', 'History-01', 'Access-01', 'Backup-01'];
const DIGIT_OPTIONS = [0, 1, 2, 3, 4, 5];
const PUSH_OPTIONS = ['None', 'All', 'Placed orders only', 'Deals only'];

export function CommonTab(): React.ReactElement {
    const { draft, setDraft, errors, setErrors } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));

        // Validation logic
        setErrors(prev => {
            const next = { ...prev };
            if (field === 'name') {
                if (!val) {
                    next.name = 'Group name is required';
                } else if (/[/:*?"<>|]/.test(val)) {
                    next.name = 'Group name cannot contain special characters like /, :, *, ?, ", <, >, |';
                } else {
                    delete next.name;
                }
            }
            return next;
        });
    };

    // Auto digit lock for standard currencies
    React.useEffect(() => {
        if (CURRENCIES.includes(draft.currency)) {
            updateField('digits', 2);
        }
    }, [draft.currency]);

    const isDemoGroup = draft.name.toLowerCase().includes('demo');

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
                    Group is a set of users that have the same permission settings and service conditions.
                    Please specify name of group, deposit currency, trade server, and authentication type.
                </div>
            </div>

            {/* Form Fields arranged exactly like MT5 */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 7 }}>
                {/* Row 1: Name and Currency */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: '1 1 280px' }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Name:</span>
                        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                            <input
                                className={`adm-input ${errors.name ? 'error' : ''}`}
                                style={{ height: 21, padding: '2px 6px', fontSize: 11 }}
                                placeholder="e.g. real\real"
                                value={draft.name}
                                onChange={e => updateField('name', e.target.value)}
                            />
                            {errors.name && (
                                <span className="adm-input-error-text" style={{ fontSize: 9, color: 'var(--theia-errorForeground)' }}>
                                    {errors.name}
                                </span>
                            )}
                        </div>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: 220 }}>
                        <span style={{ width: 60, textAlign: 'right', opacity: 0.85 }}>Currency:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={CURRENCIES.includes(draft.currency) ? draft.currency : 'other'}
                            onChange={e => {
                                const val = e.target.value;
                                if (val !== 'other') {
                                    updateField('currency', val);
                                }
                            }}
                        >
                            {CURRENCIES.map(c => (
                                <option key={c} value={c}>{c}</option>
                            ))}
                            <option value="other">Custom...</option>
                        </select>
                        {!CURRENCIES.includes(draft.currency) && (
                            <input
                                className="adm-input"
                                style={{ width: 55, height: 21, padding: '2px 6px', fontSize: 11 }}
                                placeholder="USD"
                                value={draft.currency}
                                onChange={e => updateField('currency', e.target.value.toUpperCase())}
                            />
                        )}
                    </div>
                </div>

                {/* Row 2: Trade Server and Digits */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: '1 1 280px' }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Trade server:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.trade_server}
                            onChange={e => updateField('trade_server', e.target.value)}
                        >
                            {SERVERS.map(s => (
                                <option key={s} value={s}>{s}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: 220 }}>
                        <span style={{ width: 60, textAlign: 'right', opacity: 0.85 }}>Digits:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.digits}
                            onChange={e => updateField('digits', parseInt(e.target.value) || 0)}
                        >
                            {DIGIT_OPTIONS.map(d => (
                                <option key={d} value={d}>{d}</option>
                            ))}
                        </select>
                    </div>
                </div>

                {/* Row 3: Authentication and Minimum Password Length */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: '1 1 280px' }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Authentication:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.authentication}
                            onChange={e => updateField('authentication', e.target.value)}
                        >
                            {AUTH_METHODS.map(a => (
                                <option key={a} value={a}>{a}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: 220 }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Minimum password length:</span>
                        <input
                            className="adm-input"
                            type="number"
                            min={5}
                            max={16}
                            style={{ width: 65, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.min_password_len}
                            onChange={e => updateField('min_password_len', Math.min(16, parseInt(e.target.value) || 8))}
                        />
                    </div>
                </div>

                {/* Row 4: One-time Password and Force Checkbox */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: '1 1 280px' }}>
                        <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>One-time password:</span>
                        <select
                            className="adm-select"
                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.otp_mode}
                            onChange={e => updateField('otp_mode', e.target.value)}
                        >
                            <option value="disabled">Disabled</option>
                            <option value="all">Required for all</option>
                            <option value="web">Required for Web Platform</option>
                        </select>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, width: 220 }}>
                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', whiteSpace: 'nowrap' }}>
                            <input
                                type="checkbox"
                                checked={draft.force_otp}
                                onChange={e => updateField('force_otp', e.target.checked)}
                            />
                            <span>Force one-time password usage</span>
                        </label>
                    </div>
                </div>

                {/* Row 5: Push Notifications */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Push notifications:</span>
                    <select
                        className="adm-select"
                        style={{ width: 180, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.push_placed_orders ? 'All' : 'None'}
                        onChange={e => {
                            const on = e.target.value !== 'None';
                            updateField('push_placed_orders', on);
                            updateField('push_performed_deals', on);
                        }}
                    >
                        {PUSH_OPTIONS.map(p => (
                            <option key={p} value={p}>{p}</option>
                        ))}
                    </select>
                    <span style={{ opacity: 0.8, fontSize: 11 }}>sent from the trade server</span>
                </div>
            </div>

            {/* MT5 Checkbox List below fields */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginTop: 6, paddingLeft: 148 }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                    <input
                        type="checkbox"
                        checked={draft.enable_connections}
                        onChange={e => updateField('enable_connections', e.target.checked)}
                    />
                    <span>Enable connections</span>
                </label>

                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                    <input
                        type="checkbox"
                        checked={draft.enable_cert_confirm}
                        onChange={e => updateField('enable_cert_confirm', e.target.checked)}
                    />
                    <span>Enable certificate confirmation</span>
                </label>

                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                    <input
                        type="checkbox"
                        checked={draft.change_pass_first_login}
                        onChange={e => updateField('change_pass_first_login', e.target.checked)}
                    />
                    <span>Change password at first login</span>
                </label>

                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer', opacity: isDemoGroup ? 0.6 : 1 }}>
                    <input
                        type="checkbox"
                        disabled={isDemoGroup}
                        checked={!isDemoGroup && draft.show_risk_warning}
                        onChange={e => updateField('show_risk_warning', e.target.checked)}
                    />
                    <span>Show the risk warning window after connection</span>
                </label>

                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                    <input
                        type="checkbox"
                        checked={draft.regulatory_restrictions}
                        onChange={e => updateField('regulatory_restrictions', e.target.checked)}
                    />
                    <span>Enforce country-specific regulatory restrictions for retail clients</span>
                </label>
            </div>
        </div>
    );
}
