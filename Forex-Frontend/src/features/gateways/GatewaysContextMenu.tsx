import * as React from 'react';

export interface GatewaysContextMenuProps {
    x: number;
    y: number;
    hasSelection: boolean;
    canMoveUp: boolean;
    canMoveDown: boolean;
    isGatewayEnabled?: boolean;
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
    onAutomationTriggers?: () => void;
    onAutomationActions?: () => void;
    onExport: () => void;
    onImport: () => void;
    onJournal: () => void;
    onFind: () => void;
    onToggleAutoArrange: () => void;
    onToggleGrid: () => void;
    onToggleColumns: () => void;
}

export function GatewaysContextMenu({
    x,
    y,
    hasSelection,
    canMoveUp,
    canMoveDown,
    isGatewayEnabled,
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
    onAutomationTriggers,
    onAutomationActions,
    onExport,
    onImport,
    onJournal,
    onFind,
    onToggleAutoArrange,
    onToggleGrid,
    onToggleColumns,
}: GatewaysContextMenuProps): React.ReactElement {
    React.useEffect(() => {
        const handleOutsideClick = () => onClose();
        window.addEventListener('click', handleOutsideClick);
        return () => window.removeEventListener('click', handleOutsideClick);
    }, [onClose]);

    const handleAction = (fn?: () => void) => {
        if (!fn) return;
        fn();
        onClose();
    };

    const menuWidth = 210;
    const menuHeight = 490;
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
                minWidth: 200,
                boxShadow: '0 4px 18px rgba(0, 0, 0, 0.5)',
                background: 'var(--theia-menu-background, #252526)',
                border: '1px solid var(--theia-menu-border, #454545)',
                padding: '4px 0',
                borderRadius: 3,
                fontSize: 12,
            }}
            onClick={(e) => e.stopPropagation()}
        >
            {/* Primary Operations */}
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
                className="adm-context-item"
                disabled={!hasSelection}
                onClick={() => handleAction(onDelete)}
            >
                <i className="codicon codicon-trash" style={{ color: '#f14c4c' }} /> Delete
            </button>

            <div className="adm-context-separator" style={{ height: 1, background: 'rgba(255,255,255,0.1)', margin: '4px 0' }} />

            {/* Reorder and Sorting */}
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
                <i className="codicon codicon-sort-precedence" /> Sort Alphabetically
            </button>

            <div className="adm-context-separator" style={{ height: 1, background: 'rgba(255,255,255,0.1)', margin: '4px 0' }} />

            {/* Enable / Disable */}
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection || isGatewayEnabled === true}
                onClick={() => handleAction(onEnable)}
            >
                <i className="codicon codicon-play" style={{ color: '#89d185' }} /> Enable
            </button>
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection || isGatewayEnabled === false}
                onClick={() => handleAction(onDisable)}
            >
                <i className="codicon codicon-debug-pause" style={{ color: '#cca700' }} /> Disable
            </button>

            <div className="adm-context-separator" style={{ height: 1, background: 'rgba(255,255,255,0.1)', margin: '4px 0' }} />

            {/* Automation */}
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection}
                onClick={() => handleAction(onAutomationTriggers)}
            >
                <i className="codicon codicon-zap" style={{ color: '#dcdcaa' }} /> Automation triggers
            </button>
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection}
                onClick={() => handleAction(onAutomationActions)}
            >
                <i className="codicon codicon-play-circle" style={{ color: '#dcdcaa' }} /> Automation actions
            </button>

            <div className="adm-context-separator" style={{ height: 1, background: 'rgba(255,255,255,0.1)', margin: '4px 0' }} />

            {/* File & Utilities */}
            <button type="button" className="adm-context-item" onClick={() => handleAction(onExport)}>
                <i className="codicon codicon-export" /> Export to File
            </button>
            <button type="button" className="adm-context-item" onClick={() => handleAction(onImport)}>
                <i className="codicon codicon-cloud-upload" /> Import from File
            </button>
            <button
                type="button"
                className="adm-context-item"
                disabled={!hasSelection}
                onClick={() => handleAction(onJournal)}
            >
                <i className="codicon codicon-output" style={{ color: '#4fc1ff' }} /> Journal
            </button>
            <button type="button" className="adm-context-item" onClick={() => handleAction(onFind)}>
                <i className="codicon codicon-search" /> Find
            </button>

            <div className="adm-context-separator" style={{ height: 1, background: 'rgba(255,255,255,0.1)', margin: '4px 0' }} />

            {/* View Customizations */}
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onToggleAutoArrange)}
            >
                <i
                    className={`codicon ${autoArrange ? 'codicon-check' : 'codicon-blank'}`}
                    style={{ color: autoArrange ? '#89d185' : 'transparent', width: 16 }}
                />{' '}
                Auto Arrange
            </button>
            <button type="button" className="adm-context-item" onClick={() => handleAction(onToggleGrid)}>
                <i
                    className={`codicon ${grid ? 'codicon-check' : 'codicon-blank'}`}
                    style={{ color: grid ? '#89d185' : 'transparent', width: 16 }}
                />{' '}
                Grid
            </button>
            <button
                type="button"
                className="adm-context-item"
                onClick={() => handleAction(onToggleColumns)}
            >
                <i className="codicon codicon-layout-col" /> Columns
            </button>
        </div>
    );
}
