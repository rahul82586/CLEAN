import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const MAIL_SERVERS = ['(Default)', 'Internal Mailer', 'Local-Postfix', 'AWS-SES', 'SendGrid-SMTP'];

export function ReportsTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const isDailyDataEnabled = draft.report_generation !== 'off';

    const handleDailyDataToggle = (checked: boolean) => {
        updateField('report_generation', checked ? 'daily' : 'off');
        if (!checked) {
            updateField('generate_statements', false);
            updateField('send_statements_email', false);
            updateField('send_copies_support', false);
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
                    The platform can daily save the end-of-day state of accounts to a special database. That data is used for generating daily statements and various reports for managers.
                </div>
            </div>

            {/* MT5 Reports Checkbox Tree and Fields */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8, paddingLeft: 40, maxWidth: 520 }}>
                {/* 1. Generate daily data */}
                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer', fontWeight: 600 }}>
                    <input
                        type="checkbox"
                        checked={isDailyDataEnabled}
                        onChange={e => handleDailyDataToggle(e.target.checked)}
                    />
                    <span>Generate daily data</span>
                </label>

                {/* Indented statements checkboxes */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 7, paddingLeft: 24, opacity: isDailyDataEnabled ? 1 : 0.6 }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                        <input
                            type="checkbox"
                            disabled={!isDailyDataEnabled}
                            checked={isDailyDataEnabled && draft.generate_statements}
                            onChange={e => updateField('generate_statements', e.target.checked)}
                        />
                        <span>Generate daily statements for clients</span>
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer', opacity: isDailyDataEnabled && draft.generate_statements ? 1 : 0.6 }}>
                        <input
                            type="checkbox"
                            disabled={!isDailyDataEnabled || !draft.generate_statements}
                            checked={isDailyDataEnabled && draft.generate_statements && draft.send_statements_email}
                            onChange={e => updateField('send_statements_email', e.target.checked)}
                        />
                        <span>Send daily statements by email</span>
                    </label>
                </div>

                {/* Mail Server row */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 12, opacity: isDailyDataEnabled && draft.send_statements_email ? 1 : 0.6 }}>
                    <span style={{ width: 100, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Mail server:</span>
                    <select
                        className="adm-select"
                        style={{ width: 220, height: 21, padding: '2px 6px', fontSize: 11 }}
                        disabled={!isDailyDataEnabled || !draft.send_statements_email}
                        value={draft.mail_server || '(Default)'}
                        onChange={e => updateField('mail_server', e.target.value)}
                    >
                        {MAIL_SERVERS.map(m => (
                            <option key={m} value={m}>{m}</option>
                        ))}
                    </select>
                </div>

                {/* Indented Send copies to support email */}
                <div style={{ paddingLeft: 108, opacity: isDailyDataEnabled && draft.send_statements_email ? 1 : 0.6 }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                        <input
                            type="checkbox"
                            disabled={!isDailyDataEnabled || !draft.send_statements_email}
                            checked={isDailyDataEnabled && draft.send_statements_email && draft.send_copies_support}
                            onChange={e => updateField('send_copies_support', e.target.checked)}
                        />
                        <span>Send copies to support email</span>
                    </label>

                    {draft.send_copies_support && draft.support_email && (
                        <div style={{ fontSize: 10, opacity: 0.75, paddingLeft: 22, marginTop: 2 }}>
                            (to: {draft.support_email})
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
