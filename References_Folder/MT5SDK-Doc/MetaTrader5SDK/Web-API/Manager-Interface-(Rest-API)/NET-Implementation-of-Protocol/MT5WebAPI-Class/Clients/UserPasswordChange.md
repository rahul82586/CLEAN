[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Clients](../Clients.md) / UserPasswordChange

[Previous](UserPasswordCheck.md) | [Next](UserAccountGet.md)

# MT5WebAPI.UserPasswordChange

Change a client's password.
    
    
    MTRetCode  MT5WebAPI.UserPasswordChange(
       ulong                  login,     // Login
       string                 password,  // Password
       MTUser.EnUserPasswords type       // Type of password
       )

### Parameters

**login**  
[in] The login of a client.

**password**  
[in] A new password.

**type**  
[in] The type of password to change.. Passed using theMTUser.EnUserPasswordsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The password must contain at least two of three types of characters (lower case, upper case and digits) and meet the minimum length requirements set for the [group](../../../Configuration-Databases/Groups.md).

# MT5WebAPI.UserPasswordChange

Changing the master password of the client.
    
    
    MTRetCode  MT5WebAPI.UserPasswordChange(
       ulong   login,         // Login
       string  password       // Password
       )

### Parameters

**login**  
[in] The login of a client.

**password**  
[in] A new password.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The password must contain at least two of three types of characters (lower case, upper case and digits) and meet the minimum length requirements set for the [group](../../../Configuration-Databases/Groups.md).
