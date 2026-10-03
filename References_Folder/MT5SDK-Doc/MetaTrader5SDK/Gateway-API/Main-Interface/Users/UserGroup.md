[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserGroup

[Previous](UserGetByAccount.md) | [Next](UserLogins.md)

# IMTGatewayAPI::UserGroup

Get the group of a client by the login.

C++
    
    
    MTAPIRES  IMTGatewayAPI::UserGroup(
       const UINT64  login,     // Client login
       MTAPISTR&     group      // Client group
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.UserGroup(
       ulong         login,     // Client login
       out string    group      // Client group
       )

### Parameters

**login**  
[in] The login of a client.

**group**  
[out] The name of a user group to which the client belongs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A gateway can only access groups, which are specified in the gateway configuration (the Groups tab in MetaTrader 5 Administrator the Groups tab). To get the list of available groups, use [IMTConGateway::Group*](../../../Configuration-Interfaces/Gateways/IMTConGateway/GroupNext.md) methods.
