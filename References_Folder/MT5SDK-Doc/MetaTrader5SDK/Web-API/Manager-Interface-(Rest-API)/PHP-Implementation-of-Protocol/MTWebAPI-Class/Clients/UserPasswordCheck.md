[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserPasswordCheck

[Previous](UserGet.md) | [Next](UserPasswordChange.md)

# MTWebAPI::UserPasswordCheck

Check a client's password.
    
    
    MTAPIRES  MTWebAPI::UserPasswordCheck(
       int     $login,                                         // Login
       string  $password,                                      // Password
       string  $type=MTProtocolConsts::WEB_VAL_USER_PASS_MAIN  // Type of password
       )

### Parameters

**$login**  
[in] The login of a client.

**$password**  
[in] The password to check.

**$type=MTProtocolConsts::WEB_VAL_USER_PASS_MAIN**  
[in] The type of password to check. Passed using the following Web API constants: MTProtocolConsts::WEB_VAL_USER_PASS_MAIN - master password, MTProtocolConsts::WEB_VAL_USER_PASS_INVESTOR - investor password.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code. For example, code [MT_RET_USR_INVALID_PASSWORD](../../../../../Return-Codes/User-management.md) indicates that the password is incorrect.

### Note

The strings specifying the password and the password type must be passed in the UTF-8 format.
