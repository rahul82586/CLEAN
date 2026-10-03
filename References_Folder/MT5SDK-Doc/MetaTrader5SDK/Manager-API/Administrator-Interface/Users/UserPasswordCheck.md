[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserPasswordCheck

[Previous](UserRequestByLogins.md) | [Next](UserPasswordChange.md)

# IMTAdminAPI::UserPasswordCheck

Check the user's password.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserPasswordCheck(
       const UINT    type,         // Type of password
       const UINT64  login,        // User's login
       LPCWSTR       password      // User's password
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserPasswordCheck(
       EnUsersPasswords  type,     // Type of password
       ulong             login,    // User's login
       string            password  // User's password
       )

Python
    
    
    AdminAPI.UserPasswordCheck(
       type,             # Type of password
       login,            # User's login
       password          # User's password
       )

### Parameters

**type**  
[in] The type of a password to check is specified using theIMTUser::EnUsersPasswordsenumeration.

**login**  
[in] The login of a user whose password should be checked.

**password**  
[in] A password to check.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
