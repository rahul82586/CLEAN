[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserLogins

[Previous](UserGroup.md) | [Next](../Configuration-Databases.md)

# IMTGatewayAPI::UserLogins

Returns an array of logins of the clients available to the gateway.

C++
    
    
    MTAPIRES  IMTGatewayAPI::UserLogins(
       UINT64*&      logins,       // An array of client logins
       UINT&         logins_total  // The number of logins
       )

.NET
    
    
    ulong[]  CIMTGatewayAPI.UserLogins(
       out MTRetCode res           // Response code
       )

### Parameters

**logins**  
[out] An array of client logins.

**logins_total**  
[out] The number of logins in the logins array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A gateway can only access groups, which are specified in the gateway configuration (the Groups tab in MetaTrader 5 Administrator the Groups tab). To get the list of available groups, use [IMTConGateway::Group*](../../../Configuration-Interfaces/Gateways/IMTConGateway/GroupNext.md) methods.
