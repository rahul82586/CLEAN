[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Trading](../Trading.md) / Deals

[Previous](Orders/Reopen-Order.md) | [Next](Deals/Data-Structure.md)

# Deals

The Web API provides the following requests for receiving information about clients' deals:

Request | Description  
---|---  
[/api/deal/get](Deals/Get-by-Ticket.md) | Get a deal by a ticket.  
[/api/deal/get_total](Deals/Get-Total.md) | Get the total number of deals.  
[/api/deal/get_page](Deals/Get-Paged.md) | Get deals by the login of a client.  
[/api/deal/get_batch](Deals/Get-Multiple.md) | Get information about multiple deals by a list of logins, tickets or groups.  
[/api/deal/update](Deals/Update.md) | Change deal on the server.  
[/api/deal/delete](Deals/Delete.md) | Deletes one or more deals by ticket numbers.  
[/api/deal/backup/list](Deals/Get-Backups-List.md) | Get deal backup creation dates within the specified time range.  
[/api/deal/backup/get](Deals/Get-from-Backup.md) | Get information about one or more deals from a specific backup on the server.  
[/api/deal/backup/restore](Deals/Restore-from-Backup.md) | Recover a deal from backup.  
  
The format, in which the data about deals are passed, are described under the [Data Structure](Deals/Data-Structure.md) section.
