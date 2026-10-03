[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Trade](../Trade.md) / Deals

[Previous](Orders/HistoryReopen.md) | [Next](Deals/DealCreate.md)

# Deals

The MetaTrader 5 Server API allows managing a database of deals on a trade server. Using the server API, you can modify and delete deals, as well as handle events of changes in the database of deals.

An important feature of working with deals is that they are bound to a certain trade server. Accordingly, the plugin can manage only those deals that belong to the server where it is running.

Functions described in this section allow to manage the database of deals, as well subscribe and unsubscribe from events associated with changes in the deal base.

Function | Purpose  
---|---  
[DealCreate](Deals/DealGet.md) | Create an object of a deal.  
[DealCreateArray](Deals/DealCreateArray.md) | Create an object of the array of deals.  
[DealSubscribe](Deals/DealSubscribe.md) | Subscribe to events and hooks associated with changes in the database of deals.  
[DealUnsubscribe](Deals/DealUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the database of deals.  
[DealAdd](Deals/DealAdd.md) | Add a deal to the server database.  
[DealAddBatch](Deals/DealAddBatch.md) | Add deals to a server database in bulk.  
[DealAddBatchArray](Deals/DealAddBatchArray.md) | Add deals to a server database in bulk.  
[DealUpdate](Deals/DealUpdate.md) | Update a deal in the server database.  
[DealUpdateBatch](Deals/DealUpdateBatch.md) | Update multiple deals in the server database.  
[DealUpdateBatchArray](Deals/DealUpdateBatchArray.md) | Update multiple deals in the server database.  
[DealDelete](Deals/DealDelete.md) | Delete a deal from the server database.  
[DealDeleteBatch](Deals/DealDeleteBatch.md) | Delete multiple deals from the server database.  
[DealGet](Deals/DealGet.md) | Get a deal by a ticket and login.  
[DealGetByGroup](Deals/DealGetByGroup.md) | Get deals related to a group of accounts.  
[DealGetByGroupSymbol](Deals/DealGetByGroupSymbol.md) | Get deals by group and symbol.  
[DealGetByLogins](Deals/DealGetByLogins.md) | Get deals by the list of logins.  
[DealGetByLoginsSymbol](Deals/DealGetByLoginsSymbol.md) | Get deals by a list of logins and symbol.  
[DealGetByTickets](Deals/DealGetByTickets.md) | Get deals by the list of tickets.  
[DealSelectByGroup](Deals/DealSelectByGroup.md) | Request deals from a database for a group of accounts using additional criteria.  
[DealSelectByLogins](Deals/DealSelectByLogins.md) | Request deals from a database for a list of logins using additional criteria.  
[DealPerform](Deals/DealPerform.md) | Execute a deal on the client's account. This method performs a market buy or sell operation on an account, as if it is performed by the client through the terminal.  
[DealPerformCloseBy](Deals/DealPerformCloseBy.md) | Close a position by an opposite one. This method performs a Close By operation, as if it is performed by the client through the terminal.  
[DealPerformBatch](Deals/DealPerformBatch.md) | Perform multiple deals on the client's account. This method performs market buy or sell operations on the account as if they were performed by the client through the terminal.  
[DealPerformBatchArray](Deals/DealPerformBatchArray.md) | Perform multiple deals on the client's account. This method performs market buy or sell operations on the account as if they were performed by the client through the terminal.
