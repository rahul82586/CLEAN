[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / TotalOrders

[Previous](TotalDeals.md) | [Next](TotalOrdersHistory.md)

# IMTConServerTrade::TotalOrders

Get the total number of active [orders](../../../Database-Interfaces/Trade/Orders.md) placed on the trade server.

C++
    
    
    UINT  IMTConServerTrade::TotalOrders()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerTrade.TotalOrders()

Python (Manager API)
    
    
    MTConServerTrade.TotalOrders

### Return Value

The total number of orders.

### Note

Active orders include all pending orders and the orders awaiting processing (state [placed and started (#enorderstate)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate)).
