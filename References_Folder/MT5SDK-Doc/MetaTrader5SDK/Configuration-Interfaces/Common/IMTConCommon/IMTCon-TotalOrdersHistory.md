[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon TotalOrdersHistory

[Previous](IMTCon-TotalOrders.md) | [Next](IMTCon-TotalPositions.md)

# IMTConCommon::TotalOrdersHistory

Get the total number of [orders](../../../Database-Interfaces/Trade/Orders.md) in the history in the whole trading platform (on all trade server).

C++
    
    
    UINT  IMTConCommon::TotalOrdersHistory()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.TotalOrdersHistory()

Python (Manager API)
    
    
    MTConCommon.TotalOrdersHistory

### Return Value

The total number of orders in the history.

### Note

[Filled, canceled, expired and rejected orders (#enorderstate)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate) appear in the history of orders.
