[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserUpdate

[Previous](HookUserAddExt.md) | [Next](HookUserDelete.md)

# IMTUserSink::HookUserUpdate

A hook of an event of account record update.
    
    
    virtual MTAPIRES  IMTUserSink::HookUserUpdate(
       const IMTUser*  prev,     // An object of the current account record
       IMTUser*        user      // An object of the account record after the update
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTUserSink.HookUserUpdate(
       CIMTUser        prev,     // Current account record
       CIMTUser        user      // Account record after the update
       )

### Parameters

**prev**  
[in] A pointer to the object of the currentIMTUseraccount record.

**user**  
[in/out] A pointer to the object of an account record after modification.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before updating an account record in the client base. The main purpose of this hook is to modify an entry that is updated, and, if necessary, to prevent the unwanted change of records.
