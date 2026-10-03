[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserArchive

[Previous](OnUserSync.md) | [Next](OnUserRestore.md)

# IMTUserSink::OnUserArchive

A handler of the event of [moving an account to an archive database](https://support.metaquotes.net/zh/docs/mt5/platform/administration/admin_accounts/accounts_archive).
    
    
    virtual void  IMTUserSink::OnUserArchive(
       const IMTUser*  user      // A pointer to an account object
       )

.NET(Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserArchive(
       CIMTUser        user      // Account object
       )

### Parameters

**user**  
[in] A pointer to the object of the added accountIMTUser.

### Note

An account can be moved to archive using the [Administrator terminal](https://support.metaquotes.net/zh/docs/mt5/platform/administration/admin_accounts/accounts_archive) or using API methods [IMTServerAPI::UserArchive](../../../Server-API/Main-API-Interface/Users/UserArchive.md) and [IMTAdminAPI::UserArchive](../../../Manager-API/Administrator-Interface/Users/UserArchive.md).

  1. [IMTUserSink::HookUserArchive](HookUserArchive.md)
  2. [IMTUserSink::HookUserDelete](HookUserDelete.md)
  3. [IMTUserSink::OnUsersDelete](OnUserDelete.md)
  4. IMTUserSink::OnUsersArchive


