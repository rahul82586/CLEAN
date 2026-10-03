[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSink](../IMTConGroupSink.md) / HookGroupUpdate

[Previous](HookGroupAdd.md) | [Next](HookGroupDelete.md)

# IMTConGroupSink::HookGroupAdd

Hook for the update of group settings.

C++
    
    
    virtual MTAPIRES  IMTConGroupSink::HookGroupUpdate(
       const UINT64         login,     // Manager login
       const IMTConGroup*   cfg,       // A pointer to the current group
       IMTConGroup*         new_cfg    // A pointer to the updated group
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConGroupSink.HookGroupUpdate(
       ulong                login,     // Manager login
       CIMTConGroup         cfg,       // Current group
       CIMTConGroup         new_cfg    // Updated group
       )

### Parameters

**login**  
[in]The login of the manager, who is going to update the group settings. If the group is to be updated by the plugin, 0 is specified in the parameter.

**cfg**  
[in] A pointer to thecurrent group object.

**new_cfg**  
[out] A pointer to thegroup objectafter making change.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before making changes to the configuration database. The main purpose of this hook is to modify an entry that is being updated, and, if necessary, to prevent the unwanted change of records.
