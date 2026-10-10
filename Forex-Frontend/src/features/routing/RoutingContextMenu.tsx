import * as React from 'react';

export interface RoutingContextMenuProps {
    x: number;
    y: number;
    hasSelection: boolean;
    canMoveUp: boolean;
    canMoveDown: boolean;
    isRuleEnabled?: boolean;
    autoArrange: boolean;
    grid: boolean;
    onClose: () => void;
    onAdd: () => void;
    onEdit: () => void;
    onDelete: () => void;
    onMoveUp: () => void;
    onMoveDown: () => void;
    onSortAlphabetically: () => void;
    onEnable: () => void;
    onDisable: () => void;
    onAutomationActions: () => void;
    onExport: () => void;
    onImport: () => void;
    onJournal: () => void;
    onFind: () => void;
    onToggleAutoArrange: () => void;
    onToggleGrid: () => void;
    onToggleColumns: () => void;
}

export function RoutingContextMenu({
    x,
    y,
    hasSelection,
    canMoveUp,
    canMoveDown,
    isRuleEnabled,
    autoArrange,
    grid,
    onClose,
    onAdd,
    onEdit,
    onDelete,
    onMoveUp,
    onMoveDown,
    onSortAlphabetically,
    onEnable,
    onDisable,
    onAutomationActions,
    onExport,
    onImport,
    onJournal,
    onFind,
    onToggleAutoArrange,
    onToggleGrid,
    onToggleColumns,
}: RoutingContextMenuProps): React.ReactElement {
    React.useEffect(() => {
        const handleOutsideClick = () => onClose();
        window.addEventListener('click', handleOutsideClick);
        return () => window.removeEventListener('click', handleOutsideClick);
    }, [onClose]);

    const handleAction = (fn: () => void) => {
        fn();
        onClose();
    };

    // Keep context menu on screen
    const menuWidth = 200;
    const menuHeight = 440;
    const adjustedX = x + menuWidth > window.innerWidth ? Math.max(10, window.innerWidth - menuWidth - 10) : x;
    const adjustedY = y + menuHeight > window.innerHeight ? Math.max(10, window.innerHeight - menuHeight - 10) : y;

    return (
        <div
            className="adm-context-menu"
            style={{
                position: 'fixed',
                top: adjustedY,
                left: adjustedX,
                zIndex: 2500,
                minWidth: 190,
                boxShadow: '0 4px 16px rgba(0, 0, 0, 0.45)',
            }}
            onClick={(e) => e.stopPropagation()}
        >
            {/* Group 1: Add, Edit, Delete */}
            <button type="button" className="adm-context-item" onClick={() => handleAction(onAdd)}>
                <i className="codicon codicon-add" style={{ color: '#89d185' }} /> Add
            </button>
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection}
                onClick={() => handleAction(onEdit)}
            >
                <i className="codicon codicon-edit" style={{ color: '#4fc1ff' }} /> Edit
            </button>
            <button
                type="button"
                className="adm-context-item adm-context-item-danger"
                disabled={!hasSelection}
                onClick={() => handleAction(onDelete)}
            >
                <i className="codicon codicon-trash" style={{ color: '#f48771' }} /> Delete
            </button>

            <div className="adm-context-sep" />

            {/* Group 2: Move Up, Move Down, Sort Alphabetically */}
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection || !canMoveUp}
                onClick={() => handleAction(onMoveUp)}
            >
                <i className="codicon codicon-arrow-up" /> Move Up
            </button>
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection || !canMoveDown}
                onClick={() => handleAction(onMoveDown)}
            >
                <i className="codicon codicon-arrow-down" /> Move Down
            </button>
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onSortAlphabetically)}
            >
                <i className="codicon codicon-symbol-class" /> Sort Alphabetically
            </button>

            <div className="adm-context-sep" />

            {/* Group 3: Enable, Disable */}
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection || isRuleEnabled === true}
                onClick={() => handleAction(onEnable)}
            >
                <i className="codicon codicon-check" style={{ color: '#89d185' }} /> Enable
            </button>
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection || isRuleEnabled === false}
                onClick={() => handleAction(onDisable)}
            >
                <i className="codicon codicon-close" style={{ color: '#f48771' }} /> Disable
            </button>

            <div className="adm-context-sep" />

            {/* Group 4: Automation Actions */}
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onAutomationActions)}
            >
                <i className="codicon codicon-symbol-event" /> Automation Actions
            </button>

            <div className="adm-context-sep" />

            {/* Group 5: Export to File, Import from File */}
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onExport)}
            >
                <i className="codicon codicon-cloud-download" style={{ color: '#4ec9b0' }} /> Export to File
            </button>
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onImport)}
            >
                <i className="codicon codicon-cloud-upload" style={{ color: '#ce9178' }} /> Import from File
            </button>

            <div className="adm-context-sep" />

            {/* Group 6: Journal */}
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onJournal)}
            >
                <i className="codicon codicon-output" /> Journal
            </button>

            <div className="adm-context-sep" />

            {/* Group 7: Find */}
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onFind)}
            >
                <i className="codicon codicon-search" /> Find
            </button>

            <div className="adm-context-sep" />

            {/* Group 8: Auto Arrange, Grid, Columns */}
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onToggleAutoArrange)}
            >
                <span style={{ width: 14, textAlign: 'center', marginRight: 4 }}>
                    {autoArrange ? '✓' : ''}
                </span>
                Auto Arrange
            </button>
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onToggleGrid)}
            >
                <span style={{ width: 14, textAlign: 'center', marginRight: 4 }}>
                    {grid ? '✓' : ''}
                </span>
                Grid
            </button>
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onToggleColumns)}
            >
                <i className="codicon codicon-layout-panel" /> Columns
            </button>
        </div>
    );
}
