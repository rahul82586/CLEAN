[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserGet

[Previous](UserTotal.md) | [Next](UserGetByGroup.md)

# IMTManagerAPI::UserGet

Get a user by the login.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserGet(
       const UINT64  login,     // Client login
       IMTUser*      user       // An object of the client record
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserGet(
       ulong         login,     // Client login
       CIMTUser      user       // An object of the client record
       )

Python
    
    
    ManagerAPI.UserGet(
       int           login      # Client login
       )

### Parameters

**login**  
[in] The login of a client.

**user**  
[out] An object of the client login. The user object must first be created using theIMTManagerAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified login to the user object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_USERS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
