[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserChangePassword

[Previous](OnUserLogoutExt.md) | [Next](OnUserSync.md)

# IMTUserSink::OnUserChangePassword

Account password change event handler.
    
    
    virtual void  IMTUserSink::OnUserChangePassword(
       const IMTUser*   user,       // A pointer to the account object
       const UINT       type,       // Password type
       LPCWSTR          password    // Password
       )

### Parameters

**user**  
[in] A pointer to theIMTUseraccount object.

**type**  
[in] The type of the password being changed. The type is passed using theIMTUser::EnUsersPasswordsenumeration.

**password**  
[in] New account password.

### Note

This method is called by the API to notify that the account password has changed. The handler is called before the record is updated.
