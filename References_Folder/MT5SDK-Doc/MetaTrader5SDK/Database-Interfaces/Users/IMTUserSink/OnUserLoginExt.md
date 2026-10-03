[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserLoginExt

[Previous](OnUserLogin.md) | [Next](OnUserLogout.md)

# IMTUserSink::OnUserLoginExt

An extended handler of the event of an account's connection to the server. Passes an extended description of the connection.

C++
    
    
    virtual void  IMTUserSink::OnUserLoginExt(
       const IMTUser*          user,   // A pointer to the account object
       const IMTOnline*        online  // A pointer to the connection object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserLoginExt(
       CIMTUser                user,   // Account object
       CIMTOnline              online  // Connection object
       )

### Parameters

**user**  
[in] A pointer to theIMTUserobject.

**online**  
[in] A pointer to theIMTOnlineconnection description object.

### Note

This method is called by the API to notify that an account has connected to a server. Not used in the Gateway API.

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


