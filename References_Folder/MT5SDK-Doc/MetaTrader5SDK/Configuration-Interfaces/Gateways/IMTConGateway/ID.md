[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / ID

[Previous](Name.md) | [Next](Module.md)

# IMTConGateway::ID

Gets the gateway identifier. This ID is specified in the [IMTDeal::Dealer](../../../Database-Interfaces/Trade/Deals/IMTDeal/Dealer.md) fields of trades performed through the gateway. It is also used when creating [routing rules](../../Routing.md) for trade requests forwarded to the gateway.

C++
    
    
    UINT64  IMTConGateway::ID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGateway.ID()

Python (Manager API)
    
    
    MTConGateway.ID

### Return Value

The gateway ID.

# IMTConGateway::ID

Sets the gateway identifier. This ID is specified in the [IMTDeal::Dealer](../../../Database-Interfaces/Trade/Deals/IMTDeal/Dealer.md) fields of trades performed through the gateway. It is also used when creating [routing rules](../../Routing.md) for trade requests forwarded to the gateway.

C++
    
    
    MTAPIRES  IMTConGateway::ID(
       UINT64  id      // Gateway ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.ID(
       ulong   id      // Gateway ID
       )

Python (Manager API)
    
    
    MTConGateway.ID

### Parameters

**name**  
[in] The identifier of a gateway.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The Gateway ID should be unique, it must not match any of existing [manager accounts](../../Managers/IMTConManager/Login.md). When adding a new gateway or editing an existing one, the gateway ID is verified. If the ID value is invalid, gateway settings will not be added or updated accordingly.
