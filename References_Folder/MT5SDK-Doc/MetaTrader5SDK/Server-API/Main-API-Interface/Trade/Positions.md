[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Trade](../Trade.md) / Positions

[Previous](Deals/DealPerformBatchArray.md) | [Next](Positions/PositionCreate.md)

# Positions

The MetaTrader 5 Server API allows managing a database of positions on a trade server. Using the server API, you can modify and delete positions, as well as handle events of changes in the database of deals.

An important feature of working with positions is that they are bound to a certain trade server. Accordingly, the plugin can manage only those positions that belong to the server where it is running.

> MetaTrader 5 Server API does not provide features for creating positions. Creating new positions can lead to irreversible damage of the position database of a server.

Functions described in this section allow to manage the database of positions, as well subscribe and unsubscribe from events associated with changes in the database of positions.

Function | Purpose  
---|---  
[PositionCreate](Positions/PositionCreate.md) | Create an object of a trade position.  
[PositionCreateArray](Positions/PositionCreateArray.md) | Create an object of the array of trade positions.  
[PositionSubscribe](Positions/PositionSubscribe.md) | Subscribe to events and hooks associated with changes in the database of positions.  
[PositionUnsubscribe](Positions/PositionUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the database of positions.  
[PositionDelete](Positions/PositionDelete.md) | Delete a trade position.  
[PositionDeleteByTicket](Positions/PositionDeleteByTicket.md) | Delete a trade position by ticket.  
[PositionUpdate](Positions/PositionUpdate.md) | Update a trade position.  
[PositionGet](Positions/PositionGet.md) | Get a trade position or an array of positions.  
[PositionGetByTicket](Positions/PositionGetByTicket.md) | Get a trade position by the ticket.  
[PositionGetByGroup](Positions/PositionGetByGroup.md) | Get trading positions for a client group.  
[PositionGetByGroupSymbol](Positions/PositionGetByGroupSymbol.md) | Get open positions from the server by group and symbol.  
[PositionGetByLogins](Positions/PositionGetByLogins.md) | Get trading positions by the list of logins.  
[PositionGetByLoginsSymbol](Positions/PositionGetByLoginsSymbol.md) | Get open positions from the server by list of logins and symbol.  
[PositionGetByTickets](Positions/PositionGetByTickets.md) | Get trading positions by the list of tickets.  
[PositionSelectByGroup](Positions/PositionSelectByGroup.md) | Request trading positions from a database for a group of accounts using additional criteria.  
[PositionSelectByLogins](Positions/PositionSelectByLogins.md) | Request trading positions from a database for a list of logins using additional criteria.  
[PositionCheck](Positions/PositionCheck.md) | Check the correctness of a client's positions based on the history of deals.  
[PositionFix](Positions/PositionFix.md) | Correct a client's positions based on the history of his deals.  
[PositionSplit](Positions/PositionSplit.md) | Split trading positions.
