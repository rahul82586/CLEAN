[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserAddExt

[Previous](OnUserAdd.md) | [Next](OnUserUpdate.md)

# IMTUserSink::OnUserAddExt

An extended handler of a new account addition event. It additionally passes the passwords of the created account.
    
    
    virtual void  IMTUserSink::OnUserAddExt(
       const IMTUser*  user,               // A pointer to the added record
       LPCWSTR         master_password,    // Main password
       LPCWSTR         investor_password,  // Investor password
       )

### Parameters

**user**  
[in] A pointer to theIMTUseradded user object.

**master_password**  
[in] The main password of the created account.

**investor_password**  
[in] The investor password of the created account.

### Note

The method is only used in the MetaTrader 5 Server API.
