[🏠 Document Start](../../README.md) / [Web API](../README.md) / [Manager Interface (Rest API)](../Manager-Interface-(Rest-API).md) / Users

[Previous](Trading/Trade-Requests/Get-Request-Result.md) | [Next](Users/Data-Structure.md)

# Users

The Web API provides the following requests for working with users on the server:

Request | Description  
---|---  
[/api/user/add](Users/Add.md) | Add a user.  
[/api/user/update](Users/Update.md) | Update a user.  
[/api/user/delete](Users/Delete.md) | Delete a user.  
[/api/user/get](Users/Get-by-Login.md) | Get user information by login.  
[/api/user/get_external](Users/Get-by-External-Account.md) | Get user information by his or her external trading system (exchange) account.  
[/api/user/get_batch](Users/Get-Multiple.md) | Get information about multiple users by a list of logins or groups.  
[/api/user/check_password](Users/Check-Password.md) | Check user password.  
[/api/user/change_password](Users/Change-Password.md) | Change the user password.  
[/api/user/account/get](Users/Get-Trade-State.md) | Get information about user trading status.  
[/api/user/account/get_batch](Users/Get-Multiple-Trade-States.md) | Get information about multiple trading accounts by a list of logins or groups.  
[/api/user/logins](Users/Get-List.md) | Get a list of accounts in the specified groups.  
[/api/user/total](Users/Get-Total.md) | Get the total number of users on the trading server, available to your manager account.  
[/api/user/group](Users/Get-Group.md) | Get user group by login.  
[/api/user/certificate/update](Users/Update-Certificate.md) | Add or update user certificates.  
[/api/user/certificate/get](Users/Get-Certificate.md) | Get a user certificate.  
[/api/user/certificate/delete](Users/Delete-Certificate.md) | Delete a user certificate.  
[/api/user/certificate/confirm](Users/Confirm-Certificate.md) | Confirm the user certificate.  
[/api/user/otp_secret/get](Users/Get-OTP-Key.md) | Get a secret OTP key.  
[/api/user/otp_secret/set](Users/Set-OTP-Key.md) | Set a secret OTP key.  
[/api/user/sync_external](Users/Sync-with-External-System.md) | Synchronize trading account status with an external trading system.  
[/api/user/check_balance](Users/Check-Balance.md) | Check and correct user balance and credit funds.  
[/api/user/archive/add](Users/Move-to-Archvie.md) | Move a user to an archive database.  
[/api/user/archive/get](Users/Get-from-Archive.md) | Get user information from an archive database.  
[/api/user/archive/get_batch](Users/Get-Multiple-from-Archive.md) | Gets bulk user information from an archive database.  
[/api/user/restore](Users/Restore-from-Archive.md) | Restore users from archive or backup databases.  
[/api/user/backup/list](Users/Get-Backups-List.md) | Get user backup creation dates within the specified time range.  
[/api/user/backup/get](Users/Get-User-from-Backup.md) | Get user information from a specific backup on the server.  
[/api/notification/send](Users/Send-Push-Notifications.md) | Send push-notifications to a list of MetaQuotes IDs.  
  
The format, in which the data about a client are passed, are described in the ["Data Structure"](Users/Data-Structure.md).
