[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / PriceGateway

[Previous](GatewaySet.md) | [Next](PriceGatewaySet.md)

# IMTDeal::PriceGateway

Gets the actual price of a deal executed via a gateway in an external trading system, not taking into account the [gateway price transformation settings](../../../../Configuration-Interfaces/Gateways/IMTConGateway/TranslateAdd.md).

C++
    
    
    double  IMTDeal::PriceGateway()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.PriceGateway()

### Return Value

The price at which the deal was executed.

### Note

Gateways have the built-in [price markup](../../../../Configuration-Interfaces/Gateways/IMTConGatewayTranslate.md) option, which can be applied to prices provided by an external system. The markup is applied to prices featured in the Market Watch as well as to prices, at which deals are executed on the platform side. The actual price at which the deal was executed on the external system side (excluding the markup) is written in the PriceGateway field.
