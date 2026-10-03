[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserTotal

[Previous](UserUnsubscribe.md) | [Next](UserGet.md)

# IMTGatewayAPI::UserTotal

Get the total number of users in groups available to the gateway.

C++
    
    
    UINT  IMTGatewayAPI::UserTotal()

.NET
    
    
    uint  CIMTGatewayAPI.UserTotal()

### Return Value

The number of users in groups available to the gateway.

### Note

A gateway can only access groups, which are specified in the gateway configuration (the Groups tab in MetaTrader 5 Administrator the Groups tab). To get the list of available groups, use [IMTConGateway::Group*](../../../Configuration-Interfaces/Gateways/IMTConGateway/GroupNext.md) methods.
