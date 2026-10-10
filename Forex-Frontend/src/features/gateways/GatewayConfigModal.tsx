import * as React from 'react';
import { FloatingWindow } from '../../shared/FloatingWindow';

export interface GatewayRecord {
    id: number;
    name: string;
    module: string;
    mode: 'Trade and Quotes' | 'Trade Only' | 'Quotes Only' | string;
    server: string;
    login: string | number;
    password?: string;
    groups: string;
    symbols: string;
    last_active?: string;
    lastActive?: string;
    status?: string;
    is_active: boolean;
    enabled?: boolean;
    import_traders_balances?: boolean;
    import_symbol_settings?: boolean;
    translations?: Array<{ symbol: string; source: string; bid: number; ask: number }>;
    parameters?: Array<{ parameter: string; value: string }>;
    timeouts?: {
        reconnect_interval: number;
        reconnect_attempts: number;
        reconnect_series_interval: number;
    };
    monitoring?: {
        enable_logging: boolean;
        enable_profiling: boolean;
        collect_days: number;
    };
    advanced_network?: {
        gateway_server: string;
        gateway_login: string;
        password?: string;
    };
}

interface GatewayConfigModalProps {
    gateway?: GatewayRecord | null;
    isNew?: boolean;
    onClose: () => void;
    onSave: (gateway: GatewayRecord) => void;
}

const GATEWAY_TABS = [
    'Common',
    'Groups',
    'Symbols',
    'Translations',
    'Parameters',
    'Timeouts',
    'Monitoring',
] as const;
type TabId = (typeof GATEWAY_TABS)[number];

const AVAILABLE_MODULES = [
    { name: 'MetaTrader 5 Gateway', file: 'MT5Gateway.dll' },
    { name: 'Currenex FIX Gateway', file: 'CurrenexGateway.dll' },
    { name: 'Integral FX Inside Gateway', file: 'IntegralGateway.dll' },
    { name: 'LMAX FIX Gateway', file: 'LMAXGateway.dll' },
    { name: 'Cboe FX / Hotspot Gateway', file: 'CboeFXGateway.dll' },
    { name: 'FastMatch FX Gateway', file: 'FastMatchGateway.dll' },
    { name: 'Swissquote Bank Gateway', file: 'SwissquoteGateway.dll' },
    { name: 'Centroid Bridge Gateway', file: 'CentroidBridge.dll' },
    { name: 'Interactive Brokers Gateway', file: 'IBGateway.dll' },
    { name: 'B2Broker Multi-Asset Gateway', file: 'B2BrokerGateway.dll' },
];

const STANDARD_PARAMETERS = [
    'NewsCategory',
    'Quotes Delay',
    'Quotes Tickstats Sample',
    'Quotes Ticks Sample',
    'Quotes Books Sample',
    'Trading Calendar Holidays',
    'Max Price Deviation',
    'Limit Orders Coverage Mode',
    'Quotes Time Original',
    'Last Price Markup',
    'Symbols Path',
    'Symbols Update',
    'Calculate Hedged Margin',
    'Calculate Hedged Margin ...',
    'News Enable',
];

// Reusable MT5-style modal overlay for inner sub-dialogs
function SubDialogOverlay({
    title,
    icon,
    children,
    onClose,
    onOk,
    width = 440,
}: {
    title: string;
    icon?: React.ReactNode;
    children: React.ReactNode;
    onClose: () => void;
    onOk: () => void;
    width?: number;
}): React.ReactElement {
    React.useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === 'Escape') {
                e.stopPropagation();
                onClose();
            } else if (e.key === 'Enter') {
                const target = e.target as HTMLElement;
                if (target.tagName !== 'TEXTAREA') {
                    e.preventDefault();
                    onOk();
                }
            }
        };
        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    }, [onClose, onOk]);

    return (
        <div
            className="adm-modal-overlay"
            style={{
                position: 'fixed',
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                backgroundColor: 'rgba(0, 0, 0, 0.55)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                zIndex: 3500,
            }}
            onClick={onClose}
        >
            <div
                className="adm-modal"
                style={{
                    width,
                    maxWidth: '92vw',
                    backgroundColor: 'var(--theia-editor-background, #252526)',
                    border: '1px solid var(--theia-border, #454545)',
                    boxShadow: '0 8px 26px rgba(0, 0, 0, 0.65)',
                    borderRadius: 3,
                    display: 'flex',
                    flexDirection: 'column',
                    overflow: 'hidden',
                }}
                onClick={(e) => e.stopPropagation()}
            >
                {/* Header */}
                <div
                    style={{
                        padding: '6px 12px',
                        backgroundColor: 'var(--theia-editorGroupHeader-tabsBackground, #2d2d2d)',
                        borderBottom: '1px solid var(--theia-border, #3a3a3a)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        fontWeight: 600,
                        fontSize: 12,
                        color: 'var(--theia-ui-typography-color-heading, #e6edf3)',
                        userSelect: 'none',
                    }}
                >
                    <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
                        {icon}
                        <span>{title}</span>
                    </div>
                    <button
                        type="button"
                        onClick={onClose}
                        style={{
                            background: 'transparent',
                            border: 'none',
                            color: '#8b949e',
                            cursor: 'pointer',
                            fontSize: 14,
                            padding: '0 4px',
                        }}
                    >
                        ✕
                    </button>
                </div>

                {/* Body */}
                <div style={{ padding: '14px 16px', fontSize: 11, color: 'var(--theia-foreground, #ccc)' }}>
                    {children}
                </div>

                {/* Footer */}
                <div
                    style={{
                        padding: '8px 14px',
                        backgroundColor: 'var(--theia-editorGroupHeader-tabsBackground, #202020)',
                        borderTop: '1px solid var(--theia-border, #333)',
                        display: 'flex',
                        justifyContent: 'flex-end',
                        gap: 8,
                    }}
                >
                    <button
                        type="button"
                        className="wb-btn primary"
                        style={{ height: 23, minWidth: 65, fontSize: 11 }}
                        onClick={onOk}
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
                </div>
            </div>
        </div>
    );
}

// 1. Translation Sub-Dialog
function TranslationSubDialog({
    initial,
    onSave,
    onClose,
}: {
    initial?: { symbol: string; source: string; bid: number; ask: number };
    onSave: (item: { symbol: string; source: string; bid: number; ask: number }) => void;
    onClose: () => void;
}): React.ReactElement {
    const [symbol, setSymbol] = React.useState(initial?.symbol || 'EURUSD');
    const [source, setSource] = React.useState(initial?.source || 'EUR/USD');
    const [bid, setBid] = React.useState(initial?.bid ?? -1);
    const [ask, setAsk] = React.useState(initial?.ask ?? 1);

    const handleSubmit = () => {
        if (!symbol.trim()) return;
        onSave({
            symbol: symbol.trim(),
            source: source.trim(),
            bid: Number(bid) || 0,
            ask: Number(ask) || 0,
        });
    };

    return (
        <SubDialogOverlay
            title="Translation"
            icon={<i className="codicon codicon-arrow-swap" style={{ color: '#e5c07b' }} />}
            onClose={onClose}
            onOk={handleSubmit}
            width={440}
        >
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                <div style={{ display: 'grid', gridTemplateColumns: '75px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Symbol:</label>
                    <input
                        type="text"
                        className="adm-input"
                        value={symbol}
                        onChange={(e) => setSymbol(e.target.value)}
                        placeholder="e.g. EURUSD or *.GW"
                        autoFocus
                    />
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '75px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Source:</label>
                    <input
                        type="text"
                        className="adm-input"
                        value={source}
                        onChange={(e) => setSource(e.target.value)}
                        placeholder="e.g. EUR/USD or *"
                    />
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '75px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Bid:</label>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                        <input
                            type="number"
                            className="adm-input"
                            value={bid}
                            onChange={(e) => setBid(Number(e.target.value))}
                            style={{ width: 100 }}
                        />
                        <span style={{ fontSize: 11, color: '#888' }}>points (e.g. -1)</span>
                    </div>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '75px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Ask:</label>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                        <input
                            type="number"
                            className="adm-input"
                            value={ask}
                            onChange={(e) => setAsk(Number(e.target.value))}
                            style={{ width: 100 }}
                        />
                        <span style={{ fontSize: 11, color: '#888' }}>points (e.g. +1)</span>
                    </div>
                </div>

                <div
                    style={{
                        marginTop: 4,
                        padding: 8,
                        background: 'rgba(56, 139, 253, 0.08)',
                        border: '1px solid rgba(56, 139, 253, 0.2)',
                        borderRadius: 3,
                        fontSize: 11,
                        color: '#90bdf4',
                        lineHeight: 1.4,
                    }}
                >
                    Specify symbol names in MetaTrader 5 and external system, and quote correction values in points (e.g. -1 for Bid, +1 for Ask).
                </div>
            </div>
        </SubDialogOverlay>
    );
}

// 2. Group Sub-Dialog
function GroupSubDialog({
    initial,
    onSave,
    onClose,
}: {
    initial?: string;
    onSave: (group: string) => void;
    onClose: () => void;
}): React.ReactElement {
    const [group, setGroup] = React.useState(initial || 'demo\\*');

    const handleSubmit = () => {
        if (!group.trim()) return;
        onSave(group.trim());
    };

    return (
        <SubDialogOverlay
            title="Group"
            icon={<i className="codicon codicon-organization" style={{ color: '#4fc1ff' }} />}
            onClose={onClose}
            onOk={handleSubmit}
            width={400}
        >
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                <div style={{ display: 'grid', gridTemplateColumns: '70px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Group:</label>
                    <input
                        type="text"
                        className="adm-input"
                        value={group}
                        onChange={(e) => setGroup(e.target.value)}
                        placeholder="e.g. real\*, demo\*, or *"
                        autoFocus
                    />
                </div>

                <div
                    style={{
                        padding: 8,
                        background: 'rgba(255, 255, 255, 0.04)',
                        border: '1px solid var(--theia-border, #333)',
                        borderRadius: 3,
                        fontSize: 11,
                        color: '#aaa',
                        lineHeight: 1.4,
                    }}
                >
                    Specify a group or subgroup from those available on the server. Wildcard masks (*) are supported.
                </div>
            </div>
        </SubDialogOverlay>
    );
}

// 3. Symbol Sub-Dialog
function SymbolSubDialog({
    initial,
    onSave,
    onClose,
}: {
    initial?: string;
    onSave: (symbol: string) => void;
    onClose: () => void;
}): React.ReactElement {
    const [symbol, setSymbol] = React.useState(initial || '*');

    const handleSubmit = () => {
        if (!symbol.trim()) return;
        onSave(symbol.trim());
    };

    return (
        <SubDialogOverlay
            title="Symbol"
            icon={<i className="codicon codicon-symbol-class" style={{ color: '#e5c07b' }} />}
            onClose={onClose}
            onOk={handleSubmit}
            width={400}
        >
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                <div style={{ display: 'grid', gridTemplateColumns: '70px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Symbol:</label>
                    <input
                        type="text"
                        className="adm-input"
                        value={symbol}
                        onChange={(e) => setSymbol(e.target.value)}
                        placeholder="e.g. *, Forex\*, EURUSD"
                        autoFocus
                    />
                </div>

                <div
                    style={{
                        padding: 8,
                        background: 'rgba(255, 255, 255, 0.04)',
                        border: '1px solid var(--theia-border, #333)',
                        borderRadius: 3,
                        fontSize: 11,
                        color: '#aaa',
                        lineHeight: 1.4,
                    }}
                >
                    Specify symbols or groups of symbols. You can additionally use mask '*' and negation sign '!'.
                </div>
            </div>
        </SubDialogOverlay>
    );
}

// 4. Parameter Sub-Dialog
function ParameterSubDialog({
    initial,
    onSave,
    onClose,
}: {
    initial?: { parameter: string; value: string };
    onSave: (item: { parameter: string; value: string }) => void;
    onClose: () => void;
}): React.ReactElement {
    const [parameter, setParameter] = React.useState(initial?.parameter || '');
    const [value, setValue] = React.useState(initial?.value || '');

    const handleSubmit = () => {
        if (!parameter.trim()) return;
        onSave({ parameter: parameter.trim(), value: value.trim() });
    };

    return (
        <SubDialogOverlay
            title="Parameter"
            icon={<i className="codicon codicon-settings-gear" style={{ color: '#4fc1ff' }} />}
            onClose={onClose}
            onOk={handleSubmit}
            width={430}
        >
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                <div style={{ display: 'grid', gridTemplateColumns: '80px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Parameter:</label>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
                        <input
                            type="text"
                            list="param-suggestions"
                            className="adm-input"
                            value={parameter}
                            onChange={(e) => setParameter(e.target.value)}
                            placeholder="Parameter name"
                            autoFocus
                        />
                        <datalist id="param-suggestions">
                            {STANDARD_PARAMETERS.map((p) => (
                                <option key={p} value={p} />
                            ))}
                        </datalist>
                    </div>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '80px 1fr', alignItems: 'center', gap: 8 }}>
                    <label style={{ fontSize: 11, color: '#aaa', textAlign: 'right' }}>Value:</label>
                    <input
                        type="text"
                        className="adm-input"
                        value={value}
                        onChange={(e) => setValue(e.target.value)}
                        placeholder="Parameter value"
                    />
                </div>

                <div
                    style={{
                        padding: 8,
                        background: 'rgba(255, 255, 255, 0.04)',
                        border: '1px solid var(--theia-border, #333)',
                        borderRadius: 3,
                        fontSize: 11,
                        color: '#aaa',
                        lineHeight: 1.4,
                    }}
                >
                    Specify additional parameters for passing extra settings to the gateway for its correct operation.
                </div>
            </div>
        </SubDialogOverlay>
    );
}

// 5. Help Sub-Dialog
function GatewayHelpDialog({ onClose }: { onClose: () => void }): React.ReactElement {
    return (
        <SubDialogOverlay
            title="MetaTrader 5 Gateway Help"
            icon={<i className="codicon codicon-question" style={{ color: '#58a6ff' }} />}
            onClose={onClose}
            onOk={onClose}
            width={500}
        >
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10, fontSize: 12, lineHeight: 1.5, color: '#ccc' }}>
                <div style={{ fontWeight: 600, color: '#e6edf3' }}>MetaTrader 5 Gateway Configuration</div>
                <p style={{ margin: 0 }}>
                    Gateways integrate MetaTrader 5 with external trading systems, liquidity providers (LPs), and exchanges.
                </p>
                <ul style={{ margin: '4px 0 0 16px', padding: 0 }}>
                    <li><strong>Common:</strong> Credentials, server endpoints, and platform dealer ID.</li>
                    <li><strong>Groups:</strong> Which client groups have their orders routed through this gateway.</li>
                    <li><strong>Symbols:</strong> Which trading symbols receive quotes and execute trades.</li>
                    <li><strong>Translations:</strong> Map instrument names and apply bid/ask point markups.</li>
                    <li><strong>Parameters:</strong> Module-specific parameters like quote thinning and schedules.</li>
                    <li><strong>Timeouts:</strong> Automatic reconnect intervals and failover policies.</li>
                    <li><strong>Monitoring:</strong> Detailed logging, profiling, and latency tracking.</li>
                </ul>
            </div>
        </SubDialogOverlay>
    );
}

export function GatewayConfigModal({ gateway, isNew, onClose, onSave }: GatewayConfigModalProps): React.ReactElement {
    const [tab, setTab] = React.useState<TabId>('Common');
    const [showAdvancedNetwork, setShowAdvancedNetwork] = React.useState(false);

    // Draft form state
    const [draft, setDraft] = React.useState<GatewayRecord>({
        id: gateway?.id ?? Date.now(),
        name: gateway?.name ?? 'New Gateway',
        module: gateway?.module ?? 'MetaTrader 5 Gateway',
        mode: gateway?.mode ?? 'Trade and Quotes',
        server: gateway?.server ?? 'access.metatrader5.com:443',
        login: gateway?.login ?? '1000',
        password: gateway?.password ?? '••••••••',
        groups: gateway?.groups ?? '*',
        symbols: gateway?.symbols ?? '*',
        last_active: gateway?.last_active ?? 'Online',
        status: gateway?.status ?? 'Online',
        is_active: gateway?.is_active ?? true,
        import_traders_balances: gateway?.import_traders_balances ?? false,
        import_symbol_settings: gateway?.import_symbol_settings ?? false,
        translations: gateway?.translations ? [...gateway.translations] : [
            { symbol: 'EURUSD', source: 'EUR/USD', bid: -1, ask: 1 }
        ],
        parameters: gateway?.parameters ? [...gateway.parameters] : [
            { parameter: 'Trading Calendar Holidays', value: '' },
            { parameter: 'Max Price Deviation', value: '50' },
            { parameter: 'Limit Orders Coverage Mode', value: 'Market' },
            { parameter: 'Quotes Time Original', value: 'No' },
            { parameter: 'Last Price Markup', value: 'Yes' },
            { parameter: 'Symbols Path', value: '' },
            { parameter: 'Symbols Update', value: 'No' },
            { parameter: 'Calculate Hedged Margin', value: 'No' },
            { parameter: 'Calculate Hedged Margin ...', value: '2.0' },
            { parameter: 'News Enable', value: 'No' },
        ],
        timeouts: gateway?.timeouts ? { ...gateway.timeouts } : {
            reconnect_interval: 1,
            reconnect_attempts: 5,
            reconnect_series_interval: 60,
        },
        monitoring: gateway?.monitoring ? { ...gateway.monitoring } : {
            enable_logging: false,
            enable_profiling: false,
            collect_days: 0,
        },
        advanced_network: gateway?.advanced_network ? { ...gateway.advanced_network } : {
            gateway_server: '127.0.0.1:16387',
            gateway_login: '1000',
            password: '',
        },
    });

    // Selections for sub-lists
    const [selectedGroupIdx, setSelectedGroupIdx] = React.useState<number | null>(0);
    const [selectedSymbolIdx, setSelectedSymbolIdx] = React.useState<number | null>(0);
    const [selectedTransIdx, setSelectedTransIdx] = React.useState<number | null>(0);
    const [selectedParamIdx, setSelectedParamIdx] = React.useState<number | null>(0);

    // Sub-dialog modal states
    const [groupDialog, setGroupDialog] = React.useState<{ open: boolean; isEdit: boolean; value: string } | null>(null);
    const [symbolDialog, setSymbolDialog] = React.useState<{ open: boolean; isEdit: boolean; value: string } | null>(null);
    const [transDialog, setTransDialog] = React.useState<{
        open: boolean;
        isEdit: boolean;
        item: { symbol: string; source: string; bid: number; ask: number };
    } | null>(null);
    const [paramDialog, setParamDialog] = React.useState<{
        open: boolean;
        isEdit: boolean;
        item: { parameter: string; value: string };
    } | null>(null);
    const [showHelpDialog, setShowHelpDialog] = React.useState(false);

    // Parsed groups and symbols list
    const groupsList = React.useMemo(() => {
        if (!draft.groups) return [];
        return draft.groups
            .split(',')
            .map((s) => s.trim())
            .filter(Boolean);
    }, [draft.groups]);

    const symbolsList = React.useMemo(() => {
        if (!draft.symbols) return [];
        return draft.symbols
            .split(',')
            .map((s) => s.trim())
            .filter(Boolean);
    }, [draft.symbols]);

    const handleSave = () => {
        onSave(draft);
        onClose();
    };

    // Yellow/Grey cylinder gateway icon component
    const GatewayCylinderIcon = () => (
        <svg width="40" height="40" viewBox="0 0 48 48" style={{ flexShrink: 0 }}>
            {/* Top grey tip */}
            <rect x="20" y="5" width="8" height="8" rx="3" fill="#7f8c8d" transform="rotate(45 24 9)" />
            {/* Yellow central cylinder */}
            <rect x="14" y="14" width="20" height="20" rx="5" fill="#f1c40f" transform="rotate(45 24 24)" />
            {/* Bottom grey tip */}
            <rect x="20" y="35" width="8" height="8" rx="3" fill="#7f8c8d" transform="rotate(45 24 39)" />
        </svg>
    );

    return (
        <FloatingWindow width={620} height={500} onClose={onClose}>
            <div
                className="adm-modal"
                style={{
                    width: '100%',
                    height: '100%',
                    display: 'flex',
                    flexDirection: 'column',
                    background: 'var(--theia-editor-background)',
                    color: 'var(--theia-foreground)',
                    fontSize: 11,
                    overflow: 'hidden',
                    position: 'relative',
                }}
            >
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
                        userSelect: 'none',
                    }}
                >
                    <span>Gateway: {draft.name || (isNew ? 'New Gateway' : 'Gateway')}</span>
                    <button
                        type="button"
                        onClick={onClose}
                        style={{ background: 'none', border: 'none', color: 'var(--theia-foreground)', cursor: 'pointer', opacity: 0.7 }}
                    >
                        ✕
                    </button>
                </div>

                {/* ── Tab Bar (7 MT5 Tabs) ──────────────────────────────── */}
                <div
                    style={{
                        display: 'flex',
                        alignItems: 'center',
                        borderBottom: '1px solid var(--theia-border)',
                        background: 'var(--theia-editorGroupHeader-tabsBackground)',
                        padding: '0 8px',
                        flexShrink: 0,
                        overflowX: 'auto',
                    }}
                >
                    {GATEWAY_TABS.map((t) => {
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
                                    padding: '6px 12px',
                                    fontSize: 11,
                                    cursor: 'pointer',
                                    fontWeight: isActive ? 600 : 400,
                                    outline: 'none',
                                    borderTopLeftRadius: 3,
                                    borderTopRightRadius: 3,
                                    whiteSpace: 'nowrap',
                                }}
                            >
                                {t}
                            </button>
                        );
                    })}
                </div>

                {/* ── Tab Body Content ──────────────────────────────────── */}
                <div style={{ flex: 1, minHeight: 0, overflowY: 'auto', padding: '14px 18px', display: 'flex', flexDirection: 'column' }}>
                    {/* ════ TAB 1: COMMON (gateway_common.png) ═════════════ */}
                    {tab === 'Common' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            {/* Header row with icon & description */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <GatewayCylinderIcon />
                                <div style={{ fontSize: 11, lineHeight: 1.4, opacity: 0.9 }}>
                                    This gateway allows connecting to an external trading system or remote MetaTrader 5 Platform.
                                </div>
                            </div>

                            {/* Enable Checkbox */}
                            <div style={{ paddingLeft: 115, margin: '2px 0' }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.is_active}
                                        onChange={(e) => setDraft({ ...draft, is_active: e.target.checked, enabled: e.target.checked })}
                                    />
                                    <span>Enable</span>
                                </label>
                            </div>

                            {/* Name & ID */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 2 }}>
                                    <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Name:</span>
                                    <input
                                        className="adm-input"
                                        style={{ flex: 1, height: 22, fontSize: 11 }}
                                        value={draft.name}
                                        onChange={(e) => setDraft({ ...draft, name: e.target.value })}
                                    />
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <span style={{ width: 30, textAlign: 'right', opacity: 0.85 }}>ID:</span>
                                    <input
                                        className="adm-input"
                                        style={{ flex: 1, height: 22, fontSize: 11 }}
                                        value={draft.id}
                                        disabled={!isNew}
                                        onChange={(e) => setDraft({ ...draft, id: Number(e.target.value) || 0 })}
                                    />
                                </div>
                            </div>

                            {/* Module & Mode */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 2 }}>
                                    <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Module:</span>
                                    <select
                                        className="adm-select"
                                        style={{ flex: 1, height: 22, fontSize: 11 }}
                                        value={draft.module}
                                        onChange={(e) => setDraft({ ...draft, module: e.target.value })}
                                    >
                                        {AVAILABLE_MODULES.map((m) => (
                                            <option key={m.file} value={m.name}>
                                                {m.name}
                                            </option>
                                        ))}
                                    </select>
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
                                    <select
                                        className="adm-select"
                                        style={{ flex: 1, height: 22, fontSize: 11 }}
                                        value={draft.mode}
                                        onChange={(e) => setDraft({ ...draft, mode: e.target.value })}
                                    >
                                        <option value="Trade and Quotes">Trade and Quotes</option>
                                        <option value="Trade Only">Trade Only</option>
                                        <option value="Quotes Only">Quotes Only</option>
                                    </select>
                                </div>
                            </div>

                            {/* Trading server */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Trading server:</span>
                                <input
                                    className="adm-input"
                                    style={{ flex: 1, height: 22, fontSize: 11 }}
                                    value={draft.server}
                                    onChange={(e) => setDraft({ ...draft, server: e.target.value })}
                                />
                            </div>

                            {/* Trading login */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Trading login:</span>
                                <input
                                    className="adm-input"
                                    style={{ flex: 1, height: 22, fontSize: 11 }}
                                    value={draft.login}
                                    onChange={(e) => setDraft({ ...draft, login: e.target.value })}
                                />
                            </div>

                            {/* Password */}
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Password:</span>
                                <input
                                    type="password"
                                    className="adm-input"
                                    style={{ flex: 1, height: 22, fontSize: 11 }}
                                    value={draft.password ?? ''}
                                    onChange={(e) => setDraft({ ...draft, password: e.target.value })}
                                />
                            </div>

                            {/* Advanced Network Settings Toggle */}
                            <div style={{ marginTop: 8, paddingLeft: 115 }}>
                                <button
                                    type="button"
                                    onClick={() => setShowAdvancedNetwork(!showAdvancedNetwork)}
                                    style={{
                                        background: 'none',
                                        border: 'none',
                                        color: 'var(--theia-textLink-foreground, #3794ff)',
                                        cursor: 'pointer',
                                        padding: 0,
                                        fontSize: 11,
                                        display: 'flex',
                                        alignItems: 'center',
                                        gap: 4,
                                    }}
                                >
                                    <i className={`codicon codicon-chevron-${showAdvancedNetwork ? 'down' : 'right'}`} />
                                    <span>Advanced Network Settings</span>
                                </button>
                            </div>

                            {/* Advanced Network Settings Section */}
                            {showAdvancedNetwork && (
                                <div
                                    style={{
                                        borderTop: '1px solid var(--theia-border)',
                                        paddingTop: 10,
                                        marginTop: 4,
                                        display: 'flex',
                                        flexDirection: 'column',
                                        gap: 8,
                                    }}
                                >
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                        <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Gateway server:</span>
                                        <input
                                            className="adm-input"
                                            style={{ flex: 1, height: 22, fontSize: 11 }}
                                            value={draft.advanced_network?.gateway_server ?? ''}
                                            onChange={(e) =>
                                                setDraft({
                                                    ...draft,
                                                    advanced_network: {
                                                        ...draft.advanced_network!,
                                                        gateway_server: e.target.value,
                                                    },
                                                })
                                            }
                                        />
                                    </div>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                        <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Gateway login:</span>
                                        <input
                                            className="adm-input"
                                            style={{ flex: 1, height: 22, fontSize: 11 }}
                                            value={draft.advanced_network?.gateway_login ?? ''}
                                            onChange={(e) =>
                                                setDraft({
                                                    ...draft,
                                                    advanced_network: {
                                                        ...draft.advanced_network!,
                                                        gateway_login: e.target.value,
                                                    },
                                                })
                                            }
                                        />
                                    </div>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                        <span style={{ width: 105, textAlign: 'right', opacity: 0.85, whiteSpace: 'nowrap' }}>Password:</span>
                                        <input
                                            type="password"
                                            className="adm-input"
                                            style={{ flex: 1, height: 22, fontSize: 11 }}
                                            value={draft.advanced_network?.password ?? ''}
                                            onChange={(e) =>
                                                setDraft({
                                                    ...draft,
                                                    advanced_network: {
                                                        ...draft.advanced_network!,
                                                        password: e.target.value,
                                                    },
                                                })
                                            }
                                        />
                                    </div>
                                </div>
                            )}
                        </div>
                    )}

                    {/* ════ TAB 2: GROUPS (gateway_groups.png) ══════════════ */}
                    {tab === 'Groups' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, height: '100%' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <GatewayCylinderIcon />
                                <div style={{ fontSize: 11, lineHeight: 1.4, opacity: 0.9 }}>
                                    Please specify the client groups whose trade operations shall be processed by this gateway. Orders, deals, and positions of clients from these groups will be translated to external trade systems through the gateway.
                                </div>
                            </div>

                            <div style={{ display: 'flex', gap: 10, flex: 1, minHeight: 180, marginTop: 4 }}>
                                {/* Left buttons */}
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 5, width: 75 }}>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() => setGroupDialog({ open: true, isEdit: false, value: 'demo\\*' })}
                                    >
                                        Add
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedGroupIdx === null || !groupsList.length}
                                        onClick={() => {
                                            if (selectedGroupIdx === null || !groupsList[selectedGroupIdx]) return;
                                            setGroupDialog({ open: true, isEdit: true, value: groupsList[selectedGroupIdx] });
                                        }}
                                    >
                                        Edit
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedGroupIdx === null || !groupsList.length}
                                        onClick={() => {
                                            if (selectedGroupIdx === null) return;
                                            const updated = groupsList.filter((_, idx) => idx !== selectedGroupIdx);
                                            setDraft({ ...draft, groups: updated.join(', ') });
                                            setSelectedGroupIdx(updated.length ? 0 : null);
                                        }}
                                    >
                                        Delete
                                    </button>
                                </div>

                                {/* Table */}
                                <div style={{ flex: 1, border: '1px solid var(--theia-border)', borderRadius: 2, overflowY: 'auto' }}>
                                    <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                        <tbody>
                                            {groupsList.length > 0 ? (
                                                groupsList.map((g, idx) => (
                                                    <tr
                                                        key={idx}
                                                        onClick={() => setSelectedGroupIdx(idx)}
                                                        onDoubleClick={() => setGroupDialog({ open: true, isEdit: true, value: g })}
                                                        style={{
                                                            background: selectedGroupIdx === idx ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                            cursor: 'pointer',
                                                        }}
                                                    >
                                                        <td style={{ padding: '6px 10px', display: 'flex', alignItems: 'center', gap: 6 }}>
                                                            <i className="codicon codicon-organization" style={{ color: '#4fc1ff' }} />
                                                            <span>{g}</span>
                                                        </td>
                                                    </tr>
                                                ))
                                            ) : (
                                                <tr>
                                                    <td style={{ padding: '16px', textAlign: 'center', opacity: 0.6 }}>No groups configured</td>
                                                </tr>
                                            )}
                                        </tbody>
                                    </table>
                                </div>
                            </div>

                            <div style={{ marginTop: 6 }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.import_traders_balances}
                                        onChange={(e) => setDraft({ ...draft, import_traders_balances: e.target.checked })}
                                    />
                                    <span>Allow importing traders balances</span>
                                </label>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 3: SYMBOLS (gateway_symbols.png) ════════════ */}
                    {tab === 'Symbols' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, height: '100%' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <GatewayCylinderIcon />
                                <div style={{ fontSize: 11, lineHeight: 1.4, opacity: 0.9 }}>
                                    Please specify the symbols for which the gateway will translate quotes and perform trade operations. The orders, trades and positions for these symbols will be translated through the gateway.
                                </div>
                            </div>

                            <div style={{ display: 'flex', gap: 10, flex: 1, minHeight: 180, marginTop: 4 }}>
                                {/* Left buttons */}
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 5, width: 75 }}>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() => setSymbolDialog({ open: true, isEdit: false, value: '*' })}
                                    >
                                        Add
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedSymbolIdx === null || !symbolsList.length}
                                        onClick={() => {
                                            if (selectedSymbolIdx === null || !symbolsList[selectedSymbolIdx]) return;
                                            setSymbolDialog({ open: true, isEdit: true, value: symbolsList[selectedSymbolIdx] });
                                        }}
                                    >
                                        Edit
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedSymbolIdx === null || !symbolsList.length}
                                        onClick={() => {
                                            if (selectedSymbolIdx === null) return;
                                            const updated = symbolsList.filter((_, idx) => idx !== selectedSymbolIdx);
                                            setDraft({ ...draft, symbols: updated.join(', ') });
                                            setSelectedSymbolIdx(updated.length ? 0 : null);
                                        }}
                                    >
                                        Delete
                                    </button>
                                </div>

                                {/* Table */}
                                <div style={{ flex: 1, border: '1px solid var(--theia-border)', borderRadius: 2, overflowY: 'auto' }}>
                                    <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                        <tbody>
                                            {symbolsList.length > 0 ? (
                                                symbolsList.map((s, idx) => (
                                                    <tr
                                                        key={idx}
                                                        onClick={() => setSelectedSymbolIdx(idx)}
                                                        onDoubleClick={() => setSymbolDialog({ open: true, isEdit: true, value: s })}
                                                        style={{
                                                            background: selectedSymbolIdx === idx ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                            cursor: 'pointer',
                                                        }}
                                                    >
                                                        <td style={{ padding: '6px 10px', display: 'flex', alignItems: 'center', gap: 6 }}>
                                                            <i className="codicon codicon-symbol-class" style={{ color: '#e5c07b' }} />
                                                            <span>{s}</span>
                                                        </td>
                                                    </tr>
                                                ))
                                            ) : (
                                                <tr>
                                                    <td style={{ padding: '16px', textAlign: 'center', opacity: 0.6 }}>No symbols configured</td>
                                                </tr>
                                            )}
                                        </tbody>
                                    </table>
                                </div>
                            </div>

                            <div style={{ marginTop: 6 }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.import_symbol_settings}
                                        onChange={(e) => setDraft({ ...draft, import_symbol_settings: e.target.checked })}
                                    />
                                    <span>Allow to import symbol settings</span>
                                </label>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 4: TRANSLATIONS (gateway_translation.png) ═══ */}
                    {tab === 'Translations' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, height: '100%' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <GatewayCylinderIcon />
                                <div style={{ fontSize: 11, lineHeight: 1.4, opacity: 0.9 }}>
                                    If necessary, please specify parameters for converting data transmitted through the gateway: name of the source symbol in the external system and value of correction of incoming prices. If any of the parameters is not set, its source values will be used.
                                </div>
                            </div>

                            <div style={{ display: 'flex', gap: 10, flex: 1, minHeight: 200, marginTop: 4 }}>
                                {/* Left buttons */}
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 5, width: 75 }}>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedTransIdx === null || selectedTransIdx <= 0}
                                        onClick={() => {
                                            if (selectedTransIdx === null || selectedTransIdx <= 0) return;
                                            const items = [...(draft.translations ?? [])];
                                            const tmp = items[selectedTransIdx];
                                            items[selectedTransIdx] = items[selectedTransIdx - 1];
                                            items[selectedTransIdx - 1] = tmp;
                                            setDraft({ ...draft, translations: items });
                                            setSelectedTransIdx(selectedTransIdx - 1);
                                        }}
                                    >
                                        Up
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedTransIdx === null || selectedTransIdx >= (draft.translations?.length ?? 1) - 1}
                                        onClick={() => {
                                            if (selectedTransIdx === null || selectedTransIdx >= (draft.translations?.length ?? 0) - 1) return;
                                            const items = [...(draft.translations ?? [])];
                                            const tmp = items[selectedTransIdx];
                                            items[selectedTransIdx] = items[selectedTransIdx + 1];
                                            items[selectedTransIdx + 1] = tmp;
                                            setDraft({ ...draft, translations: items });
                                            setSelectedTransIdx(selectedTransIdx + 1);
                                        }}
                                    >
                                        Down
                                    </button>

                                    <div style={{ height: 16 }} />

                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() =>
                                            setTransDialog({
                                                open: true,
                                                isEdit: false,
                                                item: { symbol: 'EURUSD', source: 'EUR/USD', bid: -1, ask: 1 },
                                            })
                                        }
                                    >
                                        Add
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedTransIdx === null || !draft.translations?.length}
                                        onClick={() => {
                                            if (selectedTransIdx === null || !draft.translations?.[selectedTransIdx]) return;
                                            setTransDialog({
                                                open: true,
                                                isEdit: true,
                                                item: draft.translations[selectedTransIdx],
                                            });
                                        }}
                                    >
                                        Edit
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedTransIdx === null || !draft.translations?.length}
                                        onClick={() => {
                                            if (selectedTransIdx === null) return;
                                            const items = (draft.translations ?? []).filter((_, i) => i !== selectedTransIdx);
                                            setDraft({ ...draft, translations: items });
                                            setSelectedTransIdx(items.length ? 0 : null);
                                        }}
                                    >
                                        Delete
                                    </button>
                                </div>

                                {/* Table */}
                                <div style={{ flex: 1, border: '1px solid var(--theia-border)', borderRadius: 2, overflowY: 'auto' }}>
                                    <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                        <thead>
                                            <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                                                <th style={{ padding: '4px 8px', width: 140, borderRight: '1px solid var(--theia-border)' }}>Symbol</th>
                                                <th style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>Source</th>
                                                <th style={{ padding: '4px 8px', width: 60, textAlign: 'right', borderRight: '1px solid var(--theia-border)' }}>Bid</th>
                                                <th style={{ padding: '4px 8px', width: 60, textAlign: 'right' }}>Ask</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {(draft.translations ?? []).map((t, idx) => (
                                                <tr
                                                    key={idx}
                                                    onClick={() => setSelectedTransIdx(idx)}
                                                    onDoubleClick={() =>
                                                        setTransDialog({
                                                            open: true,
                                                            isEdit: true,
                                                            item: t,
                                                        })
                                                    }
                                                    style={{
                                                        background: selectedTransIdx === idx ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                        cursor: 'pointer',
                                                    }}
                                                >
                                                    <td style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>
                                                        <i className="codicon codicon-symbol-class" style={{ color: '#e5c07b', marginRight: 4 }} />
                                                        {t.symbol}
                                                    </td>
                                                    <td style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>{t.source || '—'}</td>
                                                    <td style={{ padding: '4px 8px', textAlign: 'right', borderRight: '1px solid var(--theia-border)' }}>{t.bid}</td>
                                                    <td style={{ padding: '4px 8px', textAlign: 'right' }}>{t.ask}</td>
                                                </tr>
                                            ))}
                                            {(!draft.translations || draft.translations.length === 0) && (
                                                <tr>
                                                    <td colSpan={4} style={{ padding: '16px', textAlign: 'center', opacity: 0.6 }}>No translations defined</td>
                                                </tr>
                                            )}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 5: PARAMETERS (gateway_parameters.png) ═════ */}
                    {tab === 'Parameters' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, height: '100%' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <GatewayCylinderIcon />
                                <div style={{ fontSize: 11, lineHeight: 1.4, opacity: 0.9 }}>
                                    Please specify parameters of the gateway. These parameters are specific for each type of gateway. They allow using additional settings that were not available in the "Common" tab.
                                </div>
                            </div>

                            <div style={{ display: 'flex', gap: 10, flex: 1, minHeight: 200, marginTop: 4 }}>
                                {/* Left buttons */}
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 5, width: 75 }}>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedParamIdx === null || selectedParamIdx <= 0}
                                        onClick={() => {
                                            if (selectedParamIdx === null || selectedParamIdx <= 0) return;
                                            const items = [...(draft.parameters ?? [])];
                                            const tmp = items[selectedParamIdx];
                                            items[selectedParamIdx] = items[selectedParamIdx - 1];
                                            items[selectedParamIdx - 1] = tmp;
                                            setDraft({ ...draft, parameters: items });
                                            setSelectedParamIdx(selectedParamIdx - 1);
                                        }}
                                    >
                                        Up
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedParamIdx === null || selectedParamIdx >= (draft.parameters?.length ?? 1) - 1}
                                        onClick={() => {
                                            if (selectedParamIdx === null || selectedParamIdx >= (draft.parameters?.length ?? 0) - 1) return;
                                            const items = [...(draft.parameters ?? [])];
                                            const tmp = items[selectedParamIdx];
                                            items[selectedParamIdx] = items[selectedParamIdx + 1];
                                            items[selectedParamIdx + 1] = tmp;
                                            setDraft({ ...draft, parameters: items });
                                            setSelectedParamIdx(selectedParamIdx + 1);
                                        }}
                                    >
                                        Down
                                    </button>

                                    <div style={{ height: 16 }} />

                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() =>
                                            setParamDialog({
                                                open: true,
                                                isEdit: false,
                                                item: { parameter: '', value: '' },
                                            })
                                        }
                                    >
                                        Add
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedParamIdx === null || !draft.parameters?.length}
                                        onClick={() => {
                                            if (selectedParamIdx === null || !draft.parameters?.[selectedParamIdx]) return;
                                            setParamDialog({
                                                open: true,
                                                isEdit: true,
                                                item: draft.parameters[selectedParamIdx],
                                            });
                                        }}
                                    >
                                        Edit
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        disabled={selectedParamIdx === null || !draft.parameters?.length}
                                        onClick={() => {
                                            if (selectedParamIdx === null) return;
                                            const items = (draft.parameters ?? []).filter((_, i) => i !== selectedParamIdx);
                                            setDraft({ ...draft, parameters: items });
                                            setSelectedParamIdx(items.length ? 0 : null);
                                        }}
                                    >
                                        Delete
                                    </button>
                                    <button
                                        type="button"
                                        className="wb-btn secondary"
                                        style={{ height: 22, fontSize: 11 }}
                                        onClick={() => {
                                            setDraft({
                                                ...draft,
                                                parameters: [
                                                    { parameter: 'Trading Calendar Holidays', value: '' },
                                                    { parameter: 'Max Price Deviation', value: '50' },
                                                    { parameter: 'Limit Orders Coverage Mode', value: 'Market' },
                                                    { parameter: 'Quotes Time Original', value: 'No' },
                                                    { parameter: 'Last Price Markup', value: 'Yes' },
                                                    { parameter: 'Symbols Path', value: '' },
                                                    { parameter: 'Symbols Update', value: 'No' },
                                                    { parameter: 'Calculate Hedged Margin', value: 'No' },
                                                    { parameter: 'Calculate Hedged Margin ...', value: '2.0' },
                                                    { parameter: 'News Enable', value: 'No' },
                                                ],
                                            });
                                        }}
                                    >
                                        Default
                                    </button>
                                </div>

                                {/* Table */}
                                <div style={{ flex: 1, border: '1px solid var(--theia-border)', borderRadius: 2, overflowY: 'auto' }}>
                                    <table className="adm-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: 11 }}>
                                        <thead>
                                            <tr style={{ background: 'var(--theia-sideBarSectionHeader-background)', textAlign: 'left' }}>
                                                <th style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>Parameter</th>
                                                <th style={{ padding: '4px 8px' }}>Value</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {(draft.parameters ?? []).map((p, idx) => (
                                                <tr
                                                    key={idx}
                                                    onClick={() => setSelectedParamIdx(idx)}
                                                    onDoubleClick={() =>
                                                        setParamDialog({
                                                            open: true,
                                                            isEdit: true,
                                                            item: p,
                                                        })
                                                    }
                                                    style={{
                                                        background: selectedParamIdx === idx ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                        cursor: 'pointer',
                                                    }}
                                                >
                                                    <td style={{ padding: '4px 8px', borderRight: '1px solid var(--theia-border)' }}>
                                                        <span style={{ color: '#4fc1ff', marginRight: 4 }}>ab</span>
                                                        {p.parameter}
                                                    </td>
                                                    <td style={{ padding: '4px 8px' }}>{p.value}</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 6: TIMEOUTS (gateway_timeouts.png) ═════════ */}
                    {tab === 'Timeouts' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <GatewayCylinderIcon />
                                <div style={{ fontSize: 11, lineHeight: 1.4, opacity: 0.9 }}>
                                    Please set up gateway timeout parameters for connection errors. These parameters allow quick restoring of a lost network connection and limiting the frequency of reconnections in case of continuous network problems.
                                </div>
                            </div>

                            <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 8, paddingLeft: 30 }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                    <span style={{ width: 220, textAlign: 'right', opacity: 0.85 }}>Interval between reconnections:</span>
                                    <input
                                        className="adm-input"
                                        type="number"
                                        style={{ width: 75, height: 22, fontSize: 11 }}
                                        value={draft.timeouts?.reconnect_interval ?? 1}
                                        onChange={(e) =>
                                            setDraft({
                                                ...draft,
                                                timeouts: { ...draft.timeouts!, reconnect_interval: Number(e.target.value) },
                                            })
                                        }
                                    />
                                    <span>seconds</span>
                                </div>

                                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                    <span style={{ width: 220, textAlign: 'right', opacity: 0.85 }}>Number of reconnection attempts:</span>
                                    <input
                                        className="adm-input"
                                        type="number"
                                        style={{ width: 75, height: 22, fontSize: 11 }}
                                        value={draft.timeouts?.reconnect_attempts ?? 5}
                                        onChange={(e) =>
                                            setDraft({
                                                ...draft,
                                                timeouts: { ...draft.timeouts!, reconnect_attempts: Number(e.target.value) },
                                            })
                                        }
                                    />
                                </div>

                                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                    <span style={{ width: 220, textAlign: 'right', opacity: 0.85 }}>Interval between series of reconnections:</span>
                                    <input
                                        className="adm-input"
                                        type="number"
                                        style={{ width: 75, height: 22, fontSize: 11 }}
                                        value={draft.timeouts?.reconnect_series_interval ?? 60}
                                        onChange={(e) =>
                                            setDraft({
                                                ...draft,
                                                timeouts: { ...draft.timeouts!, reconnect_series_interval: Number(e.target.value) },
                                            })
                                        }
                                    />
                                    <span>seconds</span>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* ════ TAB 7: MONITORING (gateway_monitoring.png) ═════ */}
                    {tab === 'Monitoring' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <GatewayCylinderIcon />
                                <div style={{ fontSize: 11, lineHeight: 1.4, opacity: 0.9 }}>
                                    Use monitoring parameters for additional control and troubleshooting. Don't keep detailed profiling always on, as this may slow down trade request processing.
                                </div>
                            </div>

                            <div style={{ display: 'flex', flexDirection: 'column', gap: 12, marginTop: 8, paddingLeft: 54 }}>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.monitoring?.enable_logging}
                                        onChange={(e) =>
                                            setDraft({
                                                ...draft,
                                                monitoring: { ...draft.monitoring!, enable_logging: e.target.checked },
                                            })
                                        }
                                    />
                                    <span>Enable trading operations logging</span>
                                </label>

                                <label style={{ display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer' }}>
                                    <input
                                        type="checkbox"
                                        checked={draft.monitoring?.enable_profiling}
                                        onChange={(e) =>
                                            setDraft({
                                                ...draft,
                                                monitoring: { ...draft.monitoring!, enable_profiling: e.target.checked },
                                            })
                                        }
                                    />
                                    <span>Enable detailed profiling</span>
                                </label>

                                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                    <span style={{ opacity: 0.85 }}>Collect transactions for</span>
                                    <input
                                        className="adm-input"
                                        type="number"
                                        style={{ width: 60, height: 22, fontSize: 11 }}
                                        value={draft.monitoring?.collect_days ?? 0}
                                        onChange={(e) =>
                                            setDraft({
                                                ...draft,
                                                monitoring: { ...draft.monitoring!, collect_days: Number(e.target.value) },
                                            })
                                        }
                                    />
                                    <span>days</span>
                                </div>
                            </div>
                        </div>
                    )}
                </div>

                {/* ── Footer ────────────────────────────────────────────── */}
                <div
                    style={{
                        padding: '8px 14px',
                        borderTop: '1px solid var(--theia-border)',
                        background: 'var(--theia-editorGroupHeader-tabsBackground)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'flex-end',
                        gap: 8,
                        flexShrink: 0,
                    }}
                >
                    <button
                        type="button"
                        className="wb-btn primary"
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
                        onClick={() => setShowHelpDialog(true)}
                    >
                        Help
                    </button>
                </div>

                {/* ════ MT5 Sub-Dialog Modals (No browser prompts!) ════════════ */}

                {/* Translation Sub-Dialog */}
                {transDialog?.open && (
                    <TranslationSubDialog
                        initial={transDialog.item}
                        onClose={() => setTransDialog(null)}
                        onSave={(item) => {
                            if (transDialog.isEdit && selectedTransIdx !== null) {
                                const items = [...(draft.translations ?? [])];
                                items[selectedTransIdx] = item;
                                setDraft({ ...draft, translations: items });
                            } else {
                                setDraft({
                                    ...draft,
                                    translations: [...(draft.translations ?? []), item],
                                });
                                setSelectedTransIdx((draft.translations?.length ?? 0));
                            }
                            setTransDialog(null);
                        }}
                    />
                )}

                {/* Group Sub-Dialog */}
                {groupDialog?.open && (
                    <GroupSubDialog
                        initial={groupDialog.value}
                        onClose={() => setGroupDialog(null)}
                        onSave={(group) => {
                            if (groupDialog.isEdit && selectedGroupIdx !== null) {
                                const updated = [...groupsList];
                                updated[selectedGroupIdx] = group;
                                setDraft({ ...draft, groups: updated.join(', ') });
                            } else {
                                const updated = [...groupsList, group];
                                setDraft({ ...draft, groups: updated.join(', ') });
                                setSelectedGroupIdx(updated.length - 1);
                            }
                            setGroupDialog(null);
                        }}
                    />
                )}

                {/* Symbol Sub-Dialog */}
                {symbolDialog?.open && (
                    <SymbolSubDialog
                        initial={symbolDialog.value}
                        onClose={() => setSymbolDialog(null)}
                        onSave={(symbol) => {
                            if (symbolDialog.isEdit && selectedSymbolIdx !== null) {
                                const updated = [...symbolsList];
                                updated[selectedSymbolIdx] = symbol;
                                setDraft({ ...draft, symbols: updated.join(', ') });
                            } else {
                                const updated = [...symbolsList, symbol];
                                setDraft({ ...draft, symbols: updated.join(', ') });
                                setSelectedSymbolIdx(updated.length - 1);
                            }
                            setSymbolDialog(null);
                        }}
                    />
                )}

                {/* Parameter Sub-Dialog */}
                {paramDialog?.open && (
                    <ParameterSubDialog
                        initial={paramDialog.item}
                        onClose={() => setParamDialog(null)}
                        onSave={(param) => {
                            if (paramDialog.isEdit && selectedParamIdx !== null) {
                                const items = [...(draft.parameters ?? [])];
                                items[selectedParamIdx] = param;
                                setDraft({ ...draft, parameters: items });
                            } else {
                                setDraft({
                                    ...draft,
                                    parameters: [...(draft.parameters ?? []), param],
                                });
                                setSelectedParamIdx(draft.parameters?.length ?? 0);
                            }
                            setParamDialog(null);
                        }}
                    />
                )}

                {/* Help Sub-Dialog */}
                {showHelpDialog && (
                    <GatewayHelpDialog onClose={() => setShowHelpDialog(false)} />
                )}
            </div>
        </FloatingWindow>
    );
}

export default GatewayConfigModal;
