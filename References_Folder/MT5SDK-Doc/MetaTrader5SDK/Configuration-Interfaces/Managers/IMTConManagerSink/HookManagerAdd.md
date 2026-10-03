[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerSink](../IMTConManagerSink.md) / HookManagerAdd

[Previous](OnManagerSync.md) | [Next](HookManagerUpdate.md)

# IMTConManagerSink::HookManagerAdd

Hook for the addition of a new manager configuration.

C++
    
    
    virtual MTAPIRES  IMTConManagerSink::HookManagerAdd(
       const UINT64         login,     // Manager login
       IMTConManager*       new_cfg    // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConManagerSink.HookManagerAdd(
       ulong                login,     // Manager login
       CIMTConManager       new_cfg    // Configuration object
       )

### Parameters

**login**  
[in]The login of the manager, who is adding the new configuration. If the new configuration is being added by the plugin, 0 is specified in the parameter.

**new_cfg**  
[in/out] A pointer theobject of the manager to be added.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before adding a manager configuration to the client base. The main purpose of this hook is to modify an entry that is added, and, if necessary, to prevent the addition of unwanted records.
