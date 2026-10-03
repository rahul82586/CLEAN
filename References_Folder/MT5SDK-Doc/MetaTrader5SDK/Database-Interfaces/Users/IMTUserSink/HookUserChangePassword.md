[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / HookUserChangePassword

[Previous](HookUserLoginExt.md) | [Next](HookUserArchive.md)

# IMTUserSink::HookUserChangePassword

Account password change event hook.
    
    
    virtual MTAPIRES  IMTUserSink::HookUserChangePassword(
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

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

This method is called by the API to notify that the account password has changed. The handler is called before the record is updated.
