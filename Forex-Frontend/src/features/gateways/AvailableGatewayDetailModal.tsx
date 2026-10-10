import * as React from 'react';

export interface AvailableGatewayModule {
    id: string;
    name: string;
    moduleFile: string;
    vendor: string;
    version: string;
    protocol: string;
    defaultPort: number;
    description: string;
    supportedModes: ('Trade and Quotes' | 'Trade Only' | 'Quotes Only')[];
    features: string[];
    category: 'ECN / Interbank' | 'Liquidity Bridge' | 'Crypto Exchange' | 'Multi-Asset' | 'Remote Service';
}

export const AVAILABLE_GATEWAY_MODULES: AvailableGatewayModule[] = [
    {
        id: 'currenex',
        name: 'Currenex Gateway',
        moduleFile: 'MT5GatewayCurrenex.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4260',
        protocol: 'FIX 4.4 / Currenex ITCH API',
        defaultPort: 16387,
        category: 'ECN / Interbank',
        description:
            'High-speed direct access to Currenex FX trading engine. Supports real-time depth of market (Level 2), streaming quotes, full trade execution lifecycle, STP/ECN routing, and trade balance reconciliation.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Level 2 Market Depth (Depth of Market)',
            'Sub-millisecond Streaming Quotes',
            'Full Order Lifecycle (IOC, FOK, GTC, Stop, Limit)',
            'Automatic Balance Reconciliation',
            'Real-time Symbol Settings Synchronization',
        ],
    },
    {
        id: 'integral',
        name: 'Integral FX Grid Gateway',
        moduleFile: 'MT5GatewayIntegral.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4260',
        protocol: 'FIX 4.4 / Integral FX Inside',
        defaultPort: 16388,
        category: 'ECN / Interbank',
        description:
            'Turnkey connectivity to the Integral FX Grid network. Delivers consolidated institutional multi-bank pricing, algorithmic routing, fast trade confirmations, and automatic symbol translation.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Aggregated Multi-Bank Pricing Stream',
            'Low-Latency FIX Execution Engine',
            'Flexible Price/Spread Markup Translations',
            'Asynchronous Trade Confirmations',
            'Customizable Group Allocations',
        ],
    },
    {
        id: 'lmax',
        name: 'LMAX Exchange Gateway',
        moduleFile: 'MT5GatewayLMAX.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4255',
        protocol: 'FIX 4.4 / LMAX FIX Protocol',
        defaultPort: 16389,
        category: 'ECN / Interbank',
        description:
            'Direct execution venue connectivity to LMAX Exchange MTF. Offers strictly exchange-quality execution with complete pre- and post-trade transparency, depth of book, and strict price-time priority.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Exchange-Quality Central Limit Order Book (CLOB)',
            'Strict Price-Time Priority Execution',
            'Microsecond Quote Dispatching',
            'Complete Order Fill History and Partial Fills',
            'Auto Reconnect & Failover Handling',
        ],
    },
    {
        id: 'cboe',
        name: 'Cboe FX Gateway (Hotspot)',
        moduleFile: 'MT5GatewayCboeFX.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4250',
        protocol: 'FIX 4.2 / 4.4 ITCH',
        defaultPort: 16390,
        category: 'ECN / Interbank',
        description:
            'Integrated connector for Cboe FX (formerly Hotspot FX). Enables direct interbank quote feeds, anonymous and bilateral trading models, with institutional liquidity distribution.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Anonymous & Disclosed Trading Pools',
            'Deep Liquidity Order Book Feed',
            'Instant STP Trade Execution',
            'Comprehensive Fill Monitoring & Latency Stats',
        ],
    },
    {
        id: 'fastmatch',
        name: 'Euronext FX (FastMatch) Gateway',
        moduleFile: 'MT5GatewayFastMatch.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4240',
        protocol: 'FastMatch FIX Protocol / Binary Feed',
        defaultPort: 16391,
        category: 'ECN / Interbank',
        description:
            'Ultra-fast gateway for Euronext FX / FastMatch matching engine. Optimized for institutional HFT and quantitative flow with high tick volume handling.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Ultra-Low Latency Execution Engine',
            'High-Frequency Quote Ingestion',
            'Flexible Matching Engine Rule Sets',
            'Symbol Mapping & Pricing Multipliers',
        ],
    },
    {
        id: 'primexm',
        name: 'PrimeXM XCore Gateway',
        moduleFile: 'MT5GatewayPrimeXM.dll',
        vendor: 'PrimeXM / MetaQuotes',
        version: '5.00 build 4190',
        protocol: 'PrimeXM XCore Proprietary / FIX',
        defaultPort: 16392,
        category: 'Liquidity Bridge',
        description:
            'Direct bridge interface into PrimeXM XCore aggregation engine. Connects to dozens of Tier-1 banks, non-bank liquidity providers, and crypto liquidity pools.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Multi-Asset Aggregation Feed',
            'Dynamic Order Routing Rules',
            'Advanced Slippage & Spread Controls',
            'Live Latency Tracking and Queue Diagnostics',
        ],
    },
    {
        id: 'onezero',
        name: 'oneZero EcoSystem Hub Gateway',
        moduleFile: 'MT5GatewayOneZero.dll',
        vendor: 'oneZero Financial Systems',
        version: '5.00 build 4185',
        protocol: 'oneZero Hub Protocol / FIX 4.4',
        defaultPort: 16393,
        category: 'Liquidity Bridge',
        description:
            'Integration connector for oneZero Financial Systems Hub. Offers institutional liquidity routing, risk aggregation, and real-time trade monitoring.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'oneZero Hub Connectivity',
            'Automated B-Book / A-Book Hedging Synchronization',
            'Level 2 Market Depth Support',
            'Configurable Reconnect Timeouts and Heartbeats',
        ],
    },
    {
        id: 'b2broker',
        name: 'B2Broker MarksMan Gateway',
        moduleFile: 'MT5GatewayB2Broker.dll',
        vendor: 'B2Broker / MetaQuotes',
        version: '5.00 build 4210',
        protocol: 'FIX 4.4 / REST WebSocket',
        defaultPort: 16394,
        category: 'Liquidity Bridge',
        description:
            'Connects MetaTrader 5 server directly to B2Broker MarksMan liquidity hub, supplying spot FX, metals, indices, commodities, and 100+ crypto pairs.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Crypto, FX & CFD Unified Feeds',
            'Deep Multi-Layer Order Book',
            'Auto Margin & Balance Synchronization',
            'Built-in Reconnection Protection',
        ],
    },
    {
        id: 'binance',
        name: 'Binance Digital Assets Gateway',
        moduleFile: 'MT5GatewayBinance.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4160',
        protocol: 'FIX 4.4 / Binance WebSocket API',
        defaultPort: 16395,
        category: 'Crypto Exchange',
        description:
            'Integration module for digital asset trading on Binance Spot and USD-M Futures. Receives tick feeds, order books, and dispatches trading orders with sub-second acknowledgement.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            '24/7 Digital Asset Trading & Quotes',
            'Spot and Perpetual Futures Markets',
            'Order Book Level 2 Stream',
            'Automatic Symbol Spec Import',
        ],
    },
    {
        id: 'interactive_brokers',
        name: 'Interactive Brokers Gateway',
        moduleFile: 'MT5GatewayIB.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4140',
        protocol: 'IB TWS / FIX Gateway API',
        defaultPort: 16396,
        category: 'Multi-Asset',
        description:
            'Provides direct trading and market data forwarding to Interactive Brokers exchange network across global equities, options, futures, and currencies.',
        supportedModes: ['Trade and Quotes', 'Trade Only', 'Quotes Only'],
        features: [
            'Global Exchange Access (US, EU, APAC)',
            'Multi-Asset Class Execution',
            'Smart Routing Support',
            'End-of-day Position & Balance Reconciliation',
        ],
    },
    {
        id: 'remote_service',
        name: 'Remote Service Gateway Module',
        moduleFile: 'MT5GatewayRemote.dll',
        vendor: 'MetaQuotes Software Corp.',
        version: '5.00 build 4260',
        protocol: 'MT5 APIGateway Inter-Process RPC',
        defaultPort: 16380,
        category: 'Remote Service',
        description:
            'Enables running gateways as standalone Windows services on dedicated hardware or outside DMZ network clusters. History and trade servers connect via secure TCP/IP tunnel.',
        supportedModes: ['Trade and Quotes', 'Trade Only'],
        features: [
            'Standalone Background Service Architecture',
            'DMZ / Firewall Tunneling Support',
            'Zero Impact on History Server CPU',
            'Independent Restart and Crash Recovery',
        ],
    },
];

export interface AvailableGatewayDetailModalProps {
    module: AvailableGatewayModule;
    onClose: () => void;
    onAddGateway: (module: AvailableGatewayModule) => void;
}

export function AvailableGatewayDetailModal({
    module,
    onClose,
    onAddGateway,
}: AvailableGatewayDetailModalProps): React.ReactElement {
    const [dragging, setDragging] = React.useState(false);
    const [position, setPosition] = React.useState<{ x: number; y: number } | null>(null);
    const dragStartRef = React.useRef<{ mouseX: number; mouseY: number; startX: number; startY: number } | null>(null);

    const handleMouseDown = (e: React.MouseEvent) => {
        const modal = (e.currentTarget as HTMLElement).closest('.adm-modal') as HTMLElement | null;
        if (!modal) return;
        const rect = modal.getBoundingClientRect();
        dragStartRef.current = {
            mouseX: e.clientX,
            mouseY: e.clientY,
            startX: position ? position.x : rect.left,
            startY: position ? position.y : rect.top,
        };
        setDragging(true);
    };

    React.useEffect(() => {
        if (!dragging) return;
        const handleMouseMove = (e: MouseEvent) => {
            if (!dragStartRef.current) return;
            const dx = e.clientX - dragStartRef.current.mouseX;
            const dy = e.clientY - dragStartRef.current.mouseY;
            setPosition({
                x: Math.max(10, dragStartRef.current.startX + dx),
                y: Math.max(10, dragStartRef.current.startY + dy),
            });
        };
        const handleMouseUp = () => {
            setDragging(false);
            dragStartRef.current = null;
        };
        window.addEventListener('mousemove', handleMouseMove);
        window.addEventListener('mouseup', handleMouseUp);
        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
            window.removeEventListener('mouseup', handleMouseUp);
        };
    }, [dragging]);

    return (
        <div className="adm-modal-overlay" onClick={onClose} style={{ zIndex: 2100 }}>
            <div
                className="adm-modal"
                style={{
                    width: 720,
                    maxWidth: '95vw',
                    maxHeight: '90vh',
                    position: position ? 'fixed' : 'relative',
                    left: position ? position.x : undefined,
                    top: position ? position.y : undefined,
                    transform: position ? 'none' : undefined,
                    display: 'flex',
                    flexDirection: 'column',
                }}
                onClick={(e) => e.stopPropagation()}
            >
                {/* Header */}
                <div
                    className="adm-modal-header"
                    onMouseDown={handleMouseDown}
                    style={{ cursor: 'move', userSelect: 'none', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}
                >
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        {/* Gateway Yellow Cylinder Icon */}
                        <svg width="18" height="18" viewBox="0 0 16 16" fill="none">
                            <ellipse cx="8" cy="4" rx="6" ry="2.5" fill="#f6c344" stroke="#d99b1a" strokeWidth="1" />
                            <path d="M2 4v8c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V4" fill="#f9d368" stroke="#d99b1a" strokeWidth="1" />
                            <ellipse cx="8" cy="8" rx="6" ry="2" stroke="#d99b1a" strokeWidth="0.8" fill="none" opacity="0.6" />
                        </svg>
                        <span style={{ fontWeight: 600, fontSize: 13, color: 'var(--theia-ui-typography-color-heading, #e6edf3)' }}>
                            Gateway Module Specification: {module.name}
                        </span>
                    </div>
                    <button
                        type="button"
                        onClick={onClose}
                        className="adm-modal-close"
                        style={{ background: 'transparent', border: 'none', color: '#8b949e', cursor: 'pointer', fontSize: 16 }}
                    >
                        ×
                    </button>
                </div>

                {/* Body */}
                <div
                    className="adm-modal-body"
                    style={{
                        padding: 18,
                        overflowY: 'auto',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: 16,
                        color: 'var(--theia-foreground, #ccc)',
                        fontSize: 12,
                    }}
                >
                    {/* Top Hero Banner */}
                    <div
                        style={{
                            display: 'flex',
                            gap: 16,
                            padding: 14,
                            background: 'rgba(255, 255, 255, 0.03)',
                            border: '1px solid var(--theia-border, #333)',
                            borderRadius: 4,
                        }}
                    >
                        <div
                            style={{
                                width: 54,
                                height: 54,
                                borderRadius: 6,
                                background: 'linear-gradient(135deg, rgba(246, 195, 68, 0.15), rgba(246, 195, 68, 0.05))',
                                border: '1px solid rgba(246, 195, 68, 0.3)',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                flexShrink: 0,
                            }}
                        >
                            <svg width="32" height="32" viewBox="0 0 16 16" fill="none">
                                <ellipse cx="8" cy="4" rx="6" ry="2.5" fill="#f6c344" stroke="#d99b1a" strokeWidth="1" />
                                <path d="M2 4v8c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V4" fill="#f9d368" stroke="#d99b1a" strokeWidth="1" />
                                <ellipse cx="8" cy="8" rx="6" ry="2" stroke="#d99b1a" strokeWidth="0.8" fill="none" opacity="0.6" />
                            </svg>
                        </div>
                        <div style={{ flex: 1 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
                                <h3 style={{ margin: 0, fontSize: 15, fontWeight: 600, color: '#e6edf3' }}>{module.name}</h3>
                                <span
                                    style={{
                                        fontSize: 10,
                                        padding: '2px 6px',
                                        borderRadius: 3,
                                        background: 'rgba(56, 139, 253, 0.15)',
                                        color: '#58a6ff',
                                        border: '1px solid rgba(56, 139, 253, 0.3)',
                                    }}
                                >
                                    {module.category}
                                </span>
                            </div>
                            <div style={{ color: '#8b949e', fontSize: 11, marginBottom: 6 }}>
                                <span>Binary: <strong style={{ color: '#e6edf3' }}>{module.moduleFile}</strong></span>
                                <span style={{ margin: '0 8px' }}>•</span>
                                <span>Version: {module.version}</span>
                                <span style={{ margin: '0 8px' }}>•</span>
                                <span>Vendor: {module.vendor}</span>
                            </div>
                            <div style={{ lineHeight: 1.5, color: '#ccc' }}>{module.description}</div>
                        </div>
                    </div>

                    {/* Technical Specifications Grid */}
                    <div style={{ border: '1px solid var(--theia-border, #333)', borderRadius: 4, overflow: 'hidden' }}>
                        <div
                            style={{
                                padding: '7px 12px',
                                background: 'rgba(255, 255, 255, 0.04)',
                                borderBottom: '1px solid var(--theia-border, #333)',
                                fontWeight: 600,
                                fontSize: 11,
                                textTransform: 'uppercase',
                                letterSpacing: 0.5,
                                color: '#e6edf3',
                            }}
                        >
                            Technical Specifications & Architecture
                        </div>
                        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 12 }}>
                            <tbody>
                                <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                                    <td style={{ padding: '8px 12px', width: 170, color: '#8b949e' }}>Module Library</td>
                                    <td style={{ padding: '8px 12px', color: '#e6edf3', fontFamily: 'monospace' }}>
                                        /gateways/{module.moduleFile}
                                    </td>
                                </tr>
                                <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                                    <td style={{ padding: '8px 12px', color: '#8b949e' }}>Protocol / Standard</td>
                                    <td style={{ padding: '8px 12px', color: '#e6edf3' }}>{module.protocol}</td>
                                </tr>
                                <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                                    <td style={{ padding: '8px 12px', color: '#8b949e' }}>Default History Port</td>
                                    <td style={{ padding: '8px 12px', color: '#e6edf3' }}>{module.defaultPort} (TCP/IP)</td>
                                </tr>
                                <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                                    <td style={{ padding: '8px 12px', color: '#8b949e' }}>Supported Operating Modes</td>
                                    <td style={{ padding: '8px 12px', color: '#e6edf3' }}>
                                        {module.supportedModes.join(', ')}
                                    </td>
                                </tr>
                                <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                                    <td style={{ padding: '8px 12px', color: '#8b949e' }}>Platform Interface</td>
                                    <td style={{ padding: '8px 12px', color: '#e6edf3' }}>
                                        MT5APIGateway.dll v5.00 Native C++ API
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    {/* Supported Capabilities */}
                    <div style={{ border: '1px solid var(--theia-border, #333)', borderRadius: 4, padding: 12 }}>
                        <div style={{ fontWeight: 600, fontSize: 11, marginBottom: 8, color: '#e6edf3' }}>
                            SUPPORTED PLATFORM CAPABILITIES
                        </div>
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 8 }}>
                            {module.features.map((feat, idx) => (
                                <div key={idx} style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11 }}>
                                    <i className="codicon codicon-check" style={{ color: '#89d185' }} />
                                    <span>{feat}</span>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Operational Note */}
                    <div
                        style={{
                            padding: 10,
                            borderRadius: 4,
                            background: 'rgba(56, 139, 253, 0.08)',
                            border: '1px solid rgba(56, 139, 253, 0.2)',
                            fontSize: 11,
                            color: '#90bdf4',
                            display: 'flex',
                            gap: 8,
                            alignItems: 'flex-start',
                        }}
                    >
                        <i className="codicon codicon-info" style={{ marginTop: 2, flexShrink: 0 }} />
                        <span>
                            Click <strong>Add Gateway...</strong> to configure connection credentials, groups, symbol mappings,
                            price translations, and timeouts for this module. Multiple active configurations of this module can run concurrently.
                        </span>
                    </div>
                </div>

                {/* Footer Buttons */}
                <div
                    className="adm-modal-footer"
                    style={{
                        padding: '12px 18px',
                        borderTop: '1px solid var(--theia-border, #333)',
                        display: 'flex',
                        justifyContent: 'flex-end',
                        gap: 10,
                        background: 'rgba(0, 0, 0, 0.2)',
                    }}
                >
                    <button
                        type="button"
                        className="adm-btn adm-btn-primary"
                        onClick={() => {
                            onClose();
                            onAddGateway(module);
                        }}
                        style={{
                            display: 'flex',
                            alignItems: 'center',
                            gap: 6,
                            padding: '6px 16px',
                            fontWeight: 600,
                        }}
                    >
                        <i className="codicon codicon-add" />
                        Add Gateway...
                    </button>
                    <button
                        type="button"
                        className="adm-btn adm-btn-secondary"
                        onClick={onClose}
                        style={{ padding: '6px 16px' }}
                    >
                        Close
                    </button>
                </div>
            </div>
        </div>
    );
}
