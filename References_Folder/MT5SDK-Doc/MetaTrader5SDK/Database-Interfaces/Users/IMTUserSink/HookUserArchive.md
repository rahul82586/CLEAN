[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserArchive

[Previous](HookUserChangePassword.md) | [Next](../../Online-Connections.md)

# IMTUserSink::HookUserArchive

A hook of the event of [moving an account to an archive database](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_archive).
    
    
    virtual void  IMTUserSink::HookUserArchive(
       const IMTUser*  user      // A pointer to an account record
       )

.NET(Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.HookUserArchive(
       CIMTUser        user      // Account object
       )

### Parameters

**user**  
[in] A pointer to theIMTUserobject of the added account record.

### Return value

To confirm the transfer to the archive, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) should be returned. If the hook returns a code different from [MT_RET_OK](../../../Return-Codes/Successful-completion.md), the account record will not be moved to archive and the hook will not be passed to other handlers (including other plugins).

### Note

An account can be moved to archive using the [Administrator terminal](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_archive) or using API methods [IMTServerAPI::UserArchive](../../../Server-API/Main-API-Interface/Users/UserArchive.md) and [IMTAdminAPI::UserArchive](../../../Manager-API/Administrator-Interface/Users/UserArchive.md).

  1. IMTUserSink::HookUserArchive
  2. [IMTUserSink::HookUserDelete](HookUserDelete.md)
  3. [IMTUserSink::OnUsersDelete](OnUserDelete.md)
  4. [IMTUserSink::OnUsersArchive](OnUserArchive.md)


