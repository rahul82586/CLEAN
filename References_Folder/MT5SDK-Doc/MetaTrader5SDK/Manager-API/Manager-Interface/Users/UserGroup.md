[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserGroup

[Previous](UserRequestByLogins.md) | [Next](UserLogins.md)

# IMTManagerAPI::UserGroup

Get the group of a client by the login.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserGroup(
       const UINT64  login,     // Client login
       MTAPISTR&     group      // Client group
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserGroup(
       ulong         login,     // Client login
       out string    group      // Client group
       )

Python
    
    
    ManagerAPI.UserGroup(
       login         # Client login
       )

### Parameters

**login**  
[in] The login of a client.

**group**  
[out] The name of a user group to which the client belongs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_USERS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
