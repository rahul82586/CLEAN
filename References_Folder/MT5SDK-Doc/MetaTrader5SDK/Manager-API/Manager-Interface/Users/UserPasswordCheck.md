[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserPasswordCheck

[Previous](UserLogins.md) | [Next](UserPasswordChange.md)

# IMTManagerAPI::UserPasswordCheck

Check the user's password.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserPasswordCheck(
       const UINT    type,         // Type of password
       const UINT64  login,        // User's login
       LPCWSTR       password      // User's password
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserPasswordCheck(
       CIMTUser.EnUsersPasswords  type,     // Type of password
       ulong                      login,    // User's login
       string                     password  // User's password
       )

Python
    
    
    ManagerAPI.UserPasswordCheck(
       type,                      # Type of password
       login,                     # User's login
       password                   # User's password
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
