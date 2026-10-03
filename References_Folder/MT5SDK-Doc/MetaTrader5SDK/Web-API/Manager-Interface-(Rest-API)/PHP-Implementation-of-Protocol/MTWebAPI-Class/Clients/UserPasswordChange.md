[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserPasswordChange

[Previous](UserPasswordCheck.md) | [Next](UserAccountGet.md)

# MTWebAPI::UserPasswordChange

Change a client's password.
    
    
    MTAPIRES  MTWebAPI::UserPasswordChange(
       int     $login,                                         // Login
       string  $password,                                      // Password
       string  $type=MTProtocolConsts::WEB_VAL_USER_PASS_MAIN  // Type of password
       )

### Parameters

**$login**  
[in] The login of a client.

**$password**  
[in] A new password.

**$type=MTProtocolConsts::WEB_VAL_USER_PASS_MAIN**  
[in] The type of password to change. Passed using the following Web API constants: MTProtocolConsts::WEB_VAL_USER_PASS_MAIN - master password, MTProtocolConsts::WEB_VAL_USER_PASS_INVESTOR - investor password.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The password must contain at least two of three types of characters (lower case, upper case and digits) and meet the minimum length requirements set for the [group](../../../Configuration-Databases/Groups.md).
