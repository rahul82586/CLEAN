[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserRequest

[Previous](UserGetByLogins.md) | [Next](UserRequestArray.md)

# IMTManagerAPI::UserRequest

Request a client record by the login from a server.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserRequest(
       const UINT64  login,     // Client login
       IMTUser*      user       // An object of the client record
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserRequest(
       ulong         login,     // Client login
       CIMTUser      obj        // An object of the client record
       )

Python
    
    
    ManagerAPI.UserRequest(
       login         # Client login
       )

### Parameters

**login**  
[in] The login of a client.

***user**  
[out] An object of the client login. The user object must first be created using theIMTManagerAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified login to the user object.
