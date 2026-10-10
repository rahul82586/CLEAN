import * as React from 'react';
import { API, isBackendGap } from '../../services/api';
import { RoutingRuleItem, RoutingRuleModal } from './RoutingRuleModal';
import { RoutingContextMenu } from './RoutingContextMenu';

function formatDealersList(dealers?: Array<{ login: string | number; name: string }>): string {
    if (!dealers || dealers.length === 0) return '';
    return dealers
        .map((d) => (d.name.includes(String(d.login)) ? d.name : `${d.name} (${d.login})`))
        .join(', ');
}

export function RoutingPage(): React.ReactElement {
    const [rules, setRules] = React.useState<RoutingRuleItem[]>([]);
    const [loading, setLoading] = React.useState(true);
    const [selectedId, setSelectedId] = React.useState<number | null>(null);
    const [searchQuery, setSearchQuery] = React.useState('');
    const [showSearch, setShowSearch] = React.useState(false);

    // Modals
    const [editingRule, setEditingRule] = React.useState<RoutingRuleItem | null>(null);
    const [isCreating, setIsCreating] = React.useState(false);
    const [journalMsg, setJournalMsg] = React.useState<string | null>(null);
    const [columnModal, setColumnModal] = React.useState(false);

    // View options
    const [autoArrange, setAutoArrange] = React.useState(true);
    const [showGrid, setShowGrid] = React.useState(true);
    const [visibleColumns, setVisibleColumns] = React.useState({
        name: true,
        action: true,
        dealers: true,
    });

    // Context menu state
    const [contextMenu, setContextMenu] = React.useState<{ x: number; y: number } | null>(null);

    // File input ref for import
    const fileInputRef = React.useRef<HTMLInputElement | null>(null);

    const loadRules = React.useCallback(async () => {
        setLoading(true);
        try {
            const res = await API.getRoutingRules();
            if (Array.isArray(res) && res.length > 0) {
                setRules(res);
                if (selectedId === null && res.length > 0) setSelectedId(res[0].id);
            }
        } catch (e: any) {
            // If backend gap, keep current rules or default MT5 samples
            if (!isBackendGap(e)) {
                console.warn('Failed to load routing rules:', e);
            }
        } finally {
            setLoading(false);
        }
    }, [selectedId]);

    React.useEffect(() => {
        void loadRules();
    }, [loadRules]);

    const selectedIndex = rules.findIndex((r) => r.id === selectedId);
    const selectedRule = selectedIndex >= 0 ? rules[selectedIndex] : null;

    // Actions
    const handleAdd = () => {
        setIsCreating(true);
        setEditingRule({
            id: Date.now(),
            name: 'New Rule',
            priority: rules.length + 1,
            is_enabled: true,
            action: 'Confirm by request price',
            action_type: 'Confirm by request price',
            request_type: 'All',
            order_type: 'All',
            conditions: [{ type: 'Group', condition: 'Equal (=)', value: '*' }],
            dealers: [],
        });
    };

    const handleEdit = () => {
        if (!selectedRule) return;
        setIsCreating(false);
        setEditingRule(selectedRule);
    };

    const handleDelete = async () => {
        if (!selectedRule) return;
        if (!window.confirm(`Delete routing rule "${selectedRule.name}"?`)) return;
        try {
            await API.deleteRoutingRule(selectedRule.id);
        } catch {
            // Keep local state in sync
        }
        setRules((prev) => {
            const next = prev.filter((r) => r.id !== selectedRule.id);
            if (next.length > 0) setSelectedId(next[0].id);
            else setSelectedId(null);
            return next;
        });
    };

    const handleMove = async (up: boolean) => {
        if (selectedIndex < 0) return;
        const target = up ? selectedIndex - 1 : selectedIndex + 1;
        if (target < 0 || target >= rules.length) return;

        const next = [...rules];
        const tmp = next[selectedIndex];
        next[selectedIndex] = next[target];
        next[target] = tmp;

        // Update priority indices
        const reindexed = next.map((r, i) => ({ ...r, priority: i + 1 }));
        setRules(reindexed);
        setSelectedId(tmp.id);

        try {
            await API.reorderRoutingRules(reindexed.map((r) => r.id));
        } catch {
            /* local state preserved */
        }
    };

    const handleSortAlphabetically = () => {
        const sorted = [...rules].sort((a, b) => a.name.localeCompare(b.name));
        const reindexed = sorted.map((r, i) => ({ ...r, priority: i + 1 }));
        setRules(reindexed);
    };

    const handleToggleEnable = async (enable: boolean) => {
        if (!selectedRule) return;
        try {
            if (enable) await API.enableRoutingRule(selectedRule.id);
            else await API.disableRoutingRule(selectedRule.id);
        } catch {
            /* sync locally */
        }
        setRules((prev) =>
            prev.map((r) => (r.id === selectedRule.id ? { ...r, is_enabled: enable } : r))
        );
    };

    const handleSaveRule = async (saved: RoutingRuleItem) => {
        try {
            if (isCreating) {
                await API.createRoutingRule(saved as any);
                setRules((prev) => [...prev, saved]);
            } else {
                await API.updateRoutingRule(saved.id, saved as any);
                setRules((prev) => prev.map((r) => (r.id === saved.id ? saved : r)));
            }
        } catch {
            // Keep state intact
            setRules((prev) => {
                if (isCreating) return [...prev, saved];
                return prev.map((r) => (r.id === saved.id ? saved : r));
            });
        }
        setSelectedId(saved.id);
        setEditingRule(null);
    };

    const handleExport = () => {
        const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(rules, null, 2));
        const downloadAnchor = document.createElement('a');
        downloadAnchor.setAttribute('href', dataStr);
        downloadAnchor.setAttribute('download', `mt5_routing_rules_${new Date().toISOString().slice(0, 10)}.json`);
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
    };

    const handleImport = () => {
        if (fileInputRef.current) {
            fileInputRef.current.value = '';
            fileInputRef.current.click();
        }
    };

    const onFileSelected = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (event) => {
            try {
                const parsed = JSON.parse(String(event.target?.result));
                if (Array.isArray(parsed)) {
                    setRules(parsed);
                    if (parsed.length > 0) setSelectedId(parsed[0].id);
                    alert(`Successfully imported ${parsed.length} routing rules.`);
                }
            } catch {
                alert('Invalid JSON file format for routing rules.');
            }
        };
        reader.readAsText(file);
    };

    const handleJournal = () => {
        if (!selectedRule) return;
        setJournalMsg(
            `[Server Journal Query]\nRequest logs for routing rule '${selectedRule.name}':\n` +
            `Rule execution mode: ${selectedRule.action}\n` +
            `Assigned dealers: ${formatDealersList(selectedRule.dealers) || 'None'}\n` +
            `Status: ${selectedRule.is_enabled ? 'Active / Evaluating requests' : 'Disabled'}`
        );
    };

    const filteredRules = React.useMemo(() => {
        if (!searchQuery.trim()) return rules;
        const q = searchQuery.toLowerCase();
        return rules.filter(
            (r) =>
                r.name.toLowerCase().includes(q) ||
                r.action.toLowerCase().includes(q) ||
                formatDealersList(r.dealers).toLowerCase().includes(q)
        );
    }, [rules, searchQuery]);

    // Right click handler
    const onContextMenu = (e: React.MouseEvent, rowId?: number) => {
        e.preventDefault();
        e.stopPropagation();
        if (rowId !== undefined) {
            setSelectedId(rowId);
        }
        setContextMenu({ x: e.clientX, y: e.clientY });
    };

    return (
        <div
            className="mt5-admin-content-panel"
            style={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                background: 'var(--theia-editor-background)',
                color: 'var(--theia-foreground)',
                userSelect: 'none',
                overflow: 'hidden',
                fontFamily: 'var(--theia-ui-font-family)',
                fontSize: 11,
            }}
            onContextMenu={(e) => onContextMenu(e)}
        >
            <input
                type="file"
                ref={fileInputRef}
                style={{ display: 'none' }}
                accept=".json"
                onChange={onFileSelected}
            />

            {/* ── MT5 Standard Action Toolbar ────────────────────────────── */}
            <div
                style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '3px 8px',
                    borderBottom: '1px solid var(--theia-border)',
                    background: 'var(--theia-sideBarSectionHeader-background)',
                    flexShrink: 0,
                    gap: 4,
                }}
            >
                {/* Left Action Buttons */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 2, flexWrap: 'wrap' }}>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        onClick={loadRules}
                        title="Refresh"
                    >
                        <i className="codicon codicon-refresh" /> Refresh
                    </button>

                    <div style={{ width: 1, height: 16, background: 'var(--theia-border)', margin: '0 2px' }} />

                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        onClick={handleExport}
                        title="Export to file"
                    >
                        <i className="codicon codicon-cloud-download" style={{ color: '#4ec9b0' }} /> Export
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        onClick={handleImport}
                        title="Import from file"
                    >
                        <i className="codicon codicon-cloud-upload" style={{ color: '#ce9178' }} /> Import
                    </button>

                    <div style={{ width: 1, height: 16, background: 'var(--theia-border)', margin: '0 2px' }} />

                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        onClick={handleAdd}
                        title="Add routing rule"
                    >
                        <i className="codicon codicon-add" style={{ color: '#89d185' }} /> Add
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        disabled={!selectedRule}
                        onClick={handleEdit}
                        title="Edit routing rule"
                    >
                        <i className="codicon codicon-edit" style={{ color: '#4fc1ff' }} /> Edit
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        disabled={!selectedRule}
                        onClick={handleDelete}
                        title="Delete routing rule"
                    >
                        <i className="codicon codicon-trash" style={{ color: '#f48771' }} /> Delete
                    </button>

                    <div style={{ width: 1, height: 16, background: 'var(--theia-border)', margin: '0 2px' }} />

                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        disabled={selectedIndex <= 0}
                        onClick={() => handleMove(true)}
                        title="Move Up"
                    >
                        <i className="codicon codicon-arrow-up" />
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        disabled={selectedIndex < 0 || selectedIndex >= rules.length - 1}
                        onClick={() => handleMove(false)}
                        title="Move Down"
                    >
                        <i className="codicon codicon-arrow-down" />
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        onClick={handleSortAlphabetically}
                        title="Sort Alphabetically"
                    >
                        <i className="codicon codicon-symbol-class" /> Sort
                    </button>

                    <div style={{ width: 1, height: 16, background: 'var(--theia-border)', margin: '0 2px' }} />

                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        disabled={!selectedRule || selectedRule.is_enabled}
                        onClick={() => handleToggleEnable(true)}
                        title="Enable rule"
                    >
                        <i className="codicon codicon-check" style={{ color: '#89d185' }} /> Enable
                    </button>
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, padding: '0 7px', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4 }}
                        disabled={!selectedRule || !selectedRule.is_enabled}
                        onClick={() => handleToggleEnable(false)}
                        title="Disable rule"
                    >
                        <i className="codicon codicon-close" style={{ color: '#f48771' }} /> Disable
                    </button>
                </div>

                {/* Right Filter / Find */}
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                    {showSearch && (
                        <input
                            className="adm-input"
                            style={{ width: 150, height: 21, fontSize: 11, padding: '1px 6px' }}
                            placeholder="Find rule..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            autoFocus
                        />
                    )}
                    <button
                        type="button"
                        className="wb-btn secondary"
                        style={{ height: 22, width: 26, padding: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                        onClick={() => setShowSearch(!showSearch)}
                        title="Find"
                    >
                        <i className="codicon codicon-search" />
                    </button>
                </div>
            </div>

            {/* ── Rules Table ────────────────────────────────────────────── */}
            <div style={{ flex: 1, minHeight: 0, overflow: 'auto', background: 'var(--theia-editor-background)' }}>
                <table
                    className={`adm-table ${showGrid ? 'adm-table-grid' : ''}`}
                    style={{
                        width: '100%',
                        borderCollapse: 'collapse',
                        fontSize: 11,
                        tableLayout: autoArrange ? 'auto' : 'fixed',
                    }}
                >
                    <thead>
                        <tr
                            style={{
                                background: 'var(--theia-sideBarSectionHeader-background)',
                                position: 'sticky',
                                top: 0,
                                zIndex: 10,
                                textAlign: 'left',
                                borderBottom: '1px solid var(--theia-border)',
                            }}
                        >
                            {visibleColumns.name && (
                                <th style={{ padding: '4px 8px', width: autoArrange ? '28%' : 260, borderRight: showGrid ? '1px solid var(--theia-border)' : 'none' }}>
                                    Name
                                </th>
                            )}
                            {visibleColumns.action && (
                                <th style={{ padding: '4px 8px', width: autoArrange ? '42%' : 380, borderRight: showGrid ? '1px solid var(--theia-border)' : 'none' }}>
                                    Action
                                </th>
                            )}
                            {visibleColumns.dealers && (
                                <th style={{ padding: '4px 8px' }}>
                                    Dealers
                                </th>
                            )}
                        </tr>
                    </thead>
                    <tbody>
                        {filteredRules.map((r) => {
                            const isSelected = r.id === selectedId;
                            return (
                                <tr
                                    key={r.id}
                                    onClick={() => setSelectedId(r.id)}
                                    onDoubleClick={handleEdit}
                                    onContextMenu={(e) => onContextMenu(e, r.id)}
                                    style={{
                                        background: isSelected
                                            ? 'var(--theia-list-activeSelectionBackground)'
                                            : 'transparent',
                                        color: isSelected
                                            ? 'var(--theia-list-activeSelectionForeground)'
                                            : r.is_enabled
                                            ? 'var(--theia-foreground)'
                                            : 'var(--theia-descriptionForeground)',
                                        borderBottom: showGrid ? '1px solid var(--theia-border)' : 'none',
                                        cursor: 'pointer',
                                    }}
                                >
                                    {visibleColumns.name && (
                                        <td
                                            style={{
                                                padding: '4px 8px',
                                                borderRight: showGrid ? '1px solid var(--theia-border)' : 'none',
                                                whiteSpace: 'nowrap',
                                            }}
                                        >
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                                {/* Double Crossing Arrow Icon (Green if enabled, Red if disabled) */}
                                                <svg
                                                    width="14"
                                                    height="14"
                                                    viewBox="0 0 16 16"
                                                    style={{ flexShrink: 0 }}
                                                >
                                                    {r.is_enabled ? (
                                                        <>
                                                            {/* Green Up-Right Arrow */}
                                                            <path
                                                                d="M3 13 L12 4 M7 4 L12 4 L12 9"
                                                                stroke="#2ecc71"
                                                                strokeWidth="2"
                                                                strokeLinecap="round"
                                                                strokeLinejoin="round"
                                                                fill="none"
                                                            />
                                                            {/* Green Down-Left Arrow */}
                                                            <path
                                                                d="M13 3 L4 12 M9 12 L4 12 L4 7"
                                                                stroke="#2ecc71"
                                                                strokeWidth="2"
                                                                strokeLinecap="round"
                                                                strokeLinejoin="round"
                                                                fill="none"
                                                            />
                                                        </>
                                                    ) : (
                                                        <>
                                                            {/* Red Up-Right Arrow */}
                                                            <path
                                                                d="M3 13 L12 4 M7 4 L12 4 L12 9"
                                                                stroke="#e74c3c"
                                                                strokeWidth="2"
                                                                strokeLinecap="round"
                                                                strokeLinejoin="round"
                                                                fill="none"
                                                            />
                                                            {/* Red Down-Left Arrow */}
                                                            <path
                                                                d="M13 3 L4 12 M9 12 L4 12 L4 7"
                                                                stroke="#e74c3c"
                                                                strokeWidth="2"
                                                                strokeLinecap="round"
                                                                strokeLinejoin="round"
                                                                fill="none"
                                                            />
                                                        </>
                                                    )}
                                                </svg>
                                                <span style={{ fontWeight: isSelected ? 600 : 400 }}>{r.name}</span>
                                            </div>
                                        </td>
                                    )}

                                    {visibleColumns.action && (
                                        <td
                                            style={{
                                                padding: '4px 8px',
                                                borderRight: showGrid ? '1px solid var(--theia-border)' : 'none',
                                            }}
                                        >
                                            {r.action}
                                        </td>
                                    )}

                                    {visibleColumns.dealers && (
                                        <td style={{ padding: '4px 8px', opacity: r.dealers?.length ? 1 : 0.6 }}>
                                            {formatDealersList(r.dealers) || '—'}
                                        </td>
                                    )}
                                </tr>
                            );
                        })}

                        {!loading && filteredRules.length === 0 && (
                            <tr>
                                <td
                                    colSpan={3}
                                    style={{
                                        padding: '40px 16px',
                                        textAlign: 'center',
                                        opacity: 0.6,
                                    }}
                                >
                                    {rules.length === 0
                                        ? 'No routing rules configured. Click Add to create a new rule.'
                                        : 'No rules match the current search filter.'}
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>

            {/* ── Status Bar / Bottom summary ────────────────────────────── */}
            <div
                style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '3px 10px',
                    borderTop: '1px solid var(--theia-border)',
                    background: 'var(--theia-sideBarSectionHeader-background)',
                    fontSize: 10.5,
                    opacity: 0.85,
                    flexShrink: 0,
                }}
            >
                <div>
                    Rules: {rules.length} total ({rules.filter((r) => r.is_enabled).length} enabled)
                </div>
                <div>Top-down first-match execution order</div>
            </div>

            {/* Context Menu with all 16 items */}
            {contextMenu && (
                <RoutingContextMenu
                    x={contextMenu.x}
                    y={contextMenu.y}
                    hasSelection={selectedRule !== null}
                    canMoveUp={selectedIndex > 0}
                    canMoveDown={selectedIndex >= 0 && selectedIndex < rules.length - 1}
                    isRuleEnabled={selectedRule?.is_enabled}
                    autoArrange={autoArrange}
                    grid={showGrid}
                    onClose={() => setContextMenu(null)}
                    onAdd={handleAdd}
                    onEdit={handleEdit}
                    onDelete={handleDelete}
                    onMoveUp={() => handleMove(true)}
                    onMoveDown={() => handleMove(false)}
                    onSortAlphabetically={handleSortAlphabetically}
                    onEnable={() => handleToggleEnable(true)}
                    onDisable={() => handleToggleEnable(false)}
                    onAutomationActions={() =>
                        alert(
                            'Routing Automation Actions:\nConfigure server automation triggers and automated hedging tasks based on order routing events.'
                        )
                    }
                    onExport={handleExport}
                    onImport={handleImport}
                    onJournal={handleJournal}
                    onFind={() => setShowSearch(true)}
                    onToggleAutoArrange={() => setAutoArrange(!autoArrange)}
                    onToggleGrid={() => setShowGrid(!showGrid)}
                    onToggleColumns={() => setColumnModal(true)}
                />
            )}

            {/* Edit / Add Rule Modal */}
            {editingRule && (
                <RoutingRuleModal
                    rule={editingRule}
                    isNew={isCreating}
                    onClose={() => setEditingRule(null)}
                    onSave={handleSaveRule}
                />
            )}

            {/* Journal Dialog */}
            {journalMsg && (
                <div
                    style={{
                        position: 'fixed',
                        inset: 0,
                        zIndex: 3000,
                        background: 'rgba(0, 0, 0, 0.55)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                    }}
                    onClick={() => setJournalMsg(null)}
                >
                    <div
                        style={{
                            background: 'var(--theia-editor-background)',
                            border: '1px solid var(--theia-border)',
                            borderRadius: 4,
                            width: 440,
                            padding: 16,
                            boxShadow: '0 8px 24px rgba(0, 0, 0, 0.5)',
                        }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div style={{ fontWeight: 600, fontSize: 13, marginBottom: 8, display: 'flex', alignItems: 'center', gap: 6 }}>
                            <i className="codicon codicon-output" /> Routing Server Journal
                        </div>
                        <pre
                            style={{
                                background: 'var(--theia-input-background)',
                                border: '1px solid var(--theia-border)',
                                padding: 10,
                                borderRadius: 3,
                                fontSize: 11,
                                whiteSpace: 'pre-wrap',
                                color: 'var(--theia-foreground)',
                                fontFamily: 'Consolas, monospace',
                            }}
                        >
                            {journalMsg}
                        </pre>
                        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 12 }}>
                            <button
                                type="button"
                                className="wb-btn"
                                style={{ minWidth: 60, height: 23 }}
                                onClick={() => setJournalMsg(null)}
                            >
                                Close
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Columns Toggle Dialog */}
            {columnModal && (
                <div
                    style={{
                        position: 'fixed',
                        inset: 0,
                        zIndex: 3000,
                        background: 'rgba(0, 0, 0, 0.55)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                    }}
                    onClick={() => setColumnModal(false)}
                >
                    <div
                        style={{
                            background: 'var(--theia-editor-background)',
                            border: '1px solid var(--theia-border)',
                            borderRadius: 4,
                            width: 280,
                            padding: 16,
                            boxShadow: '0 8px 24px rgba(0, 0, 0, 0.5)',
                        }}
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div style={{ fontWeight: 600, fontSize: 12, marginBottom: 12 }}>Configure Columns</div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                <input
                                    type="checkbox"
                                    checked={visibleColumns.name}
                                    onChange={(e) => setVisibleColumns({ ...visibleColumns, name: e.target.checked })}
                                />
                                <span>Name</span>
                            </label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                <input
                                    type="checkbox"
                                    checked={visibleColumns.action}
                                    onChange={(e) => setVisibleColumns({ ...visibleColumns, action: e.target.checked })}
                                />
                                <span>Action</span>
                            </label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                <input
                                    type="checkbox"
                                    checked={visibleColumns.dealers}
                                    onChange={(e) => setVisibleColumns({ ...visibleColumns, dealers: e.target.checked })}
                                />
                                <span>Dealers</span>
                            </label>
                        </div>
                        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 14 }}>
                            <button
                                type="button"
                                className="wb-btn"
                                style={{ minWidth: 60, height: 23 }}
                                onClick={() => setColumnModal(false)}
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
