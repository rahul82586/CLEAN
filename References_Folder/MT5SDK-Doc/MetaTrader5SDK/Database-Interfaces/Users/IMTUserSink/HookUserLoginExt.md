[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserLoginExt

[Previous](HookUserLogin.md) | [Next](HookUserChangePassword.md)

# IMTUserSink::HookUserLoginExt

A hook of a account's connection to the server. Passes an extended description of the connection.
    
    
    virtual MTAPIRES  IMTUserSink::HookUserLoginExt(
       const IMTUser*          user,   // Account object
       const IMTOnline*        online  // A pointer to the connection object
       )

.NET(Gateway/Manager API)
    
    
    virtual MTRetCoed  CIMTUserSink.HookUserLoginExt(
       CIMTUser                user,   // Account object
       CIMTOnline              online  // Connection object
       )

### Parameters

**user**  
[in] A pointer to theIMTUseraccount object.

**online**  
[in] A pointer to theIMTOnlineconnection description object.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called after a successful authorization of an account connection, before the connection starts working.

  * [IMTUser::Login](../IMTUser/Login.md)
  * [IMTUser::Group](../IMTUser/Group.md)
  * [IMTUser::PhonePassword](../IMTUser/PhonePassword.md)
  * [IMTUser::PassworHash](../IMTUser/PasswordHash.md)
  * [IMTUser::Name](../IMTUser/Name.md)
  * [IMTUser::Rights](../IMTUser/Rights.md)
  * [IMTUser::MQID](../IMTUser/MQID.md)
  * [IMTUser::Registration](../IMTUser/Registration.md)
  * [IMTUser::LastAccess](../IMTUser/LastAccess.md)
  * [IMTUser::LastIP](../IMTUser/LastIP.md)
  * [IMTUser::Language](../IMTUser/Language.md)
  * [IMTUser::Balance](../IMTUser/Balance.md)
  * [IMTUser::Credit](../IMTUser/Credit.md)
  * [IMTUser::Commission*](../IMTUser/CommissionAgentDaily.md)
  * [IMTUser::Leverage](../IMTUser/Leverage.md)
  * [IMTUser::Agent](../IMTUser/Agent.md)
  * [IMTUser::ExternalAccount*](../IMTUser/ExternalAccountAdd.md)


