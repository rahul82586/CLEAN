[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserSync

[Previous](OnUserChangePassword.md) | [Next](OnUserArchive.md)

# IMTUserSink::OnUserSync

A handler of the event of the account base synchronization.

C++
    
    
    virtual void  IMTUserSink::OnUserSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserSync()

### Note

The handler is used only in [Gateway API](../../../Gateway-API/Main-Interface/Users/UserSubscribe.md) and [Manager API](../../../Manager-API/Manager-Interface/Users/UserSubscribe.md). It is called after the synchronization of the user databases between API and the trade server. If multiple trade servers are used in the platform, the handler is called several times — after synchronizing with each of them.
