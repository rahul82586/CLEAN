[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Trade](../Trade.md) / Orders

[Previous](../Trade.md) | [Next](Orders/OrderCreate.md)

# Orders

The MetaTrader 5 Server API allows managing a database of orders on a trade server. Using the server API, you can modify and delete orders, as well as handle events of changes in the database of deals.

An important feature of working with orders is that they are bound to a certain trade server. Accordingly, the plugin can manage only those orders that belong to the server where it is running.

Functions described in this section allow to manage the database of orders, as well subscribe and unsubscribe from events associated with changes in the order base.

Function | Purpose  
---|---  
[OrderCreate](Orders/OrderCreate.md) | Create an object of a trade order.  
[OrderCreateArray](Orders/OrderCreateArray.md) | Create an object of the array of orders.  
[OrderSubscribe](Orders/OrderSubscribe.md) | Subscribe to events and hooks associated with changes in the database of open orders.  
[OrderUnsubscribe](Orders/OrderUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the database of open orders.  
[OrderAdd](Orders/OrderAdd.md) | Add an open order to the server database.  
[OrderAddBatch](Orders/OrderAddBatch.md) | Add open orders to a server database in bulk.  
[OrderAddBatchArray](Orders/OrderAddBatchArray.md) | Add open orders to a server database in bulk.  
[OrderUpdate](Orders/OrderUpdate.md) | Update an open trade order in the server data base.  
[OrderUpdateBatch](Orders/OrderUpdateBatch.md) | Update open orders in a server database in bulk.  
[OrderUpdateBatchArray](Orders/OrderUpdateBatchArray.md) | Update open orders in a server database in bulk.  
[OrderDelete](Orders/OrderDelete.md) | Delete an open trade order from the server data base.  
[OrderDeleteBatch](Orders/OrderDeleteBatch.md) | Delete open orders from a server database in bulk.  
[OrderCancel](Orders/OrderCancel.md) | Move an open trading order to history.  
[OrderCancelBatch](Orders/OrderCancelBatch.md) | Move multiple open order to history.  
[OrderGet](Orders/OrderGet.md) | Get open trade orders based on the ticket or login.  
[OrderGetByGroup](Orders/OrderGetByGroup.md) | Get open orders for a client group.  
[OrderGetByGroupSymbol](Orders/OrderGetByGroupSymbol.md) | Get open orders from the server by group and symbol.  
[OrderGetByLogins](Orders/OrderGetByLogins.md) | Receive open orders by the list of logins.  
[OrderGetByLoginsSymbol](Orders/OrderGetByLoginsSymbol.md) | Get open orders from the server by list of logins and symbol.  
[OrderGetByTickets](Orders/OrderGetByTickets.md) | Get open orders by the list of tickets.  
[OrderSelectByGroup](Orders/OrderSelectByGroup.md) | Request open orders from a database for a group of accounts using additional criteria.  
[OrderSelectByLogins](Orders/OrderSelectByLogins.md) | Request open orders from a database for a list of logins using additional criteria.  
[HistorySubscribe](Orders/HistorySubscribe.md) | Subscribe to events and hooks associated with changes in the database of closed orders.  
[HistoryUnsubscribe](Orders/HistoryUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the database of closed orders.  
[HistoryAdd](Orders/HistoryAdd.md) | Add a closed order to the server database.  
[HistoryAddBatch](Orders/HistoryAddBatch.md) | Add closed orders to a server database in bulk.  
[HistoryAddBatchArray](Orders/HistoryAddBatchArray.md) | Add closed orders to a server database in bulk.  
[HistoryUpdate](Orders/HistoryUpdate.md) | Update a closed trade order in the server database.  
[HistoryUpdateBatch](Orders/HistoryUpdateBatch.md) | Update closed orders in a server database in bulk.  
[HistoryUpdateBatchArray](Orders/HistoryUpdateBatchArray.md) | Update closed orders in a server database in bulk.  
[HisotryDelete](Orders/HistoryDelete.md) | Delete a closed trade order from the server database.  
[HistoryDeleteBatch](Orders/HistoryDeleteBatch.md) | Delete closed orders from a server database in bulk.  
[HistoryGet](Orders/HistoryGet.md) | Get closed trade orders by a ticket or login.  
[HistoryGetByTickets](Orders/HistoryGetByTickets.md) | Receive closed orders (history) related to a client group.  
[HistoryGetByLogins](Orders/HistoryGetByLogins.md) | Receive closed orders (history) related to the list of logins.  
[HistoryGetByLoginsSymbol](Orders/HistoryGetByLoginsSymbol.md) | Get closed orders (history) from the server by a list of logins and symbol.  
[HistoryGetByGroup](Orders/HistoryGetByGroup.md) | Receive closed orders (history) related to the list of tickets.  
[HistoryGetByGroupSymbol](Orders/HistoryGetByGroupSymbol.md) | Get closed orders (history) from the server by group and symbol.  
[HistorySelectByGroup](Orders/HistorySelectByGroup.md) | Request closed orders from a database for a group of accounts using additional criteria.  
[HistorySelectByLogins](Orders/HistorySelectByLogins.md) | Request closed orders from a database for a list of logins using additional criteria.  
[HistoryReopen](Orders/HistoryReopen.md) | Reopen a pending order from the client's history.
