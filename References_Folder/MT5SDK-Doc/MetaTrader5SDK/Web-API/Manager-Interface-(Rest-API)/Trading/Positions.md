[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Trading](../Trading.md) / Positions

[Previous](Deals/Restore-from-Backup.md) | [Next](Positions/Data-Structure.md)

# Positions

The Web API provides the following requests for receiving information about clients' positions:

Request | Description  
---|---  
[/api/position/get](Positions/Get-by-Symbol.md) | Get a client's position by the symbol name.  
[/api/position/get_total](Positions/Get-Total.md) | Get the total number of a client's open positions.  
[/api/position/get_page](Positions/Get-Paged.md) | Get positions by the login of a client.  
[/api/position/get_batch](Positions/Get-Multiple.md) | Get information about multiple positions by a list of logins, tickets or groups.  
[/api/position/update](Positions/Update.md) | Change position on the server.  
[/api/position/delete](Positions/Delete.md) | Deletes one or more positions by ticket numbers.  
[/api/position/backup/list](Positions/Get-Backups-List.md) | Get position backup creation dates within the specified time range.  
[/api/position/backup/get](Positions/Get-from-Backup.md) | Get position backup creation dates within the specified time range.  
[/api/position/backup/restore](Positions/Restore-from-Backup.md) | Recover a position from a backup.  
[/api/position/check](Positions/Check.md) | Checks the correctness of an account's positions based on the history of deals.  
[/api/position/fix](Positions/Fix-Position.md) | Corrects an account's positions based on the history of deals.  
  
The format, in which the data about positions are passed, are described in the ["Data Structure"](Positions/Data-Structure.md) section.
