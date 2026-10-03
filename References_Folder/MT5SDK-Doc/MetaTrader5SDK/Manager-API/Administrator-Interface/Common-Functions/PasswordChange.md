[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Common Functions](../Common-Functions.md) / PasswordChange

[Previous](LicenseCheck.md) | [Next](../Connection-to-the-Server.md)

# IMTAdminAPI::PasswordChange

Change password of an account that is used to [connect](../Connection-to-the-Server/Connect.md) the application to the server.

C++
    
    
    MTAPIRES  IMTAdminAPI::PasswordChange(
       const UINT    type,         // Type of password
       LPCWSTR       password      // New password
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PasswordChange(
       uint          type,         // Type of password
       string        password      // New password
       )

Python
    
    
    AdminAPI.PasswordChange(
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
