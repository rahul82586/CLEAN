[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerSink](../IMTConManagerSink.md) / HookManagerUpdate

[Previous](HookManagerAdd.md) | [Next](HookManagerDelete.md)

# IMTConManagerSink::HookManagerUpdate

Hook for the update of manager settings.

C++
    
    
    virtual MTAPIRES  IMTConManagerSink::HookManagerUpdate(
       const UINT64         login,     // Manager login
       const IMTConManager* cfg,       // A pointer to the current configuration
       IMTConManager*       new_cfg    // A pointer to the updated configuration
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConManagerSink.HookManagerUpdate(
       ulong                login,     // Manager login
       CIMTConManager       cfg,       // Current configuration
       CIMTConManager       new_cfg    // Updated configuration
       )

### Parameters

**login**  
[in]The login of the manager, who is going to update the configuration settings. If the configuration is to be updated by the plugin, 0 is specified in the parameter.

**cfg**  
[in] A pointer to thecurrent configuration object.

**new_cfg**  
[out] A pointer to themanager configuration objectafter making change.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

If the event handler returns a code different from [MT_RET_OK](../../../Return-Codes/Successful-completion.md), the manager will not be updated and the hook will not be passed to other handlers (including other plugins).

### Note

The hook is called right before making changes to the configuration database. The main purpose of this hook is to modify an entry that is being updated, and, if necessary, to prevent the unwanted change of records.

This method can only be used in the MetaTrader 5 Server API.
