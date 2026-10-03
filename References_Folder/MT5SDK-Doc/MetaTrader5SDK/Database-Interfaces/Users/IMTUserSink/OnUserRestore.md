[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserRestore

[Previous](OnUserArchive.md) | [Next](HookUserAdd.md)

# IMTUserSink::OnUserRestore

A handler of the event of restoration of an account [from an archive or backup database](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_archive).
    
    
    virtual void  IMTUserSink::OnUserRestore(
       const IMTUser*  user      // A pointer to an account object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserRestore(
       CIMTUser        user      // Account object
       )

### Parameters

**user**  
[in] A pointer to the object of the added account record.

### Note

An account can be restored using the [Administrator terminal](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_archive) or using API methods [IMTServerAPI::UserRestore](../../../Server-API/Main-API-Interface/Users/UserRestore.md) and [IMTAdminAPI::UserRestore](../../../Manager-API/Administrator-Interface/Users/UserRestore.md).
