[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSink](../IMTConGroupSink.md) / HookGroupAdd

[Previous](OnGroupSync.md) | [Next](HookGroupUpdate.md)

# IMTConGroupSink::HookGroupAdd

Hook for the new group addition.

C++
    
    
    virtual MTAPIRES  IMTConGroupSink::HookGroupAdd(
       const UINT64         login,     // Manager login
       IMTConGroup*         new_cfg    // A pointer to the group object
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConGroupSink.HookGroupAdd(
       ulong                login,     // Manager login
       CIMTConGroup         new_cfg    // Group object
       )

### Parameters

**login**  
[in]The login of the manager, who is adding the new group. If the new group is being added by the plugin, 0 is specified in the parameter.

**new_cfg**  
[in/out] A pointer theobject of the group to be added.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before adding a group configuration to the client base. The main purpose of this hook is to modify an entry that is added, and, if necessary, to prevent the addition of unwanted records.
