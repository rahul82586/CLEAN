[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserAddExt

[Previous](HookUserAdd.md) | [Next](HookUserUpdate.md)

# IMTUserSink::HookUserAddExt

An extended hook for the new account addition event. It additionally passes the passwords of the created account.
    
    
    virtual MTAPIRES  IMTUserSink::HookUserAddExt(
       IMTUser*  user                // Account object
       LPCWSTR   master_password,    // Main password
       LPCWSTR   investor_password,  // Investor password
       )

### Parameters

**user**  
[in] A pointer to theIMTUseradded user object.

**master_password**  
[in] The main password of the created account.

**investor_password**  
[in] The investor password of the created account.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before an account is added to the database. The main purpose of this hook is to modify an entry being added and, if necessary, to prevent the addition of unwanted records.
