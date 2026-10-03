[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / PriceGatewaySet

[Previous](PriceGateway.md) | [Next](MarketBid.md)

# IMTDeal::PriceGatewaySet

Sets the actual price of a deal executed via a gateway in an external trading system.

C++
    
    
    MTAPIRES  IMTDeal::PriceGatewaySet(
       const double  price_gateway  // Price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.PriceGatewaySet(
       double        price_gateway  // Price
       )

### Parameters

**price_gateway**  
[in] The actual price, at which a deal was executed in an external trading system.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.

### Note

Gateways have the built-in [price markup](../../../../Configuration-Interfaces/Gateways/IMTConGatewayTranslate.md) option, which can be applied to prices provided by an external system. The markup is applied to prices featured in the Market Watch as well as to prices, at which deals are executed on the platform side. The actual price at which the deal was executed on the external system side (excluding the markup) is written in the PriceGateway field.
