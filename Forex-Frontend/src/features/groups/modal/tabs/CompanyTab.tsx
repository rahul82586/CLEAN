import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const COMPANIES = [
    'MetaQuotes Software Corp.',
    'Demo Brokerage Ltd.',
    'Global Clearing Inc.',
];

export function CompanyTab(): React.ReactElement {
    const { draft, setDraft, errors, setErrors } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));

        // Remove error if valid
        if (field === 'company' && val) {
            setErrors(prev => {
                const next = { ...prev };
                delete next.company;
                return next;
            });
        }
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
                    Please specify details of the group servicing company and the folder with mail and report templates.
                </div>
            </div>

            {/* Exact MT5 8 vertical full-width rows */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 7, maxWidth: 520 }}>
                {/* 1. Company */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Company:</span>
                    <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                        <select
                            className={`adm-select ${errors.company ? 'error' : ''}`}
                            style={{ height: 21, padding: '2px 6px', fontSize: 11 }}
                            value={draft.company}
                            onChange={e => updateField('company', e.target.value)}
                        >
                            <option value="">Select Company...</option>
                            {COMPANIES.map(c => (
                                <option key={c} value={c}>{c}</option>
                            ))}
                        </select>
                        {errors.company && (
                            <span className="adm-input-error-text" style={{ fontSize: 9, color: 'var(--theia-errorForeground)' }}>
                                {errors.company}
                            </span>
                        )}
                    </div>
                </div>

                {/* 2. Company site */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Company site:</span>
                    <input
                        className="adm-input"
                        type="url"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="https://www.company.com"
                        value={draft.company_website}
                        onChange={e => updateField('company_website', e.target.value)}
                    />
                </div>

                {/* 3. Company email */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Company email:</span>
                    <input
                        className="adm-input"
                        type="email"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="info@company.com"
                        value={draft.company_email}
                        onChange={e => updateField('company_email', e.target.value)}
                    />
                </div>

                {/* 4. Deposit site */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Deposit site:</span>
                    <input
                        className="adm-input"
                        type="url"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="https://client.company.com/deposit"
                        value={draft.deposit_url}
                        onChange={e => updateField('deposit_url', e.target.value)}
                    />
                </div>

                {/* 5. Withdrawal site */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Withdrawal site:</span>
                    <input
                        className="adm-input"
                        type="url"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="https://client.company.com/withdraw"
                        value={draft.withdrawal_url}
                        onChange={e => updateField('withdrawal_url', e.target.value)}
                    />
                </div>

                {/* 6. Support site */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Support site:</span>
                    <input
                        className="adm-input"
                        type="url"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="https://support.company.com"
                        value={draft.support_site}
                        onChange={e => updateField('support_site', e.target.value)}
                    />
                </div>

                {/* 7. Support email */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Support email:</span>
                    <input
                        className="adm-input"
                        type="email"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="support@company.com"
                        value={draft.support_email}
                        onChange={e => updateField('support_email', e.target.value)}
                    />
                </div>

                {/* 8. Templates folder */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Templates folder:</span>
                    <input
                        className="adm-input"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="standard_templates"
                        value={draft.templates_folder}
                        onChange={e => updateField('templates_folder', e.target.value)}
                    />
                </div>
            </div>
        </div>
    );
}

