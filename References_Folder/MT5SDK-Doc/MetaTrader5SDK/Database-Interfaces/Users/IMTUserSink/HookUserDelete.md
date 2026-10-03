[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserDelete

[Previous](HookUserUpdate.md) | [Next](HookUserLogin.md)

# IMTUserSink::HookUserDelete

A hook of an event of account record deletion.
    
    
    virtual MTAPIRES  IMTUserSink::HookUserDelete(
       const IMTUser*  user      // An object of a deleted account record
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTUserSink.HookUserDelete(
       CIMTUser        user      // Deleted account record
       )

### Parameters

**user**  
[in] A pointer to the object of anIMTUseraccount record to delete.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before deleting an account record from the client base. The main purpose of this hook is prevent the unwanted deletion of records.
