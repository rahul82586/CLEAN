[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSink](../IMTConGroupSink.md) / HookGroupDelete

[Previous](HookGroupUpdate.md) | [Next](../IMTConCommission.md)

# IMTConGroupSink::HookGroupDelete

Group deletion hook.

C++
    
    
    virtual MTAPIRES  IMTConGroupSink::HookGroupDelete(
       const UINT64         login,     // Manager login
       const IMTConGroup*   cfg        // A pointer to the group object
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConGroupSink.HookGroupDelete(
       ulong                login,     // Manager login
       CIMTConGroup         cfg        // Group object
       )

### Parameters

**login**  
[in]The login of the managerwho is deleting the group. If the group is to be deleted by the plugin, 0 is specified in the parameter.

**cfg**  
[in] A pointer to thegroup object.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before deleting a record from the configuration database. The main purpose of this hook is prevent the unwanted deletion of records.
