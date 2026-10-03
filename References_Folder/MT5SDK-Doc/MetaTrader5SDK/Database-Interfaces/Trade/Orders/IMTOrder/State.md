[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / State

[Previous](ContractSize.md) | [Next](StateSet.md)

# IMTOrder::State

Get the current state of an order.

C++
    
    
    UINT  IMTOrder::State()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTOrder.State()

Python
    
    
    MTOrder.State()

### Return Value

A value of the [IMTOrder::EnOrderState (#enorderstate)](Enumerations.md#enorderstate) enumeration.
