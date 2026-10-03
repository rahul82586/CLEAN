[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / TotalOrdersHistory

[Previous](TotalOrders.md) | [Next](TotalPositions.md)

# IMTConServerTrade::TotalOrdersHistory

Get the total number of [orders](../../../Database-Interfaces/Trade/Orders.md) in the history on the trade server.

C++
    
    
    UINT  IMTConServerTrade::TotalOrdersHistory()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerTrade.TotalOrdersHistory()

Python (Manager API)
    
    
    MTConServerTrade.TotalOrdersHistory

### Return Value

The total number of orders in the history.

### Note

[Filled, canceled, expired and rejected orders (#enorderstate)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate) appear in the history of orders.
