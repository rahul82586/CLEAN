[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserPasswordChange

[Previous](UserPasswordCheck.md) | [Next](UserDepositChange.md)

# IMTServerAPI::UserPasswordChange

Change the user's password.
    
    
    MTAPIRES  IMTServerAPI::UserPasswordChange(
       const UINT    type,         // Type of password
       const UINT64  login,        // User's login
       LPCWSTR       password      // New password
       )

### Parameters

**type**  
[in] The type of a password to change is specified using theIMTUSer::EnUsersPasswordsenumeration.

**login**  
[in] The login of a user whose password should be changed.

**password**  
[in] A new password. The password must contain four character types: lowercase letters, uppercase letters, numbers, andspecial characters(#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings (IMTConGroup::AuthPasswordMin), while the lowest possible value is 8 characters. The maximum length is 16 characters.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.
