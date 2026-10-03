[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Gateway

[Previous](ReasonSet.md) | [Next](GatewaySet.md)

# IMTDeal::Gateway

Gets the [ID of a trade gateway](../../../../Structures/MTGatewayInfo.md) (module_id), using which the deal was executed.

C++
    
    
    LPCWSTR  IMTDeal::Gateway()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDeal.Gateway()

### Return Value

If successful, it returns a pointer to the string with the identifier. If the gateway was not involved in the deal execution or no ID is set for the gateway, a zero value is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDeal](../IMTDeal.md) object.
