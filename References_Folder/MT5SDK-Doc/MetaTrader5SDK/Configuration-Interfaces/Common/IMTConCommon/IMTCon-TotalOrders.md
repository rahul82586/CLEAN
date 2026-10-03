[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon TotalOrders

[Previous](IMTCon-TotalDeals.md) | [Next](IMTCon-TotalOrdersHistory.md)

# IMTConCommon::TotalOrders

Get the total number of active [orders](../../../Database-Interfaces/Trade/Orders.md) placed in the whole trading platform (on all trade servers).

C++
    
    
    UINT  IMTConCommon::TotalOrders()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.TotalOrders()

Python (Manager API)
    
    
    MTConCommon.TotalOrders

### Return Value

The total number of orders.

### Note

Active orders include all pending orders and the orders awaiting processing (state [placed and started (#enorderstate)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate)).
