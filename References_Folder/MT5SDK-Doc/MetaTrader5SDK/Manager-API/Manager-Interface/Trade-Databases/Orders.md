[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Trade Databases](../Trade-Databases.md) / Orders

[Previous](../Trade-Databases.md) | [Next](Orders/OrderCreate.md)

# Orders

Functions allow to view the database of trade orders, as well subscribe and unsubscribe from events associated with changes in the order base.

The following functions are available for this purpose:

Function | Purpose  
---|---  
[OrderCreate](Orders/OrderCreate.md) | Create an object of a trade order.  
[OrderCreateArray](Orders/OrderCreateArray.md) | Create an object of the array of orders.  
[OrderSubscribe](Orders/OrderSubscribe.md) | Subscribe to the events associated with changes in the database of orders.  
[OrderUnsubscribe](Orders/OrderUnsubscribe.md) | Unsubscribe from the events associated with changes in the database of orders.  
[OrderGet](Orders/OrderGet.md) | Get a currently unfulfilled order by a ticket.  
[OrderGetOpen](Orders/OrderGetOpen.md) | Get currently unfulfilled orders of a client.  
[OrderGetByGroup](Orders/OrderGetByGroup.md) | Request from the server open orders related to a client group.  
[OrderGetByLogins](Orders/OrderGetByLogins.md) | Receive currently open orders by the list of logins.  
[OrderGetByTickets](Orders/OrderGetByTickets.md) | Receive currently open orders by the list of tickets.  
[OrderGetBySymbol](Orders/OrderGetBySymbol.md) | Receive currently open orders by groups and symbol.  
[OrderRequest](Orders/OrderRequest.md) | Request a trade order from a server by the ticket.  
[OrderRequestOpen](Orders/OrderRequestOpen.md) | Request from the server currently unfulfilled orders of a client.  
[OrderRequestByGroup](Orders/OrderRequestByGroup.md) | Request from the server open orders related to a client group.  
[OrderRequestByGroupSymbol](Orders/OrderRequestByGroupSymbol.md) | Request open orders from the server by group and symbol.  
[OrderRequestByLogins](Orders/OrderRequestByLogins.md) | Request from the server open orders related to the list of logins.  
[OrderRequestByLoginsSymbol](Orders/OrderRequestByLoginsSymbol.md) | Request open orders from the server by list of logins and symbol.  
[OrderRequestByTickets](Orders/OrderRequestByTickets.md) | Request from the server open orders by the list of tickets.  
[OrderAdd](Orders/OrderAdd.md) | Add an open order the server database.  
[OrderAddBatch](Orders/OrderAddBatch.md) | Add a batch of open orders to the server database.  
[OrderAddBatchArray](Orders/OrderAddBatchArray.md) | Add a batch of open orders to the server database.  
[OrderUpdate](Orders/OrderUpdate.md) | Update a trade order.  
[OrderUpdateBatch](Orders/OrderUpdateBatch.md) | Update multiple orders in a server database.  
[OrderUpdateBatchArray](Orders/OrderUpdateBatchArray.md) | Update multiple orders in a server database.  
[OrderDelete](Orders/OrderDelete.md) | Delete a trade order.  
[OrderDeleteBatch](Orders/OrderDeleteBatch.md) | Delete orders from the server database in bulk.  
[OrderCancel](Orders/OrderCancel.md) | Move an open trading order to history.  
[OrderCancelBatch](Orders/OrderCancelBatch.md) | Move multiple open order to history.  
[HistoryRequest](Orders/HistoryRequest.md) | Request from the server the client's closed orders (history) in the specified date range.  
[HistoryRequestByGroup](Orders/HistoryRequestByGroup.md) | Request from the server closed orders (history) related to a client group.  
[HistoryRequestByGroupSymbol](Orders/HistoryRequestByGroupSymbol.md) | Request closed orders (history) from the server by group and symbol.  
[HistoryRequestByLogins](Orders/HistoryRequestByLogins.md) | Request from the server the closed orders (history) related to the list of logins.  
[HistoryRequestByLoginsSymbol](Orders/HistoryRequestByLoginsSymbol.md) | Request closed orders (history) from the server by list of logins and symbol.  
[HistoryRequestByTickets](Orders/HistoryRequestByTickets.md) | Request from the server the closed orders (history) related to the list of tickets.  
[HistoryRequestPage](Orders/HistoryRequestPage.md) | Request from the server client's closed orders (history) in a paged form.
