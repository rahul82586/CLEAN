[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Network](../Network.md) / IMTConServerTrade

[Previous](IMTConServer/ClusterStateGet.md) | [Next](IMTConServerTrade/Enumerations.md)

# IMTConServerTrade

The IMTConServerTrade interface contains methods for managing settings that are specific to Trade Servers.

Method | Purpose  
---|---  
[Release](IMTConServerTrade/Release.md) | Delete the current object.  
[Assign](IMTConServerTrade/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConServerTrade/Clear.md) | Clear an object.  
[DemoMode](IMTConServerTrade/DemoMode.md) | Gets and sets demo account allocation mode.  
[DemoPeriod](IMTConServerTrade/DemoPeriod.md) | Gets and sets demo account validity period.  
[OvernightMode](IMTConServerTrade/OvernightMode.md) | Get and set the mode of transition to the next day.  
[OvernightTime](IMTConServerTrade/OvernightTime.md) | Get and set the time of transition to the next day.  
[OvernightTimeLast](IMTConServerTrade/OvernightTimeLast.md) | Get the time of the last transition to the next day.  
[OvernightTimePrev](IMTConServerTrade/OvernightTimePrev.md) | Get the time of the last but one transition to the next day.  
[OvernightDays](IMTConServerTrade/OvernightDays.md) | Gets and sets the schedule of operations related to the end of the trading day.  
[OvermonthMode](IMTConServerTrade/OvermonthMode.md) | Get and set the mode of transition to the next month.  
[OvermonthTimeLast](IMTConServerTrade/OvermonthTimeLast.md) | Get the time of the last transition to the next month.  
[OvermonthTimePrev](IMTConServerTrade/OvermonthTimePrev.md) | Get the time of the last but one transition to the next month.  
[LoginsRangeAdd](IMTConServerTrade/LoginsRangeAdd.md) | Add a range of logins.  
[LoginsRangeUpdate](IMTConServerTrade/LoginsRangeUpdate.md) | Update a range of logins.  
[LoginsRangeDelete](IMTConServerTrade/LoginsRangeDelete.md) | Delete a range of logins by the index.  
[LoginsRangeClear](IMTConServerTrade/LoginsRangeClear.md) | Clear the list of logins.  
[LoginsRangeShift](IMTConServerTrade/LoginsRangeShift.md) | Move the list of logins in the list.  
[LoginsRangeTotal](IMTConServerTrade/LoginsRangeTotal.md) | Get the number of login ranges of a trade server.  
[LoginsRangeNext](IMTConServerTrade/LoginsRangeNext.md) | Get a range of logins by the index.  
[OrdersRangeAdd](IMTConServerTrade/OrdersRangeAdd.md) | Add a range of orders.  
[OrdersRangeUpdate](IMTConServerTrade/OrdersRangeUpdate.md) | Update a range of orders.  
[OrdersRangeDelete](IMTConServerTrade/OrdersRangeDelete.md) | Delete a range of orders by the index.  
[OrdersRangeClear](IMTConServerTrade/OrdersRangeClear.md) | Clear the list of orders.  
[OrdersRangeShift](IMTConServerTrade/OrdersRangeShift.md) | Move the list of orders in the list.  
[OrdersRangeTotal](IMTConServerTrade/OrdersRangeTotal.md) | Get the number of ranges of orders of a trade server.  
[OrdersRangeNext](IMTConServerTrade/OrdersRangeNext.md) | Gets a range of orders at the specified index.  
[DealsRangeAdd](IMTConServerTrade/DealsRangeAdd.md) | Add a range of orders.  
[DealsRangeUpdate](IMTConServerTrade/DealsRangeUpdate.md) | Update a range of orders.  
[DealsRangeDelete](IMTConServerTrade/DealsRangeDelete.md) | Delete a range of deals by the index.  
[DealsRangeClear](IMTConServerTrade/DealsRangeClear.md) | Clears the range of deals.  
[DealsRangeShift](IMTConServerTrade/DealsRangeShift.md) | Move the list of deals in the list.  
[DealsRangeTotal](IMTConServerTrade/DealsRangeTotal.md) | Get the number of ranges of deals of a trade server.  
[DealsRangeNext](IMTConServerTrade/DealsRangeNext.md) | Get a range of deals by the index.  
[TotalUsers](IMTConServerTrade/TotalUsers.md) | Get the total number of client accounts on the trade server.  
[TotalUsersReal](IMTConServerTrade/TotalUsersReal.md) | Get the total number of real clients on the trade server.  
[TotalDeals](IMTConServerTrade/TotalDeals.md) | Get the total number of deals executed on the trade server.  
[TotalOrders](IMTConServerTrade/TotalOrders.md) | Get the total number of active orders placed on the trade server.  
[TotalOrdersHistory](IMTConServerTrade/TotalOrdersHistory.md) | Get the total number of orders in the history on the trade server.  
[TotalPositions](IMTConServerTrade/TotalPositions.md) | Get the total number of positions on the trade server.  
  
The IMTConServerTrade class contains the following enumerations:

Method | Purpose  
---|---  
[EnDemoMode (#endemomode)](IMTConServerTrade/Enumerations.md#endemomode) | Mode of demo account allocation.  
[EnOvernightMode (#enovernightmode)](IMTConServerTrade/Enumerations.md#enovernightmode) | The overnight mode.  
[EnOvermonthMode (#enovermonthmode)](IMTConServerTrade/Enumerations.md#enovermonthmode) | The overmonth mode.  
[EnOvernightDays (#enovernightdays)](IMTConServerTrade/Enumerations.md#enovernightdays) | The schedule of operations related to the end of the trading day.
