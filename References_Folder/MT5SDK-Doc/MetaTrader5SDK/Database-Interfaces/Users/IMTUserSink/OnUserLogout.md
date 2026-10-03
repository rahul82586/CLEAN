[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserLogout

[Previous](OnUserLoginExt.md) | [Next](OnUserLogoutExt.md)

# IMTUserSink::OnUserLogout

A handler of the event of an account's disconnection from the server.

C++
    
    
    virtual void  IMTUserSink::OnUserLogout(
       LPCWSTR                 ip,    // IP address
       const IMTUser*          user,  // A pointer to an object of an account
       const UINT              type   // Type of connection
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserLogout(
       string                  ip,    // IP address
       CIMTUser                user,  // Account object
       EnUsersConnectionTypes  type   // Type of connection
       )

### Parameters

**ip**  
[in] The IP address, from which the account connected.

**user**  
[in] A pointer to the object of an accountIMTUser.

**type**  
[in] Type of connection, passed using theIMTUser::EnUsersConnectionTypesenumeration.

### Note

This method is called by the API to notify that an account has disconnected from the server. The method is not used in Gateway API.

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


