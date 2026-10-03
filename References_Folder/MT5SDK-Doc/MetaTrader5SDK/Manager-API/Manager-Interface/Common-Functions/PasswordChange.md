[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Common Functions](../Common-Functions.md) / PasswordChange

[Previous](LicenseCheck.md) | [Next](../Connection-to-the-Server.md)

# IMTManagerAPI::PasswordChange

Change password of an account that is used to [connect](../Connection-to-the-Server/Connect.md) the application to the server.

C++
    
    
    MTAPIRES  IMTManagerAPI::PasswordChange(
       const UINT    type,         // Type of password
       LPCWSTR       password      // New password
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PasswordChange(
       uint          type,         // Type of password
       string        password      // New password
       )

Python
    
    
    ManagerAPI.PasswordChange(
       type,         # Type of password
       password      # New password
       )

### Parameters

**type**  
[in] The type of a password to change is specified using theIMTUSer::EnUsersPasswordsenumeration.

**password**  
[in] A new password.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The password must contain at least two of three types of characters (lower case, upper case and digits) and meet the minimum length requirements set for the group ([IMTConGroup::AuthPasswordMin](../../../Configuration-Interfaces/Groups/IMTConGroup/AuthPasswordMin.md)).
