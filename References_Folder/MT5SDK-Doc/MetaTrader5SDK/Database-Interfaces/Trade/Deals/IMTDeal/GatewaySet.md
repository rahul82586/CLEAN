[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / GatewaySet

[Previous](Gateway.md) | [Next](PriceGateway.md)

# IMTDeal::GatewaySet

Sets the [ID of the gateway](../../../../Structures/MTGatewayInfo.md) (module_id), using which the deal was executed.

C++
    
    
    MTAPIRES  IMTDeal::GatewaySet(
       LPCWSTR  gateway      // The gateway ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.GatewaySet(
       string   gateway      // The gateway ID
       )

### Parameters

**gateway**  
[in] The ID of the gateway, corresponds toIMTConGateway::ID.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.
