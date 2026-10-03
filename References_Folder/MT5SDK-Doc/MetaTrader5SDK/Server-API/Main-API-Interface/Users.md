[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Users

[Previous](Clients/AttachmentGet.md) | [Next](Users/UserCreate.md)

# Users

The MetaTrader 5 Server API allows managing an account base on a trade server. Using the server API, you can add or remove users, edit their data and handle events of changes in the account base.

An important feature of an account base is that users are bound to a certain trade server. Accordingly, the plugin can manage only those users who belong to the server where it is running.

Functions described in this section allow managing the server database of users and their access to the trading platform, as well subscribe and unsubscribe from events associated with changes in the user base.

Functions | Purpose  
---|---  
[UserCreate](Users/UserCreate.md) | Create an object of a client record.  
[UserCreateAccount](Users/UserCreate.md) | Create an object of a client's trading account.  
[UserSubscribe](Users/UserSubscribe.md) | Subscribe to events and hooks associated with changes in the client base.  
[UserUnsubscribe](Users/UserUnsubscribe.md) | Undubscribe from events and hooks associated with changes in the client base.  
[UserAdd](Users/UserAdd.md) | Add a client record.  
[UserDelete](Users/UserDelete.md) | Delete a client record.  
[UserUpdate](Users/UserUpdate.md) | Update a client record.  
[UserTotal](Users/UserTotal.md) | Get the total number of users on a trade server.  
[UserGet](Users/UserGet.md) | Get a client record by the login.  
[UserGroup](Users/UserGroup.md) | Get the group of a client by the login.  
[UserLogins](Users/UserLogins.md) | Returns an array of logins of the clients who are included in the specified group.  
[UserPasswordCheck](Users/UserPasswordCheck.md) | Check the user's password.  
[UserPasswordChange](Users/UserPasswordChange.md) | Change the user's password.  
[UserDepositChange](Users/UserDepositChange.md) | Conduct a balance operation on a user account.  
[UserDepositChangeRaw](Users/UserDepositChangeRaw.md) | Conduct balance operation on a user account without checking the free margin and the current balance on the account.  
[UserArchive](Users/UserArchive.md) | Move a client record to an archive database.  
[UserArchiveGet](Users/UserArchiveGet.md) | Request a client record from an archive database.  
[UserArchiveLogins](Users/UserArchiveLogins.md) | Returns an array of logins in an archive database for the specified group.  
[UserRestore](Users/UserRestore.md) | Restore a client record from an archive or a backup database.  
[NotificationsSend](Users/NotificationsSend.md) | Sends push notifications to mobile devices.  
[UserAccountGet](Users/UserAccountGet.md) | Obtaining a client's trading account by a login.
