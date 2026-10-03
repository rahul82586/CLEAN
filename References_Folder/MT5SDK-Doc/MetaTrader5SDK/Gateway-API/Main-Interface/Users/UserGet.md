[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserGet

[Previous](UserTotal.md) | [Next](UserGetByAccount.md)

# IMTGatewayAPI::UserGet

Get a client record by the login.

C++
    
    
    MTAPIRES  IMTGatewayAPI::UserGet(
       const UINT64  login,     // Client login
       IMTUser*      user       // An object of the client record
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.UserGet(
       ulong         login,     // Client login
       CIMTUser      user       // An object of the client record
       )

### Parameters

**login**  
[in] The login of a client.

**user**  
[out] An object of the client login. The user object must first be created using theIMTGatewayAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method only copies to the 'user' object the client's login ([IMTUser::Login](../../../Database-Interfaces/Users/IMTUser/Login.md)), group ([IMTUser::Group](../../../Database-Interfaces/Users/IMTUser/Group.md)) and the number of the external system account associated with this gateway ([IMTUser::ExternalAccount*](../../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md)).
