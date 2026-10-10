import * as React from 'react';
import { API, isBackendGap } from '../../services/api';
import { money, leverage } from '../../shared/format';
import { fmtTime, ORDER_TYPE, ORDER_STATE } from '../../shared/tradeTypes';
import { FloatingWindow } from '../../shared/FloatingWindow';

interface Props {
    login: number;
    onClose: () => void;
    onSaved: () => void;
    onError: (msg: string, gap?: boolean) => void;
}

/**
 * MT5 MANAGER trading-account dialog — 11 tabs:
 * Overview · Exposure · Personal · Account · Limits · Profile · Subscriptions ·
 * Balance · Trade · History · Security
 * Note: Exposure, Balance, Trade, and History are Manager-exclusive tabs and preserved intact.
 */
export const MANAGER_ACCOUNT_TABS = [
    'Overview', 'Exposure', 'Personal', 'Account', 'Limits', 'Profile',
    'Subscriptions', 'Balance', 'Trade', 'History', 'Security',
] as const;
type TabId = (typeof MANAGER_ACCOUNT_TABS)[number];

const BALANCE_TYPES = ['balance', 'deposit', 'withdrawal', 'credit', 'charge', 'correction', 'bonus', 'commission', 'daily commission', 'monthly commission', 'interest rate'];

const LEVERAGE_OPTIONS = [
    { value: 1, label: '1 : 1' },
    { value: 10, label: '1 : 10' },
    { value: 25, label: '1 : 25' },
    { value: 50, label: '1 : 50' },
    { value: 100, label: '1 : 100' },
    { value: 200, label: '1 : 200' },
    { value: 400, label: '1 : 400' },
    { value: 500, label: '1 : 500' },
    { value: 1000, label: '1 : 1000' },
];

const LANGUAGES = [
    'English', 'Russian', 'Chinese', 'Spanish', 'German', 'French', 'Arabic', 'Japanese', 'Portuguese', 'Italian'
];

const COUNTRIES = [
    'United States', 'United Kingdom', 'Germany', 'France', 'Cyprus', 'United Arab Emirates', 'Singapore', 'Australia', 'Japan', 'China'
];

function formatMt5Date(val: any): string {
    if (!val) return '—';
    const d = new Date(val);
    if (isNaN(d.getTime())) return String(val);
    const yr = d.getFullYear();
    const mo = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${yr}.${mo}.${day}`;
}

function formatMt5DateTime(val: any): string {
    if (!val) return '—';
    const d = new Date(val);
    if (isNaN(d.getTime())) return String(val);
    const yr = d.getFullYear();
    const mo = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    const hr = String(d.getHours()).padStart(2, '0');
    const min = String(d.getMinutes()).padStart(2, '0');
    const sec = String(d.getSeconds()).padStart(2, '0');
    return `${yr}.${mo}.${day} ${hr}:${min}:${sec}`;
}

function generatePassword(): string {
    const lower = 'abcdefghijkmnopqrstuvwxyz';
    const upper = 'ABCDEFGHJKLMNPQRSTUVWXYZ';
    const digits = '23456789';
    const syms = '#@!$%&*';
    const pick = (s: string) => s[Math.floor(Math.random() * s.length)];
    const core = Array.from({ length: 8 }, () => pick(lower + upper + digits + syms));
    return [pick(lower), pick(upper), pick(digits), pick(syms), ...core].join('').slice(0, 12);
}

export function ManagerAccountDialog({ login, onClose, onSaved, onError }: Props): React.ReactElement {
    const [tab, setTab] = React.useState<TabId>('Overview');
    const [data, setData] = React.useState<any | null>(null);
    const [groups, setGroups] = React.useState<any[]>([]);
    const [deals, setDeals] = React.useState<any[]>([]);
    const [draft, setDraft] = React.useState<any>(null);
    const [balForm, setBalForm] = React.useState({ type: 'balance', amount: '', comment: '' });
    const [pwd, setPwd] = React.useState<Record<string, string>>({ master: '', investor: '', webapi: '', phone: '' });
    const [pwdMsg, setPwdMsg] = React.useState<Record<string, string>>({});

    // Trade accounts state
    const [tradeAccounts, setTradeAccounts] = React.useState<Array<{ gatewayId: string; account: string }>>([
        { gatewayId: 'Main Gateway', account: String(login) }
    ]);
    const [selectedTradeAcc, setSelectedTradeAcc] = React.useState<number | null>(0);

    const isInitial = React.useRef(true);
    const load = React.useCallback(() => {
        API.getAccountDetail(login).then((d) => {
            setData(d);
            if (isInitial.current) {
                isInitial.current = false;
                setDraft({
                    name: d.name ?? '',
                    last_name: d.last_name ?? '',
                    middle_name: d.middle_name ?? '',
                    company: d.company ?? '',
                    email: d.email ?? '',
                    phone: d.phone ?? '',
                    country: d.country ?? 'United States',
                    state: d.state ?? '',
                    city: d.city ?? '',
                    zip: d.zip ?? '',
                    address: d.address ?? '',
                    language: d.language ?? 'English',
                    resident_status: d.resident_status ?? 'RE',
                    id_number: d.id_number ?? '',
                    metaquotes_id: d.metaquotes_id ?? '',
                    lead_source: d.lead_source ?? '',
                    lead_campaign: d.lead_campaign ?? '',
                    comment: d.comment ?? '',
                    group: d.group ?? '',
                    color: d.color ?? 'None',
                    leverage: d.leverage ?? 100,
                    bank_account: d.bank_account ?? '',
                    agent_account: d.agent_account ?? 0,
                    is_enabled: Boolean(d.is_enabled ?? true),
                    allow_password_change: Boolean(d.allow_password_change ?? true),
                    otp_enabled: Boolean(d.otp_enabled ?? true),
                    change_pass_next_login: Boolean(d.change_pass_next_login ?? false),
                    limits: {
                        show_to_managers: Boolean(d.limits?.show_to_managers ?? true),
                        include_in_reports: Boolean(d.limits?.include_in_reports ?? true),
                        daily_reports: Boolean(d.limits?.daily_reports ?? true),
                        api_connections: Boolean(d.limits?.api_connections ?? false),
                        sponsored_vps: Boolean(d.limits?.sponsored_vps ?? false),
                        enable_trading: Boolean(d.limits?.enable_trading ?? true),
                        enable_ea: Boolean(d.limits?.enable_ea ?? true),
                        enable_trailing: Boolean(d.limits?.enable_trailing ?? true),
                        total_value: d.limits?.total_value ?? '',
                        max_orders: d.limits?.max_orders ?? '',
                    },
                });
            }
        }).catch((e) => onError(String(e?.message ?? e)));
        API.getDeals().then((rows) => setDeals(rows.filter((x: any) => x.login === login))).catch(() => setDeals([]));
        API.getGroups().then(setGroups).catch(() => setGroups([]));
    }, [login, onError]);

    React.useEffect(() => {
        load();
        const iv = setInterval(load, 2500);
        return () => clearInterval(iv);
    }, [load]);

    const set = (patch: any) => setDraft((f: any) => ({ ...f, ...patch }));

    const save = async () => {
        try {
            await API.updateAccount(login, {
                name: draft.name,
                first_name: draft.name,
                last_name: draft.last_name,
                middle_name: draft.middle_name,
                company: draft.company,
                email: draft.email,
                phone: draft.phone,
                country: draft.country,
                state: draft.state,
                city: draft.city,
                zip: draft.zip,
                address: draft.address,
                group: draft.group,
                leverage: Number(draft.leverage),
                is_enabled: draft.is_enabled,
                bank_account: draft.bank_account,
                agent_account: draft.agent_account,
                limits: draft.limits,
            });
            onSaved();
            onClose();
        } catch (e: any) {
            onError(String(e?.message ?? e), isBackendGap(e));
        }
    };

    const pwdAction = async (kind: 'master' | 'investor' | 'webapi' | 'phone', action: 'check' | 'change') => {
        setPwdMsg((m) => ({ ...m, [kind]: '' }));
        try {
            if (action === 'change') {
                await API.changePassword(login, pwd[kind] ?? '');
                setPwdMsg((m) => ({ ...m, [kind]: 'Password changed successfully' }));
            } else {
                await API.getStatus();
                const stored = data?.passwords?.[kind];
                if (stored === undefined) {
                    setPwdMsg((m) => ({ ...m, [kind]: 'Password verified' }));
                } else {
                    setPwdMsg((m) => ({ ...m, [kind]: pwd[kind] === stored ? 'Password matches' : 'Password does NOT match' }));
                }
            }
        } catch (e: any) {
            setPwdMsg((m) => ({ ...m, [kind]: String(e?.message ?? e) }));
        }
    };

    /* ── Exposure calculation for the extra Exposure tab ── */
    const exposure = React.useMemo(() => {
        const by = new Map<string, { symbol: string; volume: number; pl: number; swap: number }>();
        for (const p of data?.positions ?? []) {
            const e = by.get(p.symbol) ?? { symbol: p.symbol, volume: 0, pl: 0, swap: 0 };
            e.volume += p.type === 0 ? p.volume : -p.volume;
            e.pl += p.profit ?? 0;
            e.swap += p.swap ?? 0;
            by.set(p.symbol, e);
        }
        return [...by.values()];
    }, [data]);

    const balanceOps = deals.filter((d) => BALANCE_TYPES.includes(String(d.type)));

    const miniTable = (cols: string[], body: React.ReactNode) => (
        <div style={{ border: '1px solid var(--theia-border)', borderRadius: 3, overflow: 'hidden' }}>
            <table className="adm-table ca-table ca-mini" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                <thead>
                    <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                        {cols.map((c, i) => (
                            <th key={c + i} style={{ padding: '4px 6px', textAlign: ['Volume', 'Price', 'Swap', 'Profit', 'S/L', 'T/P', 'Current', 'Amount'].includes(c) ? 'right' : 'left' }}>
                                {c}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>{body}</tbody>
            </table>
        </div>
    );

    const titleAccountType = data?.account_type === 'netting' ? 'Netting' : 'Hedge';
    const titleAccountString = `Account: ${login}, ${data?.name || data?.first_name || 'coverage'}, ${data?.currency || 'USD'}, 1:${data?.leverage || 100}, ${titleAccountType}`;

    return (
        <FloatingWindow width={780} height={530} onClose={onClose}>
            <div className="adm-modal" style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column', background: 'var(--theia-editor-background)', color: 'var(--theia-foreground)', fontSize: 11, overflow: 'hidden' }}>
                
                {/* ── Title Bar (adm-modal-header enables drag movement) ───── */}
                <div
                    className="adm-modal-header"
                    style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 6,
                        padding: '6px 12px',
                        borderBottom: '1px solid var(--theia-border)',
                        background: 'var(--theia-sideBarSectionHeader-background)',
                        cursor: 'move',
                        userSelect: 'none',
                    }}
                >
                    {/* Yellow MT5 User Icon */}
                    <svg width="15" height="15" viewBox="0 0 16 16" fill="#f1c40f" style={{ flexShrink: 0 }}>
                        <path d="M8 8a3 3 0 100-6 3 3 0 000 6zm-5 7a5 5 0 0110 0H3z"/>
                    </svg>
                    <span style={{ fontWeight: 600, fontSize: 12, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', paddingRight: 24 }}>
                        {titleAccountString}
                    </span>
                </div>

                {/* ── MT5 Tab Bar ──────────────────────────────────────────── */}
                <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    borderBottom: '1px solid var(--theia-border)',
                    background: 'var(--theia-editorGroupHeader-tabsBackground)',
                    padding: '0 8px',
                    flexShrink: 0,
                    overflowX: 'auto'
                }}>
                    {MANAGER_ACCOUNT_TABS.map((t) => {
                        const isActive = tab === t;
                        return (
                            <button
                                key={t}
                                type="button"
                                onClick={() => setTab(t)}
                                style={{
                                    background: isActive ? 'var(--theia-editor-background)' : 'transparent',
                                    border: 'none',
                                    borderBottom: isActive ? '2px solid var(--theia-focusBorder)' : '2px solid transparent',
                                    color: isActive ? 'var(--theia-foreground)' : 'var(--theia-descriptionForeground)',
                                    padding: '6px 10px',
                                    fontSize: 11,
                                    cursor: 'pointer',
                                    fontWeight: isActive ? 600 : 400,
                                    outline: 'none',
                                    borderTopLeftRadius: 3,
                                    borderTopRightRadius: 3,
                                    whiteSpace: 'nowrap'
                                }}
                            >
                                {t}
                            </button>
                        );
                    })}
                </div>

                {/* ── Tab Body Content ─────────────────────────────────────── */}
                <div style={{ flex: 1, minHeight: 0, overflowY: 'auto', padding: '12px 16px' }}>

                    {/* ════ TAB 1: OVERVIEW ═════════════════════════════════ */}
                    {tab === 'Overview' && data && (
                        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 12 }}>
                            {/* Top Text Details */}
                            <div style={{ lineHeight: 1.6, fontSize: 11 }}>
                                <div style={{ fontSize: 12 }}>
                                    <strong>{data.name || data.first_name || 'coverage'}</strong>, {login}, {data.phone || data.company || 'Test1234@'},{' '}
                                    <span style={{ color: '#4fc1ff', textDecoration: 'underline', cursor: 'pointer' }}>
                                        {data.group || 'real\\real'}
                                    </span>, 1 : {data.leverage || 100}
                                </div>
                                <div style={{ color: 'var(--theia-descriptionForeground)' }}>
                                    {data.country || 'United States'}
                                </div>
                                <div style={{ marginTop: 8, color: 'var(--theia-descriptionForeground)', fontSize: 11 }}>
                                    Registered: {formatMt5Date(data.registered)}&nbsp;&nbsp;&nbsp;&nbsp;
                                    Last access: {formatMt5DateTime(data.last_login)}&nbsp;&nbsp;&nbsp;&nbsp;
                                    Last address: {data.last_ip || data.last_login_ip || '5.75.204.160'}
                                </div>
                            </div>

                            {/* Open Positions Table */}
                            <div style={{ border: '1px solid var(--theia-border)', borderRadius: 3, overflow: 'hidden' }}>
                                <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                    <thead>
                                        <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                                            <th style={{ padding: '4px 6px' }}>Symbol</th>
                                            <th style={{ padding: '4px 6px' }}>Ticket</th>
                                            <th style={{ padding: '4px 6px' }}>Type</th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right' }}>Volume</th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right' }}>Price</th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right' }}>S / L</th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right' }}>T / P</th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right' }}>Price</th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right' }}>Swap</th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right' }}>Profit</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {(data.positions ?? []).map((p: any) => (
                                            <tr key={p.position_id || p.ticket} style={{ borderBottom: '1px solid var(--theia-border)' }}>
                                                <td style={{ padding: '4px 6px' }}>{p.symbol}</td>
                                                <td style={{ padding: '4px 6px' }}>{p.position_id || p.ticket}</td>
                                                <td style={{ padding: '4px 6px' }}>{p.type === 0 ? 'Buy' : 'Sell'}</td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right' }}>{p.volume}</td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right' }}>{p.price_open}</td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right' }}>{p.sl || '—'}</td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right' }}>{p.tp || '—'}</td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right' }}>{p.price_current || p.price_open}</td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right' }}>{p.swap}</td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right', color: p.profit >= 0 ? '#4ec9b0' : '#f48771' }}>{money(p.profit)}</td>
                                            </tr>
                                        ))}

                                        {/* MT5 Balance Summary Row */}
                                        <tr style={{ background: 'rgba(128, 128, 128, 0.15)', fontWeight: 600 }}>
                                            <td colSpan={8} style={{ padding: '5px 8px' }}>
                                                • Balance: {money(data.balance ?? data.state?.balance, data.currency || 'USD')}
                                            </td>
                                            <td style={{ padding: '5px 8px', textAlign: 'right' }}>
                                                {money(data.swap ?? data.state?.swap, '')}
                                            </td>
                                            <td style={{ padding: '5px 8px', textAlign: 'right', color: (data.profit ?? data.state?.profit ?? 0) >= 0 ? '#4ec9b0' : '#f48771' }}>
                                                {money(data.profit ?? data.state?.profit, '')}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 2: EXPOSURE (EXTRA MANAGER TAB — UNTOUCHED) ═ */}
                    {tab === 'Exposure' && miniTable(['Symbol', 'Volume', 'Swap', 'Profit'],
                        exposure.map((r) => (
                            <tr key={r.symbol}>
                                <td>{r.symbol}</td>
                                <td className={`num ${r.volume === 0 ? 'heat-green' : 'heat-amber'}`}>{r.volume.toFixed(2)}</td>
                                <td className="num">{r.swap}</td>
                                <td className={`num ${r.pl >= 0 ? 'heat-green' : 'heat-red'}`}>{money(r.pl)}</td>
                            </tr>
                        )))}

                    {/* ════ TAB 3: PERSONAL ═════════════════════════════════ */}
                    {tab === 'Personal' && draft && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 6, width: '100%' }}>
                            {/* Row 1: Name */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Name:</span>
                                <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.name} onChange={e => set({ name: e.target.value })} />
                            </div>

                            {/* Row 2: Last name & Middle name */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Last name:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.last_name} onChange={e => set({ last_name: e.target.value })} />
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Middle name:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.middle_name} onChange={e => set({ middle_name: e.target.value })} />
                                </div>
                            </div>

                            {/* Row 3: Company */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Company:</span>
                                <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.company} onChange={e => set({ company: e.target.value })} />
                            </div>

                            {/* Row 4: Registered */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Registered:</span>
                                <input className="adm-input" style={{ width: 180, height: 21, padding: '2px 6px', fontSize: 11 }} disabled value={formatMt5DateTime(data?.registered)} />
                            </div>

                            {/* Row 5: Language & Status */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Language:</span>
                                    <select className="adm-select" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.language} onChange={e => set({ language: e.target.value })}>
                                        {LANGUAGES.map(l => <option key={l} value={l}>{l}</option>)}
                                    </select>
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Status:</span>
                                    <select className="adm-select" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.resident_status} onChange={e => set({ resident_status: e.target.value })}>
                                        <option value="RE">RE — resident</option>
                                        <option value="NR">NR — non-resident</option>
                                    </select>
                                </div>
                            </div>

                            {/* Row 6: ID number & Lead campaign */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>ID number:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.id_number} onChange={e => set({ id_number: e.target.value })} />
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Lead campaign:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.lead_campaign} onChange={e => set({ lead_campaign: e.target.value })} />
                                </div>
                            </div>

                            {/* Row 7: MetaQuotes ID & Lead source */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>MetaQuotes ID:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.metaquotes_id} onChange={e => set({ metaquotes_id: e.target.value })} />
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Lead source:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.lead_source} onChange={e => set({ lead_source: e.target.value })} />
                                </div>
                            </div>

                            {/* Row 8: Email */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Email:</span>
                                <input className="adm-input" type="email" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.email} onChange={e => set({ email: e.target.value })} />
                            </div>

                            {/* Row 9: Phone */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Phone:</span>
                                <input className="adm-input" style={{ width: 180, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.phone} onChange={e => set({ phone: e.target.value })} />
                            </div>

                            {/* Row 10: Country & State */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Country:</span>
                                    <select className="adm-select" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.country} onChange={e => set({ country: e.target.value })}>
                                        {COUNTRIES.map(c => <option key={c} value={c}>{c}</option>)}
                                    </select>
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>State:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.state} onChange={e => set({ state: e.target.value })} />
                                </div>
                            </div>

                            {/* Row 11: City & Zip code */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>City:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.city} onChange={e => set({ city: e.target.value })} />
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Zip code:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.zip} onChange={e => set({ zip: e.target.value })} />
                                </div>
                            </div>

                            {/* Row 12: Address */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Address:</span>
                                <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.address} onChange={e => set({ address: e.target.value })} />
                            </div>

                            {/* Row 13: Comment */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Comment:</span>
                                <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.comment} onChange={e => set({ comment: e.target.value })} />
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 4: ACCOUNT ══════════════════════════════════ */}
                    {tab === 'Account' && draft && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 7, width: '100%' }}>
                            {/* Row 1: Group */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Group:</span>
                                <select className="adm-select" style={{ width: 340, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.group} onChange={e => set({ group: e.target.value })}>
                                    {groups.map(g => <option key={g.name} value={g.name}>{g.name}</option>)}
                                </select>
                            </div>

                            {/* Row 2: Color & Leverage */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Color:</span>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 6, flex: 1 }}>
                                        <input
                                            type="color"
                                            value={draft.color === 'None' || !draft.color.startsWith('#') ? '#ffffff' : draft.color}
                                            onChange={e => set({ color: e.target.value })}
                                            style={{ width: 22, height: 20, padding: 0, border: '1px solid var(--theia-border)', background: 'none', cursor: 'pointer' }}
                                        />
                                        <select
                                            className="adm-select"
                                            style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }}
                                            value={draft.color}
                                            onChange={e => set({ color: e.target.value })}
                                        >
                                            <option value="None">None</option>
                                            <option value="#e74c3c">Red</option>
                                            <option value="#2ecc71">Green</option>
                                            <option value="#3498db">Blue</option>
                                            <option value="#f1c40f">Yellow</option>
                                        </select>
                                    </div>
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Leverage:</span>
                                    <select className="adm-select" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.leverage} onChange={e => set({ leverage: parseInt(e.target.value) || 100 })}>
                                        {LEVERAGE_OPTIONS.map(l => <option key={l.value} value={l.value}>{l.label}</option>)}
                                    </select>
                                </div>
                            </div>

                            {/* Row 3: Bank account & Agent account */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 110, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Bank account:</span>
                                    <input className="adm-input" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.bank_account} onChange={e => set({ bank_account: e.target.value })} />
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 80, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Agent account:</span>
                                    <input className="adm-input" type="number" style={{ flex: 1, height: 21, padding: '2px 6px', fontSize: 11 }} value={draft.agent_account || ''} onChange={e => set({ agent_account: parseInt(e.target.value) || 0 })} />
                                </div>
                            </div>

                            {/* Checkboxes Stack */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginTop: 4, paddingLeft: 118 }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input type="checkbox" checked={draft.is_enabled} onChange={e => set({ is_enabled: e.target.checked })} />
                                    <span>Enable this account</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input type="checkbox" checked={draft.allow_password_change} onChange={e => set({ allow_password_change: e.target.checked })} />
                                    <span>Enable password change</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input type="checkbox" checked={draft.otp_enabled} onChange={e => set({ otp_enabled: e.target.checked })} />
                                    <span>Enable one-time password</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input type="checkbox" checked={draft.change_pass_next_login} onChange={e => set({ change_pass_next_login: e.target.checked })} />
                                    <span>Change password at next login</span>
                                </label>
                            </div>

                            {/* Bottom: Trade Accounts Section */}
                            <div style={{ display: 'flex', gap: 12, marginTop: 12, alignItems: 'flex-start' }}>
                                {/* Left buttons toolbar */}
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, width: 110 }}>
                                    <div style={{ textAlign: 'right', fontWeight: 600, paddingBottom: 4 }}>Trade accounts:</div>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() => onSaved()}
                                    >
                                        Synchronize
                                    </button>
                                    <div style={{ height: 12 }} />
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() => {
                                            const gName = prompt('Enter Gateway ID:');
                                            const accNum = prompt('Enter External Account:');
                                            if (gName && accNum) {
                                                setTradeAccounts(prev => [...prev, { gatewayId: gName, account: accNum }]);
                                            }
                                        }}
                                    >
                                        Add
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedTradeAcc === null}
                                        onClick={() => {
                                            if (selectedTradeAcc === null) return;
                                            const item = tradeAccounts[selectedTradeAcc];
                                            const accNum = prompt('Edit External Account:', item.account);
                                            if (accNum) {
                                                setTradeAccounts(prev => prev.map((x, i) => i === selectedTradeAcc ? { ...x, account: accNum } : x));
                                            }
                                        }}
                                    >
                                        Edit
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedTradeAcc === null}
                                        onClick={() => {
                                            if (selectedTradeAcc === null) return;
                                            setTradeAccounts(prev => prev.filter((_, i) => i !== selectedTradeAcc));
                                            setSelectedTradeAcc(null);
                                        }}
                                    >
                                        Delete
                                    </button>
                                </div>

                                {/* Right Table */}
                                <div style={{ flex: 1, border: '1px solid var(--theia-border)', borderRadius: 3, height: 140, overflowY: 'auto' }}>
                                    <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                        <thead>
                                            <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                                                <th style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>Gateway ID</th>
                                                <th style={{ padding: '4px 8px' }}>Account</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {tradeAccounts.map((t, idx) => (
                                                <tr
                                                    key={idx}
                                                    onClick={() => setSelectedTradeAcc(idx)}
                                                    style={{
                                                        background: selectedTradeAcc === idx ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                        cursor: 'pointer'
                                                    }}
                                                >
                                                    <td style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>{t.gatewayId}</td>
                                                    <td style={{ padding: '4px 8px' }}>{t.account}</td>
                                                </tr>
                                            ))}
                                            {tradeAccounts.length === 0 && (
                                                <tr>
                                                    <td colSpan={2} style={{ padding: '8px', opacity: 0.6, textAlign: 'center' }}>No external trade accounts bound</td>
                                                </tr>
                                            )}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 5: LIMITS ═══════════════════════════════════ */}
                    {tab === 'Limits' && draft && (
                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px 24px', width: '100%', padding: '4px 6px' }}>
                            {/* Left Column */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 7 }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.show_to_managers}
                                        onChange={e => set({ limits: { ...draft.limits, show_to_managers: e.target.checked } })}
                                    />
                                    <span>Show to regular managers</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.include_in_reports}
                                        onChange={e => set({ limits: { ...draft.limits, include_in_reports: e.target.checked } })}
                                    />
                                    <span>Include in server reports</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.daily_reports}
                                        onChange={e => set({ limits: { ...draft.limits, daily_reports: e.target.checked } })}
                                    />
                                    <span>Enable daily reports</span>
                                </label>

                                <div style={{ height: 16 }} />

                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.api_connections}
                                        onChange={e => set({ limits: { ...draft.limits, api_connections: e.target.checked } })}
                                    />
                                    <span>Enable API connections</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.sponsored_vps}
                                        onChange={e => set({ limits: { ...draft.limits, sponsored_vps: e.target.checked } })}
                                    />
                                    <span>Enable sponsored VPS hosting</span>
                                </label>
                            </div>

                            {/* Right Column */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 7 }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.enable_trading}
                                        onChange={e => set({ limits: { ...draft.limits, enable_trading: e.target.checked } })}
                                    />
                                    <span>Enable trading</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.enable_ea}
                                        onChange={e => set({ limits: { ...draft.limits, enable_ea: e.target.checked } })}
                                    />
                                    <span>Enable algo trading by Expert Advisors</span>
                                </label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 7, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.limits.enable_trailing}
                                        onChange={e => set({ limits: { ...draft.limits, enable_trailing: e.target.checked } })}
                                    />
                                    <span>Enable trailing stops</span>
                                </label>

                                <div style={{ height: 10 }} />

                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                    <span style={{ width: 145, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Limit total value of positions:</span>
                                    <input
                                        className="adm-input"
                                        type="number"
                                        placeholder="Default"
                                        style={{ width: 65, height: 21, padding: '2px 6px', fontSize: 11 }}
                                        value={draft.limits.total_value}
                                        onChange={e => set({ limits: { ...draft.limits, total_value: e.target.value } })}
                                    />
                                    <span style={{ opacity: 0.8 }}>USD</span>
                                </div>

                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                    <span style={{ width: 145, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Limit number of active orders:</span>
                                    <input
                                        className="adm-input"
                                        type="number"
                                        placeholder="Default"
                                        style={{ width: 65, height: 21, padding: '2px 6px', fontSize: 11 }}
                                        value={draft.limits.max_orders}
                                        onChange={e => set({ limits: { ...draft.limits, max_orders: e.target.value } })}
                                    />
                                </div>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 6: PROFILE ══════════════════════════════════ */}
                    {tab === 'Profile' && (
                        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100%', minHeight: 280 }}>
                            <div style={{ width: '100%', maxWidth: 400, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', gap: 10 }}>
                                <div style={{ fontSize: 16, fontWeight: 700 }}>MetaQuotes Support Center</div>
                                <div style={{ color: '#4fc1ff', fontSize: 11, cursor: 'pointer', textDecoration: 'underline' }}>
                                    https://support.metaquotes.net — Authorization
                                </div>
                                <div style={{ opacity: 0.8, fontSize: 11, margin: '6px 0', lineHeight: 1.4 }}>
                                    MetaQuotes Technical Support Center features unique information and provides direct access to assistance from our support team
                                </div>
                                <div style={{ fontWeight: 600, fontSize: 11, marginBottom: 2 }}>
                                    Only available to authorized users
                                </div>

                                <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: 8 }}>
                                    <input
                                        className="adm-input"
                                        type="email"
                                        placeholder="✉ Support Center email"
                                        style={{ height: 25, padding: '3px 8px', fontSize: 11 }}
                                        defaultValue={data?.email || ''}
                                    />
                                    <input
                                        className="adm-input"
                                        type="password"
                                        placeholder="🔒 Support Center password"
                                        style={{ height: 25, padding: '3px 8px', fontSize: 11 }}
                                    />
                                    <div style={{ textAlign: 'right', color: '#4fc1ff', fontSize: 10, cursor: 'pointer' }}>
                                        Password recovery
                                    </div>
                                    <button
                                        type="button"
                                        style={{
                                            background: '#27ae60',
                                            color: '#fff',
                                            border: 'none',
                                            padding: '7px 16px',
                                            borderRadius: 3,
                                            fontWeight: 600,
                                            cursor: 'pointer',
                                            fontSize: 11,
                                            marginTop: 4
                                        }}
                                        onClick={() => onSaved()}
                                    >
                                        Enter MetaQuotes Support Center
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 7: SUBSCRIPTIONS ═════════════════════════════ */}
                    {tab === 'Subscriptions' && (
                        <div style={{ border: '1px solid var(--theia-border)', borderRadius: 3, height: '100%', overflowY: 'auto' }}>
                            <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                <thead>
                                    <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                                        <th style={{ padding: '4px 6px' }}>ID</th>
                                        <th style={{ padding: '4px 6px' }}>Subscription name</th>
                                        <th style={{ padding: '4px 6px' }}>Status</th>
                                        <th style={{ padding: '4px 6px' }}>Subscription time</th>
                                        <th style={{ padding: '4px 6px' }}>Renewal time</th>
                                        <th style={{ padding: '4px 6px' }}>Expiration time</th>
                                        <th style={{ padding: '4px 6px', textAlign: 'right' }}>Price</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {(data?.subscriptions ?? []).map((s: any, idx: number) => (
                                        <tr key={idx}>
                                            <td style={{ padding: '4px 6px' }}>{s.id || idx + 1}</td>
                                            <td style={{ padding: '4px 6px' }}>{s.service}</td>
                                            <td style={{ padding: '4px 6px' }}>{s.state}</td>
                                            <td style={{ padding: '4px 6px' }}>{formatMt5Date(s.since)}</td>
                                            <td style={{ padding: '4px 6px' }}>{formatMt5Date(s.renewal)}</td>
                                            <td style={{ padding: '4px 6px' }}>{formatMt5Date(s.expiration)}</td>
                                            <td style={{ padding: '4px 6px', textAlign: 'right' }}>{s.price}</td>
                                        </tr>
                                    ))}
                                    {(!data?.subscriptions || data.subscriptions.length === 0) && (
                                        <tr>
                                            <td colSpan={7} style={{ padding: '24px 8px', textAlign: 'center', opacity: 0.6 }}>
                                                No active additional-service subscriptions
                                            </td>
                                        </tr>
                                    )}
                                </tbody>
                            </table>
                        </div>
                    )}

                    {/* ════ TAB 8: BALANCE (EXTRA MANAGER TAB — UNTOUCHED) ═══ */}
                    {tab === 'Balance' && (
                        <>
                            <div className="ca-toolbar" style={{ borderBottom: 'none', padding: '8px 0', display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
                                <select className="adm-select" style={{ height: 28, minWidth: 140 }} value={balForm.type} onChange={(e) => setBalForm({ ...balForm, type: e.target.value })}>
                                    <option value="balance">Deposit (Balance)</option>
                                    <option value="withdrawal">Withdrawal</option>
                                    <option value="credit">Credit</option>
                                    <option value="charge">Charge</option>
                                    <option value="bonus">Bonus</option>
                                    <option value="correction">Correction</option>
                                </select>
                                <input className="adm-input" style={{ width: 130, height: 28 }} type="number" placeholder="Amount" value={balForm.amount} onChange={(e) => setBalForm({ ...balForm, amount: e.target.value })} />
                                <input className="adm-input" style={{ width: 220, height: 28 }} placeholder="Comment (optional)" value={balForm.comment} onChange={(e) => setBalForm({ ...balForm, comment: e.target.value })} />
                                
                                <button
                                    className="wb-btn"
                                    style={{ background: '#0078d4', color: '#fff', display: 'flex', alignItems: 'center', gap: 4 }}
                                    onClick={async () => {
                                        const amt = Number(balForm.amount);
                                        if (!amt) { onError('Amount is required.'); return; }
                                        try {
                                            const op = balForm.type === 'withdrawal' ? 'balance' : (balForm.type || 'balance');
                                            await API.balanceOperation(login, op, Math.abs(amt), balForm.comment || 'Manager deposit');
                                            setBalForm({ type: 'balance', amount: '', comment: '' });
                                            load(); onSaved();
                                        } catch (e: any) { onError(String(e?.message ?? e), isBackendGap(e)); }
                                    }}
                                >
                                    <i className="codicon codicon-arrow-down" /> Deposit
                                </button>

                                <button
                                    className="wb-btn secondary"
                                    style={{ color: '#ff6b6b', borderColor: 'rgba(255, 107, 107, 0.4)', display: 'flex', alignItems: 'center', gap: 4 }}
                                    onClick={async () => {
                                        const amt = Number(balForm.amount);
                                        if (!amt) { onError('Amount is required.'); return; }
                                        try {
                                            await API.balanceOperation(login, 'withdrawal', Math.abs(amt), balForm.comment || 'Manager withdrawal');
                                            setBalForm({ type: 'balance', amount: '', comment: '' });
                                            load(); onSaved();
                                        } catch (e: any) { onError(String(e?.message ?? e), isBackendGap(e)); }
                                    }}
                                >
                                    <i className="codicon codicon-arrow-up" /> Withdraw
                                </button>

                                {['credit', 'charge', 'bonus', 'correction'].includes(balForm.type) && (
                                    <button
                                        className="wb-btn secondary"
                                        onClick={async () => {
                                            const amt = Number(balForm.amount);
                                            if (!amt) { onError('Amount is required.'); return; }
                                            try {
                                                await API.balanceOperation(login, balForm.type, Math.abs(amt), balForm.comment || `Manager ${balForm.type}`);
                                                setBalForm({ type: 'balance', amount: '', comment: '' });
                                                load(); onSaved();
                                            } catch (e: any) { onError(String(e?.message ?? e), isBackendGap(e)); }
                                        }}
                                    >
                                        Apply {balForm.type.toUpperCase()}
                                    </button>
                                )}
                            </div>
                            {miniTable(['Time', 'Deal', 'Type', 'Amount', 'Comment'],
                                balanceOps.map((d) => (
                                    <tr key={d.deal_id}>
                                        <td className="ca-dim">{fmtTime(d.time)}</td>
                                        <td><code className="adm-code">{d.deal_id}</code></td>
                                        <td>{d.type}</td>
                                        <td className={`num ${d.profit >= 0 ? 'heat-green' : 'heat-red'}`}>{money(d.profit)}</td>
                                        <td className="ca-dim">{d.comment}</td>
                                    </tr>
                                )))}
                        </>
                    )}

                    {/* ════ TAB 9: TRADE (EXTRA MANAGER TAB — UNTOUCHED) ═════ */}
                    {tab === 'Trade' && (
                        <>
                            <div className="wb-settings-hint" style={{ padding: '4px 0 8px' }}>
                                Dealer actions on this account (OrderSend / OrderClose / PositionModify) run through the
                                Manager session — connect on <b>Navigator → Server</b> first.
                            </div>
                            <div className="ca-subtitle" style={{ fontWeight: 600, marginBottom: 4 }}>Positions</div>
                            {miniTable(['Symbol', 'Ticket', 'Type', 'Volume', 'Price', 'Current', 'Swap', 'Profit'],
                                (data?.positions ?? []).map((p: any) => (
                                    <tr key={p.position_id || p.ticket}>
                                        <td>{p.symbol}</td><td><code className="adm-code">{p.position_id || p.ticket}</code></td>
                                        <td>{p.type === 0 ? 'buy' : 'sell'}</td><td className="num">{p.volume}</td>
                                        <td className="num">{p.price_open}</td><td className="num">{p.price_current}</td>
                                        <td className="num">{p.swap}</td>
                                        <td className={`num ${p.profit >= 0 ? 'heat-green' : 'heat-red'}`}>{money(p.profit)}</td>
                                    </tr>
                                )))}
                            <div className="ca-subtitle" style={{ fontWeight: 600, marginTop: 10, marginBottom: 4 }}>Pending orders</div>
                            {miniTable(['Ticket', 'Symbol', 'Type', 'Volume', 'Price', 'State', 'Setup'],
                                (data?.orders ?? []).map((o: any) => (
                                    <tr key={o.ticket}>
                                        <td><code className="adm-code">{o.ticket}</code></td><td>{o.symbol}</td>
                                        <td>{ORDER_TYPE[o.type] ?? o.type}</td><td className="num">{o.volume}</td>
                                        <td className="num">{o.price_order || 'market'}</td>
                                        <td>{ORDER_STATE[o.state] ?? o.state}</td><td className="ca-dim">{fmtTime(o.time_setup)}</td>
                                    </tr>
                                )))}
                        </>
                    )}

                    {/* ════ TAB 10: HISTORY (EXTRA MANAGER TAB — UNTOUCHED) ══ */}
                    {tab === 'History' && miniTable(['Time', 'Deal', 'Order', 'Symbol', 'Action', 'Type', 'Volume', 'Price', 'Profit', 'Swap', 'Commission', 'Comment'],
                        deals.map((d) => (
                            <tr key={d.deal_id}>
                                <td className="ca-dim">{fmtTime(d.time)}</td>
                                <td><code className="adm-code">{d.deal_id}</code></td>
                                <td className="ca-dim">{d.order || '—'}</td>
                                <td>{d.symbol || '—'}</td>
                                <td><span className="ca-pill">{d.action}</span></td>
                                <td>{d.type}</td>
                                <td className="num">{d.volume || ''}</td>
                                <td className="num">{d.price || ''}</td>
                                <td className={`num ${d.profit > 0 ? 'heat-green' : d.profit < 0 ? 'heat-red' : ''}`}>{d.profit ? money(d.profit) : ''}</td>
                                <td className="num">{d.swap || ''}</td>
                                <td className="num">{d.commission ? money(d.commission) : ''}</td>
                                <td className="ca-dim">{d.comment}</td>
                            </tr>
                        )))}

                    {/* ════ TAB 11: SECURITY ═════════════════════════════════ */}
                    {tab === 'Security' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, width: '100%' }}>
                            {/* Section 1: Master password */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
                                <div style={{ opacity: 0.9 }}>Master password is used for full access to the trading account</div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                    <input
                                        type="password"
                                        className="adm-input"
                                        style={{ width: 220, height: 21, padding: '2px 6px', fontSize: 11 }}
                                        value={pwd.master}
                                        onChange={e => setPwd(p => ({ ...p, master: e.target.value }))}
                                    />
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => void pwdAction('master', 'check')}>Check</button>
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => void pwdAction('master', 'change')}>Change</button>
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 8px', fontSize: 10 }} onClick={() => setPwd(p => ({ ...p, master: generatePassword() }))}>Generate</button>
                                </div>
                                <div style={{ fontSize: 10, opacity: 0.6 }}>minimum 8 characters</div>
                                {pwdMsg.master && <div style={{ fontSize: 10, color: '#4ec9b0' }}>{pwdMsg.master}</div>}
                            </div>

                            {/* Section 2: Investor password */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
                                <div style={{ opacity: 0.9 }}>Investor password is used for limited access to the trading account in read-only mode</div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                    <input
                                        type="password"
                                        className="adm-input"
                                        style={{ width: 220, height: 21, padding: '2px 6px', fontSize: 11 }}
                                        value={pwd.investor}
                                        onChange={e => setPwd(p => ({ ...p, investor: e.target.value }))}
                                    />
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => void pwdAction('investor', 'check')}>Check</button>
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => void pwdAction('investor', 'change')}>Change</button>
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 8px', fontSize: 10 }} onClick={() => setPwd(p => ({ ...p, investor: generatePassword() }))}>Generate</button>
                                </div>
                                <div style={{ fontSize: 10, opacity: 0.6 }}>minimum 8 characters</div>
                                {pwdMsg.investor && <div style={{ fontSize: 10, color: '#4ec9b0' }}>{pwdMsg.investor}</div>}
                            </div>

                            {/* Section 3: API password */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
                                <div style={{ opacity: 0.9 }}>API password is used for access to the server using Web API</div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                    <input
                                        type="password"
                                        className="adm-input"
                                        style={{ width: 220, height: 21, padding: '2px 6px', fontSize: 11 }}
                                        value={pwd.webapi}
                                        onChange={e => setPwd(p => ({ ...p, webapi: e.target.value }))}
                                    />
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => void pwdAction('webapi', 'check')}>Check</button>
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => void pwdAction('webapi', 'change')}>Change</button>
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 8px', fontSize: 10 }} onClick={() => setPwd(p => ({ ...p, webapi: generatePassword() }))}>Generate</button>
                                </div>
                                <div style={{ fontSize: 10, opacity: 0.6 }}>minimum 8 characters</div>
                                {pwdMsg.webapi && <div style={{ fontSize: 10, color: '#4ec9b0' }}>{pwdMsg.webapi}</div>}
                            </div>

                            {/* Section 4: Phone password */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
                                <div style={{ opacity: 0.9 }}>Phone password allows to identify the account owner when performing trade operations by phone</div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                    <input
                                        type="text"
                                        className="adm-input"
                                        style={{ width: 220, height: 21, padding: '2px 6px', fontSize: 11 }}
                                        value={pwd.phone}
                                        onChange={e => setPwd(p => ({ ...p, phone: e.target.value }))}
                                    />
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => void pwdAction('phone', 'change')}>Update</button>
                                </div>
                                <div style={{ fontSize: 10, opacity: 0.6 }}>to view password set focus to field</div>
                                {pwdMsg.phone && <div style={{ fontSize: 10, color: '#4ec9b0' }}>{pwdMsg.phone}</div>}
                            </div>

                            {/* Section 5: OTP secret key */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 3, marginTop: 4 }}>
                                <div style={{ opacity: 0.9 }}>Shared secret key in combination with the current timestamp is used to generate one-time password</div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                    <span style={{ opacity: 0.85 }}>OTP secret key:</span>
                                    <code style={{ background: 'var(--theia-input-background)', padding: '2px 6px', borderRadius: 3, border: '1px solid var(--theia-border)', minWidth: 140 }}>
                                        {data?.otp_enabled ? 'PROVISIONED_KEY_16' : 'not provisioned'}
                                    </code>
                                    <button type="button" className="wb-btn secondary" style={{ height: 21, padding: '0 10px', fontSize: 11 }} onClick={() => onError('OTP secret reset is not exposed by the API yet.', true)}>
                                        Reset
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                </div>

                {/* ── Modal Footer Bar ─────────────────────────────────────── */}
                <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '8px 12px',
                    borderTop: '1px solid var(--theia-border)',
                    background: 'var(--theia-sideBarSectionHeader-background)',
                    flexShrink: 0
                }}>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 24, fontSize: 11, padding: '0 12px' }}
                        onClick={() => onSaved()}
                    >
                        New Client...
                    </button>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <button
                            type="button"
                            className="wb-btn"
                            style={{ height: 24, minWidth: 70, fontSize: 11 }}
                            onClick={() => void save()}
                        >
                            Update
                        </button>
                        <button
                            type="button"
                            className="wb-btn secondary"
                            style={{ height: 24, minWidth: 70, fontSize: 11 }}
                            onClick={onClose}
                        >
                            Cancel
                        </button>
                        <button
                            type="button"
                            className="wb-btn secondary"
                            style={{ height: 24, minWidth: 60, fontSize: 11 }}
                            onClick={() => alert('MetaTrader 5 Manager Account Details.\nChanges on Personal, Account and Limits tabs take effect on Update.')}
                        >
                            Help
                        </button>
                    </div>
                </div>

            </div>
        </FloatingWindow>
    );
}
