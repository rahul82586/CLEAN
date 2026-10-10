import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const LANG_OPTIONS = [
    'English (United States)',
    'German (Germany)',
    'Chinese (Simplified)',
    'Russian (Russia)',
    'Spanish (Spain)',
    'French (France)',
    'Arabic (Saudi Arabia)',
    'Japanese (Japan)',
    'Portuguese (Brazil)',
    'Italian (Italy)',
];

export function NewsMailTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();
    const [isLangDialogOpen, setIsLangDialogOpen] = React.useState(false);

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const toggleLanguage = (lang: string) => {
        const next = draft.news_languages.includes(lang)
            ? draft.news_languages.filter(l => l !== lang)
            : [...draft.news_languages, lang];
        updateField('news_languages', next);
    };

    const langDisplayString = React.useMemo(() => {
        if (!draft.news_languages || draft.news_languages.length === 0) {
            return 'All languages';
        }
        return draft.news_languages.join(', ');
    }, [draft.news_languages]);

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
                    Please specify the settings of news received by the group and the possibility of using the mail system.
                </div>
            </div>

            {/* MT5 News and Mails Fields */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 7, maxWidth: 520 }}>
                {/* 1. News */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>News:</span>
                    <select
                        className="adm-select"
                        style={{ width: 160, height: 21, padding: '2px 6px', fontSize: 11 }}
                        value={draft.news_mode}
                        onChange={e => updateField('news_mode', e.target.value)}
                    >
                        <option value="full">Full package</option>
                        <option value="headers">Headers only</option>
                        <option value="none">None</option>
                    </select>
                </div>

                {/* 2. News categories */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>News categories:</span>
                    <input
                        className="adm-input"
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                        placeholder="e.g. Forex, Stocks\US"
                        value={draft.news_categories}
                        onChange={e => updateField('news_categories', e.target.value)}
                    />
                </div>

                {/* 3. News languages */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ width: 140, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>News languages:</span>
                    <input
                        className="adm-input"
                        readOnly
                        style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11, cursor: 'pointer', background: 'var(--theia-input-background)' }}
                        value={langDisplayString}
                        onClick={() => setIsLangDialogOpen(true)}
                    />
                    <button
                        type="button"
                        className="adm-button"
                        style={{ height: 21, padding: '0 10px', fontSize: 11, whiteSpace: 'nowrap' }}
                        onClick={() => setIsLangDialogOpen(prev => !prev)}
                    >
                        Change...
                    </button>
                </div>

                {/* 4. Enable internal mail system checkbox */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4, paddingLeft: 148 }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                        <input
                            type="checkbox"
                            checked={draft.enable_internal_mail}
                            onChange={e => updateField('enable_internal_mail', e.target.checked)}
                        />
                        <span>Enable internal mail system</span>
                    </label>
                </div>
            </div>

            {/* Language Selection Modal / Dropdown */}
            {isLangDialogOpen && (
                <div style={{
                    marginTop: 10,
                    marginLeft: 148,
                    maxWidth: 360,
                    padding: 10,
                    background: 'var(--theia-editor-background)',
                    border: '1px solid var(--theia-focusBorder)',
                    borderRadius: 4,
                    boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
                    zIndex: 20
                }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8, fontWeight: 'bold' }}>
                        <span>Select News Languages</span>
                        <button
                            type="button"
                            className="adm-button"
                            style={{ height: 18, padding: '0 6px', fontSize: 10 }}
                            onClick={() => setIsLangDialogOpen(false)}
                        >
                            ✕
                        </button>
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 6, maxHeight: 180, overflowY: 'auto' }}>
                        {LANG_OPTIONS.map(lang => (
                            <label key={lang} style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', fontSize: 11 }}>
                                <input
                                    type="checkbox"
                                    checked={draft.news_languages.includes(lang)}
                                    onChange={() => toggleLanguage(lang)}
                                />
                                <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{lang}</span>
                            </label>
                        ))}
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 6, marginTop: 8 }}>
                        <button
                            type="button"
                            className="adm-button"
                            style={{ height: 20, padding: '0 8px', fontSize: 10 }}
                            onClick={() => updateField('news_languages', [])}
                        >
                            Select All
                        </button>
                        <button
                            type="button"
                            className="adm-button adm-button-primary"
                            style={{ height: 20, padding: '0 8px', fontSize: 10 }}
                            onClick={() => setIsLangDialogOpen(false)}
                        >
                            Done
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}

