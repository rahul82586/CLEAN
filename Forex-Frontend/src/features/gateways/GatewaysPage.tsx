import * as React from 'react';
import { API, isBackendGap } from '../../services/api';
import { GatewayConfigModal, GatewayRecord } from './GatewayConfigModal';
import {
    AvailableGatewayDetailModal,
    AvailableGatewayModule,
    AVAILABLE_GATEWAY_MODULES,
} from './AvailableGatewayDetailModal';
import { GatewaysContextMenu } from './GatewaysContextMenu';

export interface GatewaysPageProps {
    selectedGatewayId?: number | string;
}

export function GatewaysPage({ selectedGatewayId }: GatewaysPageProps): React.ReactElement {
    // Active main tab: 'selected' or 'available'
    const [activeTab, setActiveTab] = React.useState<'selected' | 'available'>('selected');

    // View mode: 'list' (table) or 'showcase' (tiles)
    const [viewMode, setViewMode] = React.useState<'list' | 'showcase'>('list');

    // Gateways state
    const [gateways, setGateways] = React.useState<GatewayRecord[]>([]);
    const [loading, setLoading] = React.useState(true);
    const [selectedId, setSelectedId] = React.useState<number | null>(null);

    // Filter / search
    const [searchQuery, setSearchQuery] = React.useState('');
    const [showSearch, setShowSearch] = React.useState(false);

    // Modals
    const [editingGateway, setEditingGateway] = React.useState<GatewayRecord | null>(null);
    const [isCreating, setIsCreating] = React.useState(false);
    const [newModulePreset, setNewModulePreset] = React.useState<AvailableGatewayModule | null>(null);
    const [selectedModuleDetail, setSelectedModuleDetail] = React.useState<AvailableGatewayModule | null>(null);
    const [journalMsg, setJournalMsg] = React.useState<string | null>(null);
    const [confirmDeleteGateway, setConfirmDeleteGateway] = React.useState<GatewayRecord | null>(null);
    const [statusModal, setStatusModal] = React.useState<{ title: string; text: string } | null>(null);
    const [columnModal, setColumnModal] = React.useState(false);

    // Table view options
    const [autoArrange, setAutoArrange] = React.useState(true);
    const [showGrid, setShowGrid] = React.useState(true);
    const [visibleColumns, setVisibleColumns] = React.useState({
        name: true,
        mode: true,
        server: true,
        groups: true,
        symbols: true,
        lastActive: true,
        id: true,
        status: true,
    });

    // Context menu state
    const [contextMenu, setContextMenu] = React.useState<{ x: number; y: number } | null>(null);

    // File input ref for import
    const fileInputRef = React.useRef<HTMLInputElement | null>(null);

    // Load gateways from API
    const loadGateways = React.useCallback(async () => {
        setLoading(true);
        try {
            const list = await API.getGateways();
            if (Array.isArray(list)) {
                setGateways(list);
                if (selectedGatewayId !== undefined && selectedGatewayId !== null) {
                    const parsed = Number(selectedGatewayId);
                    if (!isNaN(parsed) && list.some((g) => g.id === parsed)) {
                        setSelectedId(parsed);
                    } else if (list.length > 0) {
                        setSelectedId(list[0].id);
                    }
                } else if (selectedId === null && list.length > 0) {
                    setSelectedId(list[0].id);
                }
            }
        } catch (e: any) {
            if (!isBackendGap(e)) {
                console.warn('Failed to load gateways:', e);
            }
        } finally {
            setLoading(false);
        }
    }, [selectedGatewayId, selectedId]);

    React.useEffect(() => {
        void loadGateways();
    }, [loadGateways]);

    // Update selection if prop changes
    React.useEffect(() => {
        if (selectedGatewayId !== undefined && selectedGatewayId !== null) {
            const parsed = Number(selectedGatewayId);
            if (!isNaN(parsed)) {
                setSelectedId(parsed);
                setActiveTab('selected');
            }
        }
    }, [selectedGatewayId]);

    const currentSelectedGateway = React.useMemo(() => {
        return gateways.find((g) => g.id === selectedId) || null;
    }, [gateways, selectedId]);

    const currentIndex = React.useMemo(() => {
        return gateways.findIndex((g) => g.id === selectedId);
    }, [gateways, selectedId]);

    const canMoveUp = currentIndex > 0;
    const canMoveDown = currentIndex >= 0 && currentIndex < gateways.length - 1;

    // Filtered lists
    const filteredGateways = React.useMemo(() => {
        if (!searchQuery.trim()) return gateways;
        const q = searchQuery.toLowerCase();
        return gateways.filter(
            (g) =>
                g.name.toLowerCase().includes(q) ||
                (g.module && g.module.toLowerCase().includes(q)) ||
                (g.server && g.server.toLowerCase().includes(q)) ||
                String(g.id).includes(q)
        );
    }, [gateways, searchQuery]);

    const filteredModules = React.useMemo(() => {
        if (!searchQuery.trim()) return AVAILABLE_GATEWAY_MODULES;
        const q = searchQuery.toLowerCase();
        return AVAILABLE_GATEWAY_MODULES.filter(
            (m) =>
                m.name.toLowerCase().includes(q) ||
                m.moduleFile.toLowerCase().includes(q) ||
                m.vendor.toLowerCase().includes(q) ||
                m.category.toLowerCase().includes(q)
        );
    }, [searchQuery]);

    // Handlers
    const handleAdd = () => {
        setNewModulePreset(null);
        setIsCreating(true);
    };

    const handleEdit = () => {
        if (currentSelectedGateway) {
            setEditingGateway(currentSelectedGateway);
        }
    };

    const handleDelete = () => {
        if (!currentSelectedGateway) return;
        setConfirmDeleteGateway(currentSelectedGateway);
    };

    const executeDelete = async (target: GatewayRecord) => {
        try {
            await API.deleteGateway(target.id);
            const remaining = gateways.filter((g) => g.id !== target.id);
            setGateways(remaining);
            if (remaining.length > 0) {
                const nextIdx = Math.min(currentIndex, remaining.length - 1);
                setSelectedId(remaining[nextIdx].id);
            } else {
                setSelectedId(null);
            }
        } catch (e: any) {
            setStatusModal({
                title: 'Error Deleting Gateway',
                text: 'Failed to delete gateway: ' + (e.message || String(e)),
            });
        } finally {
            setConfirmDeleteGateway(null);
        }
    };

    const handleMoveUp = () => {
        if (!canMoveUp) return;
        const updated = [...gateways];
        const temp = updated[currentIndex - 1];
        updated[currentIndex - 1] = updated[currentIndex];
        updated[currentIndex] = temp;
        setGateways(updated);
    };

    const handleMoveDown = () => {
        if (!canMoveDown) return;
        const updated = [...gateways];
        const temp = updated[currentIndex + 1];
        updated[currentIndex + 1] = updated[currentIndex];
        updated[currentIndex] = temp;
        setGateways(updated);
    };

    const handleSortAlphabetically = () => {
        const sorted = [...gateways].sort((a, b) => a.name.localeCompare(b.name));
        setGateways(sorted);
    };

    const handleEnable = async () => {
        if (!currentSelectedGateway || currentSelectedGateway.enabled || currentSelectedGateway.is_active) return;
        const updated: GatewayRecord = { ...currentSelectedGateway, enabled: true, is_active: true, status: 'Connected' };
        try {
            await API.updateGateway(updated.id, updated);
            setGateways((prev) => prev.map((g) => (g.id === updated.id ? updated : g)));
        } catch (e) {
            setGateways((prev) => prev.map((g) => (g.id === updated.id ? updated : g)));
        }
    };

    const handleDisable = async () => {
        if (!currentSelectedGateway || (!currentSelectedGateway.enabled && !currentSelectedGateway.is_active)) return;
        const updated: GatewayRecord = { ...currentSelectedGateway, enabled: false, is_active: false, status: 'Disabled' };
        try {
            await API.updateGateway(updated.id, updated);
            setGateways((prev) => prev.map((g) => (g.id === updated.id ? updated : g)));
        } catch (e) {
            setGateways((prev) => prev.map((g) => (g.id === updated.id ? updated : g)));
        }
    };

    const handleExport = () => {
        const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(gateways, null, 2));
        const downloadAnchor = document.createElement('a');
        downloadAnchor.setAttribute('href', dataStr);
        downloadAnchor.setAttribute('download', `MT5_Gateways_Export_${Date.now()}.json`);
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
    };

    const handleImportClick = () => {
        fileInputRef.current?.click();
    };

    const handleFileImport = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = async (event) => {
            try {
                const parsed = JSON.parse(event.target?.result as string);
                if (Array.isArray(parsed)) {
                    for (const item of parsed) {
                        try {
                            await API.createGateway(item);
                        } catch {
                            // ignore duplicate
                        }
                    }
                    await loadGateways();
                    setStatusModal({
                        title: 'Import Successful',
                        text: `Successfully imported ${parsed.length} gateways.`,
                    });
                }
            } catch (err: any) {
                setStatusModal({
                    title: 'Import Error',
                    text: 'Invalid JSON file format: ' + err.message,
                });
            }
        };
        reader.readAsText(file);
        e.target.value = '';
    };

    const handleSaveConfig = async (saved: GatewayRecord) => {
        try {
            if (isCreating) {
                const created = await API.createGateway(saved);
                setGateways((prev) => [...prev, created]);
                setSelectedId(created.id);
            } else {
                const updated = await API.updateGateway(saved.id, saved);
                setGateways((prev) => prev.map((g) => (g.id === updated.id ? updated : g)));
            }
        } catch (e) {
            // Local fallback
            if (isCreating) {
                setGateways((prev) => [...prev, saved]);
                setSelectedId(saved.id);
            } else {
                setGateways((prev) => prev.map((g) => (g.id === saved.id ? saved : g)));
            }
        } finally {
            setIsCreating(false);
            setEditingGateway(null);
            setNewModulePreset(null);
        }
    };

    const handleContextMenu = (e: React.MouseEvent) => {
        e.preventDefault();
        setContextMenu({ x: e.clientX, y: e.clientY });
    };

    return (
        <div
            className="adm-gateways-container"
            style={{
                display: 'flex',
                flexDirection: 'column',
                height: '100%',
                width: '100%',
                background: 'var(--theia-editor-background, #1e1e1e)',
                color: 'var(--theia-foreground, #cccccc)',
                fontFamily: 'Segoe UI, -apple-system, BlinkMacSystemFont, Roboto, sans-serif',
                userSelect: 'none',
                overflow: 'hidden',
            }}
            onContextMenu={handleContextMenu}
        >
            {/* Hidden Import File Input */}
            <input
                ref={fileInputRef}
                type="file"
                accept=".json,.xml"
                style={{ display: 'none' }}
                onChange={handleFileImport}
            />

            {/* Top Toolbar Header */}
            <div
                className="adm-gateways-toolbar"
                style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '4px 10px',
                    background: 'var(--theia-editorGroupHeader-tabsBackground, #252526)',
                    borderBottom: '1px solid var(--theia-border, #333333)',
                    flexShrink: 0,
                    gap: 8,
                }}
            >
                {/* Left Action Buttons */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Add Gateway (Ins)"
                        onClick={handleAdd}
                        style={{ display: 'flex', alignItems: 'center', gap: 4, padding: '3px 7px' }}
                    >
                        <i className="codicon codicon-add" style={{ color: '#89d185' }} />
                        <span style={{ fontSize: 12 }}>Add</span>
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Edit Selected Gateway (Enter)"
                        disabled={!currentSelectedGateway}
                        onClick={handleEdit}
                        style={{ display: 'flex', alignItems: 'center', gap: 4, padding: '3px 7px' }}
                    >
                        <i className="codicon codicon-edit" style={{ color: currentSelectedGateway ? '#4fc1ff' : undefined }} />
                        <span style={{ fontSize: 12 }}>Edit</span>
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Delete Selected Gateway (Del)"
                        disabled={!currentSelectedGateway}
                        onClick={handleDelete}
                        style={{ display: 'flex', alignItems: 'center', gap: 4, padding: '3px 7px' }}
                    >
                        <i className="codicon codicon-trash" style={{ color: currentSelectedGateway ? '#f14c4c' : undefined }} />
                        <span style={{ fontSize: 12 }}>Delete</span>
                    </button>

                    <div className="adm-toolbar-divider" style={{ width: 1, height: 16, background: '#444', margin: '0 4px' }} />

                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Move Up"
                        disabled={!canMoveUp}
                        onClick={handleMoveUp}
                    >
                        <i className="codicon codicon-arrow-up" />
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Move Down"
                        disabled={!canMoveDown}
                        onClick={handleMoveDown}
                    >
                        <i className="codicon codicon-arrow-down" />
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Sort Alphabetically"
                        onClick={handleSortAlphabetically}
                    >
                        <i className="codicon codicon-sort-precedence" />
                    </button>

                    <div className="adm-toolbar-divider" style={{ width: 1, height: 16, background: '#444', margin: '0 4px' }} />

                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Enable Gateway"
                        disabled={!currentSelectedGateway || currentSelectedGateway.enabled}
                        onClick={handleEnable}
                    >
                        <i className="codicon codicon-play" style={{ color: '#89d185' }} />
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Disable Gateway"
                        disabled={!currentSelectedGateway || !currentSelectedGateway.enabled}
                        onClick={handleDisable}
                    >
                        <i className="codicon codicon-debug-pause" style={{ color: '#cca700' }} />
                    </button>

                    <div className="adm-toolbar-divider" style={{ width: 1, height: 16, background: '#444', margin: '0 4px' }} />

                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Export to File"
                        onClick={handleExport}
                    >
                        <i className="codicon codicon-export" />
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Import from File"
                        onClick={handleImportClick}
                    >
                        <i className="codicon codicon-cloud-upload" />
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Journal"
                        disabled={!currentSelectedGateway}
                        onClick={() =>
                            setJournalMsg(
                                `Journal requested for gateway "${currentSelectedGateway?.name}" (ID: ${currentSelectedGateway?.id}). Query filters applied in Main Trade Server logs.`
                            )
                        }
                    >
                        <i className="codicon codicon-output" style={{ color: '#4fc1ff' }} />
                    </button>
                    <button
                        type="button"
                        className="adm-toolbar-btn"
                        title="Refresh"
                        onClick={() => void loadGateways()}
                    >
                        <i className="codicon codicon-refresh" />
                    </button>
                </div>

                {/* Right: Search + Showcase / List View Mode Icons */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                    {showSearch && (
                        <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
                            <input
                                type="text"
                                className="adm-input"
                                placeholder="Search..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                autoFocus
                                style={{
                                    height: 22,
                                    fontSize: 11,
                                    padding: '2px 20px 2px 6px',
                                    width: 150,
                                }}
                            />
                            <i
                                className="codicon codicon-close"
                                style={{
                                    position: 'absolute',
                                    right: 5,
                                    cursor: 'pointer',
                                    fontSize: 12,
                                    color: '#888',
                                }}
                                onClick={() => {
                                    setSearchQuery('');
                                    setShowSearch(false);
                                }}
                            />
                        </div>
                    )}
                    {!showSearch && (
                        <button
                            type="button"
                            className="adm-toolbar-btn"
                            title="Find (Ctrl+F)"
                            onClick={() => setShowSearch(true)}
                        >
                            <i className="codicon codicon-search" />
                        </button>
                    )}

                    <div className="adm-toolbar-divider" style={{ width: 1, height: 16, background: '#444', margin: '0 2px' }} />

                    {/* Product Showcase Mode (Tile Icon) */}
                    <button
                        type="button"
                        className={`adm-toolbar-btn ${viewMode === 'showcase' ? 'active' : ''}`}
                        title="Product Showcase (Tiles)"
                        onClick={() => setViewMode('showcase')}
                        style={{
                            background: viewMode === 'showcase' ? 'rgba(255,255,255,0.1)' : 'transparent',
                            borderRadius: 3,
                        }}
                    >
                        <i className="codicon codicon-layout-grid" />
                    </button>

                    {/* Configuration List Mode (List Icon) */}
                    <button
                        type="button"
                        className={`adm-toolbar-btn ${viewMode === 'list' ? 'active' : ''}`}
                        title="Configuration List (Table)"
                        onClick={() => setViewMode('list')}
                        style={{
                            background: viewMode === 'list' ? 'rgba(255,255,255,0.1)' : 'transparent',
                            borderRadius: 3,
                        }}
                    >
                        <i className="codicon codicon-list-flat" />
                    </button>
                </div>
            </div>

            {/* Main Content Area */}
            <div
                className="adm-gateways-body"
                style={{
                    flex: 1,
                    overflow: 'auto',
                    display: 'flex',
                    flexDirection: 'column',
                    position: 'relative',
                }}
            >
                {loading && (
                    <div
                        style={{
                            padding: 20,
                            textAlign: 'center',
                            color: '#888',
                            fontSize: 12,
                        }}
                    >
                        Loading gateways...
                    </div>
                )}

                {!loading && activeTab === 'selected' && (
                    <>
                        {viewMode === 'list' ? (
                            /* MT5 Selected Gateways Table View */
                            <div style={{ flex: 1, overflow: 'auto', width: '100%' }}>
                                <table
                                    className="adm-table"
                                    style={{
                                        width: '100%',
                                        borderCollapse: 'collapse',
                                        fontSize: 12,
                                        tableLayout: autoArrange ? 'auto' : 'fixed',
                                    }}
                                >
                                    <thead>
                                        <tr
                                            style={{
                                                background: 'var(--theia-list-headerBackground, #2d2d2d)',
                                                borderBottom: '1px solid var(--theia-border, #3a3a3a)',
                                                position: 'sticky',
                                                top: 0,
                                                zIndex: 10,
                                            }}
                                        >
                                            {visibleColumns.name && (
                                                <th style={{ textAlign: 'left', padding: '5px 10px', minWidth: 200, fontWeight: 600 }}>
                                                    Name
                                                </th>
                                            )}
                                            {visibleColumns.mode && (
                                                <th style={{ textAlign: 'left', padding: '5px 10px', width: 90, fontWeight: 600 }}>
                                                    Mode
                                                </th>
                                            )}
                                            {visibleColumns.server && (
                                                <th style={{ textAlign: 'left', padding: '5px 10px', minWidth: 160, fontWeight: 600 }}>
                                                    Server
                                                </th>
                                            )}
                                            {visibleColumns.groups && (
                                                <th style={{ textAlign: 'left', padding: '5px 10px', width: 140, fontWeight: 600 }}>
                                                    Groups
                                                </th>
                                            )}
                                            {visibleColumns.symbols && (
                                                <th style={{ textAlign: 'left', padding: '5px 10px', width: 140, fontWeight: 600 }}>
                                                    Symbols
                                                </th>
                                            )}
                                            {visibleColumns.lastActive && (
                                                <th style={{ textAlign: 'left', padding: '5px 10px', width: 150, fontWeight: 600 }}>
                                                    Last active
                                                </th>
                                            )}
                                            {visibleColumns.id && (
                                                <th style={{ textAlign: 'right', padding: '5px 10px', width: 70, fontWeight: 600 }}>
                                                    ID
                                                </th>
                                            )}
                                            {visibleColumns.status && (
                                                <th style={{ textAlign: 'left', padding: '5px 10px', minWidth: 260, fontWeight: 600 }}>
                                                    Status
                                                </th>
                                            )}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {filteredGateways.length === 0 ? (
                                            <tr>
                                                <td
                                                    colSpan={8}
                                                    style={{
                                                        textAlign: 'center',
                                                        padding: 30,
                                                        color: '#888',
                                                        fontStyle: 'italic',
                                                    }}
                                                >
                                                    No gateways configured. Switch to "Available" tab or click "Add" to add a new gateway.
                                                </td>
                                            </tr>
                                        ) : (
                                            filteredGateways.map((g) => {
                                                const isSel = g.id === selectedId;
                                                const modeLabel =
                                                    g.mode === 'Trade Only'
                                                        ? 'T'
                                                        : g.mode === 'Quotes Only'
                                                        ? 'Q'
                                                        : 'T + Q';

                                                return (
                                                    <tr
                                                        key={g.id}
                                                        onClick={() => setSelectedId(g.id)}
                                                        onDoubleClick={handleEdit}
                                                        style={{
                                                            background: isSel
                                                                ? 'var(--theia-list-activeSelectionBackground, #04395e)'
                                                                : 'transparent',
                                                            color: isSel
                                                                ? 'var(--theia-list-activeSelectionForeground, #ffffff)'
                                                                : g.enabled
                                                                ? 'inherit'
                                                                : '#888',
                                                            borderBottom: showGrid
                                                                ? '1px solid rgba(255,255,255,0.05)'
                                                                : 'none',
                                                            cursor: 'pointer',
                                                        }}
                                                    >
                                                        {visibleColumns.name && (
                                                            <td style={{ padding: '4px 10px' }}>
                                                                <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
                                                                    {/* Yellow MT5 Gateway Cylinder SVG */}
                                                                    <svg width="15" height="15" viewBox="0 0 16 16" fill="none">
                                                                        <ellipse
                                                                            cx="8"
                                                                            cy="4"
                                                                            rx="6"
                                                                            ry="2.5"
                                                                            fill={g.enabled ? '#f6c344' : '#888'}
                                                                            stroke={g.enabled ? '#d99b1a' : '#666'}
                                                                            strokeWidth="0.8"
                                                                        />
                                                                        <path
                                                                            d="M2 4v8c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V4"
                                                                            fill={g.enabled ? '#f9d368' : '#777'}
                                                                            stroke={g.enabled ? '#d99b1a' : '#666'}
                                                                            strokeWidth="0.8"
                                                                        />
                                                                        {g.enabled && (
                                                                            <ellipse
                                                                                cx="8"
                                                                                cy="8"
                                                                                rx="6"
                                                                                ry="2"
                                                                                stroke="#d99b1a"
                                                                                strokeWidth="0.6"
                                                                                fill="none"
                                                                                opacity="0.6"
                                                                            />
                                                                        )}
                                                                    </svg>
                                                                    <span style={{ fontWeight: 500 }}>{g.name}</span>
                                                                </div>
                                                            </td>
                                                        )}
                                                        {visibleColumns.mode && (
                                                            <td style={{ padding: '4px 10px', fontFamily: 'monospace' }}>
                                                                {modeLabel}
                                                            </td>
                                                        )}
                                                        {visibleColumns.server && (
                                                            <td style={{ padding: '4px 10px' }}>{g.server || '-'}</td>
                                                        )}
                                                        {visibleColumns.groups && (
                                                            <td style={{ padding: '4px 10px' }}>
                                                                {Array.isArray(g.groups)
                                                                    ? (g.groups as string[]).join(', ')
                                                                    : (g.groups || 'all')}
                                                            </td>
                                                        )}
                                                        {visibleColumns.symbols && (
                                                            <td style={{ padding: '4px 10px' }}>
                                                                {Array.isArray(g.symbols)
                                                                    ? (g.symbols as string[]).join(', ')
                                                                    : (g.symbols || '*')}
                                                            </td>
                                                        )}
                                                        {visibleColumns.lastActive && (
                                                            <td style={{ padding: '4px 10px' }}>
                                                                {g.lastActive || (g.enabled ? 'Online' : '-')}
                                                            </td>
                                                        )}
                                                        {visibleColumns.id && (
                                                            <td style={{ padding: '4px 10px', textAlign: 'right', fontFamily: 'monospace' }}>
                                                                {g.id}
                                                            </td>
                                                        )}
                                                        {visibleColumns.status && (
                                                            <td style={{ padding: '4px 10px' }}>
                                                                <span
                                                                    style={{
                                                                        color: !g.enabled
                                                                            ? '#888'
                                                                            : g.status?.toLowerCase().includes('connect')
                                                                            ? '#89d185'
                                                                            : '#dcdcaa',
                                                                    }}
                                                                >
                                                                    {g.status || (g.enabled ? 'Connected (Online)' : 'Disabled')}
                                                                </span>
                                                            </td>
                                                        )}
                                                    </tr>
                                                );
                                            })
                                        )}
                                    </tbody>
                                </table>
                            </div>
                        ) : (
                            /* MT5 Selected Showcase / Tile View */
                            <div
                                style={{
                                    display: 'grid',
                                    gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
                                    gap: 12,
                                    padding: 14,
                                }}
                            >
                                {filteredGateways.map((g) => {
                                    const isSel = g.id === selectedId;
                                    return (
                                        <div
                                            key={g.id}
                                            onClick={() => setSelectedId(g.id)}
                                            onDoubleClick={handleEdit}
                                            style={{
                                                background: isSel ? 'rgba(56, 139, 253, 0.12)' : 'rgba(255, 255, 255, 0.03)',
                                                border: `1px solid ${isSel ? '#388bfd' : 'var(--theia-border, #333)'}`,
                                                borderRadius: 6,
                                                padding: 12,
                                                cursor: 'pointer',
                                                display: 'flex',
                                                flexDirection: 'column',
                                                gap: 8,
                                                transition: 'border-color 0.15s, background-color 0.15s',
                                            }}
                                        >
                                            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                                                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                                    <svg width="22" height="22" viewBox="0 0 16 16" fill="none">
                                                        <ellipse cx="8" cy="4" rx="6" ry="2.5" fill={g.enabled ? '#f6c344' : '#888'} stroke={g.enabled ? '#d99b1a' : '#666'} strokeWidth="1" />
                                                        <path d="M2 4v8c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V4" fill={g.enabled ? '#f9d368' : '#777'} stroke={g.enabled ? '#d99b1a' : '#666'} strokeWidth="1" />
                                                    </svg>
                                                    <div>
                                                        <div style={{ fontWeight: 600, fontSize: 13, color: '#e6edf3' }}>{g.name}</div>
                                                        <div style={{ fontSize: 10, color: '#8b949e', fontFamily: 'monospace' }}>ID: {g.id}</div>
                                                    </div>
                                                </div>
                                                <span
                                                    style={{
                                                        fontSize: 10,
                                                        padding: '2px 6px',
                                                        borderRadius: 3,
                                                        background: g.enabled ? 'rgba(137, 209, 133, 0.15)' : 'rgba(255,255,255,0.08)',
                                                        color: g.enabled ? '#89d185' : '#888',
                                                        border: `1px solid ${g.enabled ? 'rgba(137, 209, 133, 0.3)' : 'transparent'}`,
                                                    }}
                                                >
                                                    {g.enabled ? 'ACTIVE' : 'DISABLED'}
                                                </span>
                                            </div>

                                            <div style={{ fontSize: 11, color: '#aaa', display: 'flex', flexDirection: 'column', gap: 3 }}>
                                                <div><strong>Endpoint:</strong> {g.server || 'None'}</div>
                                                <div><strong>Mode:</strong> {g.mode || 'Trade and Quotes'}</div>
                                                <div><strong>Module:</strong> {g.module || 'Default'}</div>
                                            </div>

                                            <div
                                                style={{
                                                    fontSize: 11,
                                                    padding: '5px 8px',
                                                    background: 'rgba(0, 0, 0, 0.25)',
                                                    borderRadius: 4,
                                                    color: g.enabled ? '#89d185' : '#888',
                                                    display: 'flex',
                                                    alignItems: 'center',
                                                    gap: 6,
                                                }}
                                            >
                                                <i className="codicon codicon-pulse" />
                                                <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                                                    {g.status || (g.enabled ? 'Connected' : 'Offline')}
                                                </span>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        )}
                    </>
                )}

                {!loading && activeTab === 'available' && (
                    <>
                        {viewMode === 'showcase' ? (
                            /* MT5 Available Showcase / Tile View */
                            <div
                                style={{
                                    display: 'grid',
                                    gridTemplateColumns: 'repeat(auto-fill, minmax(290px, 1fr))',
                                    gap: 14,
                                    padding: 14,
                                }}
                            >
                                {filteredModules.map((m) => (
                                    <div
                                        key={m.id}
                                        onClick={() => setSelectedModuleDetail(m)}
                                        style={{
                                            background: 'rgba(255, 255, 255, 0.03)',
                                            border: '1px solid var(--theia-border, #333)',
                                            borderRadius: 6,
                                            padding: 14,
                                            cursor: 'pointer',
                                            display: 'flex',
                                            flexDirection: 'column',
                                            gap: 10,
                                            transition: 'border-color 0.15s, background-color 0.15s',
                                        }}
                                        onMouseEnter={(e) => {
                                            e.currentTarget.style.borderColor = '#388bfd';
                                            e.currentTarget.style.backgroundColor = 'rgba(56, 139, 253, 0.06)';
                                        }}
                                        onMouseLeave={(e) => {
                                            e.currentTarget.style.borderColor = 'var(--theia-border, #333)';
                                            e.currentTarget.style.backgroundColor = 'rgba(255, 255, 255, 0.03)';
                                        }}
                                    >
                                        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 8 }}>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                                <div
                                                    style={{
                                                        width: 36,
                                                        height: 36,
                                                        borderRadius: 4,
                                                        background: 'rgba(246, 195, 68, 0.1)',
                                                        border: '1px solid rgba(246, 195, 68, 0.25)',
                                                        display: 'flex',
                                                        alignItems: 'center',
                                                        justifyContent: 'center',
                                                        flexShrink: 0,
                                                    }}
                                                >
                                                    <svg width="20" height="20" viewBox="0 0 16 16" fill="none">
                                                        <ellipse cx="8" cy="4" rx="6" ry="2.5" fill="#f6c344" stroke="#d99b1a" strokeWidth="1" />
                                                        <path d="M2 4v8c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V4" fill="#f9d368" stroke="#d99b1a" strokeWidth="1" />
                                                    </svg>
                                                </div>
                                                <div>
                                                    <div style={{ fontWeight: 600, fontSize: 13, color: '#e6edf3' }}>{m.name}</div>
                                                    <div style={{ fontSize: 11, color: '#8b949e', fontFamily: 'monospace' }}>{m.moduleFile}</div>
                                                </div>
                                            </div>
                                            <span
                                                style={{
                                                    fontSize: 10,
                                                    padding: '2px 6px',
                                                    borderRadius: 3,
                                                    background: 'rgba(56, 139, 253, 0.12)',
                                                    color: '#58a6ff',
                                                    border: '1px solid rgba(56, 139, 253, 0.25)',
                                                    whiteSpace: 'nowrap',
                                                }}
                                            >
                                                {m.category}
                                            </span>
                                        </div>

                                        <p
                                            style={{
                                                fontSize: 11,
                                                color: '#aaa',
                                                lineHeight: 1.45,
                                                margin: 0,
                                                display: '-webkit-box',
                                                WebkitLineClamp: 3,
                                                WebkitBoxOrient: 'vertical',
                                                overflow: 'hidden',
                                            }}
                                        >
                                            {m.description}
                                        </p>

                                        <div
                                            style={{
                                                display: 'flex',
                                                alignItems: 'center',
                                                justifyContent: 'space-between',
                                                paddingTop: 8,
                                                borderTop: '1px solid rgba(255,255,255,0.06)',
                                                fontSize: 11,
                                                color: '#8b949e',
                                            }}
                                        >
                                            <span>Default port: {m.defaultPort}</span>
                                            <span style={{ color: '#4fc1ff', display: 'flex', alignItems: 'center', gap: 4 }}>
                                                View Spec <i className="codicon codicon-arrow-right" />
                                            </span>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        ) : (
                            /* MT5 Available Table View */
                            <div style={{ flex: 1, overflow: 'auto', width: '100%' }}>
                                <table
                                    className="adm-table"
                                    style={{
                                        width: '100%',
                                        borderCollapse: 'collapse',
                                        fontSize: 12,
                                    }}
                                >
                                    <thead>
                                        <tr
                                            style={{
                                                background: 'var(--theia-list-headerBackground, #2d2d2d)',
                                                borderBottom: '1px solid var(--theia-border, #3a3a3a)',
                                                position: 'sticky',
                                                top: 0,
                                                zIndex: 10,
                                            }}
                                        >
                                            <th style={{ textAlign: 'left', padding: '5px 10px', minWidth: 220, fontWeight: 600 }}>
                                                Gateway Module
                                            </th>
                                            <th style={{ textAlign: 'left', padding: '5px 10px', minWidth: 160, fontWeight: 600 }}>
                                                Binary File
                                            </th>
                                            <th style={{ textAlign: 'left', padding: '5px 10px', width: 140, fontWeight: 600 }}>
                                                Category
                                            </th>
                                            <th style={{ textAlign: 'left', padding: '5px 10px', minWidth: 160, fontWeight: 600 }}>
                                                Protocol
                                            </th>
                                            <th style={{ textAlign: 'left', padding: '5px 10px', minWidth: 180, fontWeight: 600 }}>
                                                Developer / Vendor
                                            </th>
                                            <th style={{ textAlign: 'right', padding: '5px 10px', width: 100, fontWeight: 600 }}>
                                                Port
                                            </th>
                                            <th style={{ textAlign: 'center', padding: '5px 10px', width: 120, fontWeight: 600 }}>
                                                Action
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {filteredModules.map((m) => (
                                            <tr
                                                key={m.id}
                                                onClick={() => setSelectedModuleDetail(m)}
                                                style={{
                                                    borderBottom: showGrid ? '1px solid rgba(255,255,255,0.05)' : 'none',
                                                    cursor: 'pointer',
                                                }}
                                            >
                                                <td style={{ padding: '6px 10px' }}>
                                                    <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
                                                        <svg width="15" height="15" viewBox="0 0 16 16" fill="none">
                                                            <ellipse cx="8" cy="4" rx="6" ry="2.5" fill="#f6c344" stroke="#d99b1a" strokeWidth="0.8" />
                                                            <path d="M2 4v8c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V4" fill="#f9d368" stroke="#d99b1a" strokeWidth="0.8" />
                                                        </svg>
                                                        <span style={{ fontWeight: 500, color: '#e6edf3' }}>{m.name}</span>
                                                    </div>
                                                </td>
                                                <td style={{ padding: '6px 10px', fontFamily: 'monospace', color: '#8b949e' }}>
                                                    {m.moduleFile}
                                                </td>
                                                <td style={{ padding: '6px 10px' }}>{m.category}</td>
                                                <td style={{ padding: '6px 10px' }}>{m.protocol}</td>
                                                <td style={{ padding: '6px 10px' }}>{m.vendor}</td>
                                                <td style={{ padding: '6px 10px', textAlign: 'right', fontFamily: 'monospace' }}>
                                                    {m.defaultPort}
                                                </td>
                                                <td style={{ padding: '6px 10px', textAlign: 'center' }}>
                                                    <button
                                                        type="button"
                                                        className="adm-btn adm-btn-secondary"
                                                        onClick={(e) => {
                                                            e.stopPropagation();
                                                            setSelectedModuleDetail(m);
                                                        }}
                                                        style={{ padding: '2px 8px', fontSize: 11 }}
                                                    >
                                                        Details...
                                                    </button>
                                                </td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        )}
                    </>
                )}
            </div>

            {/* Bottom Tabs Bar (Selected / Available) matching MT5 architecture */}
            <div
                className="adm-gateways-bottom-tabs"
                style={{
                    display: 'flex',
                    alignItems: 'center',
                    background: 'var(--theia-editorGroupHeader-tabsBackground, #252526)',
                    borderTop: '1px solid var(--theia-border, #333333)',
                    padding: '0 8px',
                    height: 28,
                    flexShrink: 0,
                    gap: 4,
                }}
            >
                <button
                    type="button"
                    onClick={() => setActiveTab('selected')}
                    style={{
                        padding: '4px 14px',
                        background: activeTab === 'selected' ? 'var(--theia-editor-background, #1e1e1e)' : 'transparent',
                        color: activeTab === 'selected' ? '#ffffff' : '#888888',
                        border: 'none',
                        borderTop: activeTab === 'selected' ? '2px solid #007acc' : '2px solid transparent',
                        cursor: 'pointer',
                        fontSize: 12,
                        fontWeight: activeTab === 'selected' ? 600 : 400,
                        display: 'flex',
                        alignItems: 'center',
                        gap: 6,
                    }}
                >
                    <i className="codicon codicon-check-all" style={{ color: activeTab === 'selected' ? '#89d185' : undefined }} />
                    Selected ({gateways.length})
                </button>
                <button
                    type="button"
                    onClick={() => setActiveTab('available')}
                    style={{
                        padding: '4px 14px',
                        background: activeTab === 'available' ? 'var(--theia-editor-background, #1e1e1e)' : 'transparent',
                        color: activeTab === 'available' ? '#ffffff' : '#888888',
                        border: 'none',
                        borderTop: activeTab === 'available' ? '2px solid #007acc' : '2px solid transparent',
                        cursor: 'pointer',
                        fontSize: 12,
                        fontWeight: activeTab === 'available' ? 600 : 400,
                        display: 'flex',
                        alignItems: 'center',
                        gap: 6,
                    }}
                >
                    <i className="codicon codicon-cloud" style={{ color: activeTab === 'available' ? '#4fc1ff' : undefined }} />
                    Available ({AVAILABLE_GATEWAY_MODULES.length})
                </button>

                <div style={{ flex: 1 }} />

                <span style={{ fontSize: 11, color: '#777', paddingRight: 6 }}>
                    {activeTab === 'selected'
                        ? `${gateways.filter((g) => g.enabled).length} active, ${gateways.length} total gateways`
                        : `${AVAILABLE_GATEWAY_MODULES.length} modules found in /gateways/`}
                </span>
            </div>

            {/* Context Menu */}
            {contextMenu && (
                <GatewaysContextMenu
                    x={contextMenu.x}
                    y={contextMenu.y}
                    hasSelection={Boolean(currentSelectedGateway)}
                    canMoveUp={canMoveUp}
                    canMoveDown={canMoveDown}
                    isGatewayEnabled={currentSelectedGateway?.enabled}
                    autoArrange={autoArrange}
                    grid={showGrid}
                    onClose={() => setContextMenu(null)}
                    onAdd={handleAdd}
                    onEdit={handleEdit}
                    onDelete={handleDelete}
                    onMoveUp={handleMoveUp}
                    onMoveDown={handleMoveDown}
                    onSortAlphabetically={handleSortAlphabetically}
                    onEnable={handleEnable}
                    onDisable={handleDisable}
                    onAutomationTriggers={() =>
                        setStatusModal({
                            title: 'Automation Triggers',
                            text: 'No automation triggers configured for the selected gateway.',
                        })
                    }
                    onAutomationActions={() =>
                        setStatusModal({
                            title: 'Automation Actions',
                            text: 'No automation actions configured for the selected gateway.',
                        })
                    }
                    onExport={handleExport}
                    onImport={handleImportClick}
                    onJournal={() =>
                        setJournalMsg(
                            `Journal requested for gateway "${currentSelectedGateway?.name}" (ID: ${currentSelectedGateway?.id}).`
                        )
                    }
                    onFind={() => setShowSearch(true)}
                    onToggleAutoArrange={() => setAutoArrange((v) => !v)}
                    onToggleGrid={() => setShowGrid((v) => !v)}
                    onToggleColumns={() => setColumnModal(true)}
                />
            )}

            {/* 7-Tab Gateway Configuration Modal (Add / Edit) */}
            {(editingGateway || isCreating) && (
                <GatewayConfigModal
                    gateway={
                        editingGateway || {
                            id: Math.floor(100 + Math.random() * 900),
                            name: newModulePreset ? newModulePreset.name : 'New Gateway',
                            module: newModulePreset ? newModulePreset.moduleFile : 'MT5GatewayCurrenex.dll',
                            mode: 'Trade and Quotes',
                            enabled: true,
                            is_active: true,
                            server: '127.0.0.1:16387',
                            login: '1000',
                            password: '',
                            groups: 'demo\\*, real\\*',
                            symbols: '*',
                            import_traders_balances: true,
                            import_symbol_settings: true,
                            parameters: [],
                            translations: [],
                            timeouts: {
                                reconnect_interval: 15,
                                reconnect_attempts: 10,
                                reconnect_series_interval: 60,
                            },
                            monitoring: {
                                enable_logging: true,
                                enable_profiling: false,
                                collect_days: 7,
                            },
                            advanced_network: {
                                gateway_server: 'history.server:16387',
                                gateway_login: '1000',
                                password: '',
                            },
                        }
                    }
                    isNew={isCreating}
                    onClose={() => {
                        setIsCreating(false);
                        setEditingGateway(null);
                        setNewModulePreset(null);
                    }}
                    onSave={handleSaveConfig}
                />
            )}

            {/* Available Gateway Detail Specification Modal */}
            {selectedModuleDetail && (
                <AvailableGatewayDetailModal
                    module={selectedModuleDetail}
                    onClose={() => setSelectedModuleDetail(null)}
                    onAddGateway={(m) => {
                        setNewModulePreset(m);
                        setIsCreating(true);
                    }}
                />
            )}

            {/* Journal Dialog */}
            {journalMsg && (
                <div className="adm-modal-overlay" onClick={() => setJournalMsg(null)} style={{ zIndex: 2200 }}>
                    <div
                        className="adm-modal"
                        style={{ width: 480 }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div className="adm-modal-header" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                <i className="codicon codicon-output" style={{ color: '#4fc1ff' }} />
                                <span>Gateway Journal</span>
                            </div>
                            <button
                                type="button"
                                className="adm-modal-close"
                                onClick={() => setJournalMsg(null)}
                                style={{ background: 'transparent', border: 'none', color: '#888', cursor: 'pointer' }}
                            >
                                ×
                            </button>
                        </div>
                        <div className="adm-modal-body" style={{ padding: 16, fontSize: 12 }}>
                            <p style={{ margin: 0, lineHeight: 1.5 }}>{journalMsg}</p>
                        </div>
                        <div
                            className="adm-modal-footer"
                            style={{ padding: '8px 16px', display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid #333' }}
                        >
                            <button
                                type="button"
                                className="adm-btn adm-btn-primary"
                                onClick={() => setJournalMsg(null)}
                                style={{ padding: '4px 14px' }}
                            >
                                OK
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Columns Customization Modal */}
            {columnModal && (
                <div className="adm-modal-overlay" onClick={() => setColumnModal(false)} style={{ zIndex: 2200 }}>
                    <div
                        className="adm-modal"
                        style={{ width: 340 }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div className="adm-modal-header" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                <i className="codicon codicon-layout-col" />
                                <span>Customize Columns</span>
                            </div>
                            <button
                                type="button"
                                className="adm-modal-close"
                                onClick={() => setColumnModal(false)}
                                style={{ background: 'transparent', border: 'none', color: '#888', cursor: 'pointer' }}
                            >
                                ×
                            </button>
                        </div>
                        <div className="adm-modal-body" style={{ padding: 14, display: 'flex', flexDirection: 'column', gap: 8 }}>
                            {Object.keys(visibleColumns).map((colKey) => (
                                <label
                                    key={colKey}
                                    style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 12, cursor: 'pointer' }}
                                >
                                    <input
                                        type="checkbox"
                                        checked={(visibleColumns as any)[colKey]}
                                        onChange={(e) =>
                                            setVisibleColumns((prev) => ({
                                                ...prev,
                                                [colKey]: e.target.checked,
                                            }))
                                        }
                                    />
                                    <span style={{ textTransform: 'capitalize' }}>{colKey}</span>
                                </label>
                            ))}
                        </div>
                        <div
                            className="adm-modal-footer"
                            style={{ padding: '8px 14px', display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid #333' }}
                        >
                            <button
                                type="button"
                                className="adm-btn adm-btn-primary"
                                onClick={() => setColumnModal(false)}
                                style={{ padding: '4px 14px' }}
                            >
                                Close
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* In-app Delete Confirmation Modal (no browser confirm) */}
            {confirmDeleteGateway && (
                <div
                    className="adm-modal-overlay"
                    onClick={() => setConfirmDeleteGateway(null)}
                    style={{ zIndex: 2300 }}
                >
                    <div
                        className="adm-modal"
                        style={{ width: 440 }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div
                            className="adm-modal-header"
                            style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}
                        >
                            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                <i className="codicon codicon-warning" style={{ color: '#f14c4c' }} />
                                <span>Delete Gateway</span>
                            </div>
                            <button
                                type="button"
                                className="adm-modal-close"
                                onClick={() => setConfirmDeleteGateway(null)}
                                style={{ background: 'transparent', border: 'none', color: '#888', cursor: 'pointer' }}
                            >
                                ×
                            </button>
                        </div>
                        <div className="adm-modal-body" style={{ padding: 16, fontSize: 12 }}>
                            <p style={{ margin: 0, lineHeight: 1.5 }}>
                                Are you sure you want to delete gateway{' '}
                                <strong>"{confirmDeleteGateway.name}"</strong> (ID: {confirmDeleteGateway.id})?
                            </p>
                        </div>
                        <div
                            className="adm-modal-footer"
                            style={{
                                padding: '8px 16px',
                                display: 'flex',
                                justifyContent: 'flex-end',
                                gap: 8,
                                borderTop: '1px solid #333',
                            }}
                        >
                            <button
                                type="button"
                                className="adm-btn"
                                style={{
                                    background: '#d32f2f',
                                    color: '#fff',
                                    padding: '4px 14px',
                                    fontWeight: 600,
                                }}
                                onClick={() => void executeDelete(confirmDeleteGateway)}
                            >
                                Delete
                            </button>
                            <button
                                type="button"
                                className="adm-btn adm-btn-secondary"
                                onClick={() => setConfirmDeleteGateway(null)}
                                style={{ padding: '4px 14px' }}
                            >
                                Cancel
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* In-app Status / Alert Modal (no browser alert) */}
            {statusModal && (
                <div
                    className="adm-modal-overlay"
                    onClick={() => setStatusModal(null)}
                    style={{ zIndex: 2300 }}
                >
                    <div
                        className="adm-modal"
                        style={{ width: 440 }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div
                            className="adm-modal-header"
                            style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}
                        >
                            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                <i className="codicon codicon-info" style={{ color: '#4fc1ff' }} />
                                <span>{statusModal.title}</span>
                            </div>
                            <button
                                type="button"
                                className="adm-modal-close"
                                onClick={() => setStatusModal(null)}
                                style={{ background: 'transparent', border: 'none', color: '#888', cursor: 'pointer' }}
                            >
                                ×
                            </button>
                        </div>
                        <div className="adm-modal-body" style={{ padding: 16, fontSize: 12 }}>
                            <p style={{ margin: 0, lineHeight: 1.5 }}>{statusModal.text}</p>
                        </div>
                        <div
                            className="adm-modal-footer"
                            style={{ padding: '8px 16px', display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid #333' }}
                        >
                            <button
                                type="button"
                                className="adm-btn adm-btn-primary"
                                onClick={() => setStatusModal(null)}
                                style={{ padding: '4px 14px' }}
                            >
                                OK
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default GatewaysPage;
