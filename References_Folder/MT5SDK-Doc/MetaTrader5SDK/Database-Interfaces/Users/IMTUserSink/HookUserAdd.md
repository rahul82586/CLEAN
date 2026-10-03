[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserAdd

[Previous](OnUserRestore.md) | [Next](HookUserAddExt.md)

# IMTUserSink::HookUserAdd

A hook of an event of adding a new account.
    
    
    virtual MTAPIRES  IMTUserSink::HookUserAdd(
       IMTUser*  user      // An object of the account
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTUserSink.HookUserAdd(
       CIMTUser  user      // Account object
       )

### Parameters

**user**  
[in] A pointer to the object of aIMTUserrecord to add.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before adding an account record to the data base. The main purpose of this hook is to modify an entry that is added, and, if necessary, to prevent the addition of unwanted records.
