[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Clients](../Clients.md) / UserPasswordCheck

[Previous](UserGet.md) | [Next](UserPasswordChange.md)

# MT5WebAPI.UserPasswordCheck

Check a client's password.
    
    
    MTRetCode  MT5WebAPI.UserPasswordCheck(
       ulong                  login,     // Login
       string                 password,  // Password
       MTUser.EnUserPasswords type       // Type of password
       )

### Parameters

**login**  
[in] The login of a client.

**password**  
[in] The password to check.

**type**  
[in] The type of password to check. Passed using theMTUser.EnUserPasswordsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code. For example, code [MT_RET_USR_INVALID_PASSWORD](../../../../../Return-Codes/User-management.md) indicates that the password is incorrect.

# MT5WebAPI.UserPasswordCheck

Checking the master password of the client.
    
    
    MTRetCode  MT5WebAPI.UserPasswordCheck(
       ulong                  login,     // Login
       string                 password   // Password
       )

### Parameters

**login**  
[in] The login of a client.

**password**  
[in] The password to check.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code. For example, code [MT_RET_USR_INVALID_PASSWORD](../../../../../Return-Codes/User-management.md) indicates that the password is incorrect.
