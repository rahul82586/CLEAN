[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Trading](../Trading.md) / Orders

[Previous](../Trading.md) | [Next](Orders/Data-Structure.md)

# Orders

The MetaTrader 5 Web API provides a number of requests for working with clients' orders.

Request | Description  
---|---  
[/api/order/get](Orders/Get-Open-by-Ticket.md) | Get an open order by a ticket.  
[/api/order/get_total](Orders/Get-Open-Total.md) | Get the total number of a client's open orders.  
[/api/order/get_page](Orders/Get-Open-Paged.md) | Get open orders by the login of a client.  
[/api/order/get_batch](Orders/Get-Multiple-Open.md) | Get information about multiple open orders by a list of logins, tickets or groups.  
[/api/order/update](Orders/Update-Open.md) | Change open order on the server.  
[/api/order/delete](Orders/Delete-Open.md) | Deletes one or more open orders by ticket numbers.  
[/api/order/cancel](Orders/Move-to-History.md) | Move one or several open orders to history.  
[/api/history/get](Orders/Get-Closed-by-Ticket.md) | Get an order from a history by its ticket.  
[/api/history/get_total](Orders/Get-Closed-Total.md) | Get the number of orders in the history in the specified time range.  
[/api/history/get_page](Orders/Get-Closed-Paged.md) | Get a client's history of orders in the specified time range.  
[/api/history/get_batch](Orders/Get-Multiple-Closed.md) | Get information about multiple closed orders by a list of logins, tickets or groups.  
[/api/history/update](Orders/Update-Closed.md) | Change closed order on the server.  
[/api/history/delete](Orders/Delete-Closed.md) | Deletes one or more closed orders by ticket numbers.  
[/api/order/backup/list](Orders/Get-Backups-List.md) | Get order backup creation dates within the specified time range.  
[/api/order/backup/get](Orders/Get-from-Backup.md) | Get information about one or more orders from a specific backup on the server.  
[/api/order/backup/restore](Orders/Restore-from-Backup.md) | Recover an order from a backup.  
[/api/order/reopen](Orders/Reopen-Order.md) | Reopen a pending order from the account history.  
  
The format, in which the data about orders are passed, are described in the ["Data Structure"](Orders/Data-Structure.md) section.
