[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserLogin

[Previous](HookUserDelete.md) | [Next](HookUserLoginExt.md)

# IMTUserSink::HookUserLogin

A hook of an account's connection to the server.
    
    
    virtual MTAPIRES  IMTUserSink::HookUserLogin(
       LPCWSTR                 ip,    // IP address
       const IMTUser*          user,  // An object of an account
       const UINT              type   // Type of connection
       )

.NET(Gateway/Manager API)
    
    
    virtual MTRetCoed  CIMTUserSink.HookUserLogin(
       string                  ip,    // IP address
       CIMTUser                user,  // Account object
       EnUsersConnectionTypes  type   // Type of connection
       )

### Parameters

**ip**  
[in] The IP address, from which connection is established.

**user**  
[in] A pointer to theIMTUserobject of an account.

**type**  
[in] Type of connection, passed using theEnUsersConnectionTypesenumeration.

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


