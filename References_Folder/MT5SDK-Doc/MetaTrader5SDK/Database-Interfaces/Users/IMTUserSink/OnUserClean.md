[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserClean

[Previous](OnUserDelete.md) | [Next](OnUserLogin.md)

# IMTUserSink::OnUserClean

A handler of the event of deletion of obsolete demo account on a trade server.

C++
    
    
    virtual void  IMTUserSink::OnUserClean(
       const UINT64  login      // Account login
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserClean(
       ulong         login      // Account login
       )

### Parameters

**login**  
[in] The login of an account.

### Note

Every day, at server time, expired demo accounts are automatically deleted on trade servers. The handler notifies of such an operation and transmits the logins of deleted accounts.
