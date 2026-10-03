[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / ModificationFlags

[Previous](RateMargin.md) | [Next](../IMTOrderArray.md)

# IMTOrder::ModificationFlags

Gets the order modification flags. The flags allow defining if an order was changed manually by an administrator, manager or API.

C++
    
    
    UINT  IMTOrder::ModificationFlags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTOrder.ModificationFlags()

Python
    
    
    MTOrder.ModificationFlags()

### Return Value

[IMTOrder::EnTradeModifyFlags (#entrademodifyflags)](Enumerations.md#entrademodifyflags) enumeration value.
