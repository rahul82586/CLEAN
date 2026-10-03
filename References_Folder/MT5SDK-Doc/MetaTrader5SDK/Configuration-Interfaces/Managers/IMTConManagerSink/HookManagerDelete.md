[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerSink](../IMTConManagerSink.md) / HookManagerDelete

[Previous](HookManagerUpdate.md) | [Next](../../History-Synchronization.md)

# IMTConManagerSink::HookManagerDelete

Hook for the deletion of a manager configuration.

C++
    
    
    virtual MTAPIRES  IMTConManagerSink::HookManagerDelete(
       const UINT64         login,     // Manager login
       const IMTConManager* cfg        // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConManagerSink.HookManagerDelete(
       ulong                login,     // Manager login
       CIMTConManager       cfg        // Configuration object
       )

### Parameters

**login**  
[in]The login of the managerwho is deleting the configuration. If the configuration is to be deleted by the plugin, 0 is specified in the parameter.

**cfg**  
[in] A pointer to themanager configuration object.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before deleting a record from the configuration database. The main purpose of this hook is prevent the unwanted deletion of records.
