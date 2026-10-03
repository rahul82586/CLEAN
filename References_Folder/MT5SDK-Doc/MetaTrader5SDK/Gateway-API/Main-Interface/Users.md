[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Main Interface](../Main-Interface.md) / Users

[Previous](Tick-Data/TickHistoryReplace.md) | [Next](Users/UserCreate.md)

# Users

Functions of Gateway API allow accessing the user database on the trade server as well as subscribing and unsubscribing from events connected with changes in this database.

Functions | Purpose  
---|---  
[UserCreate](Users/UserCreate.md) | Create an object of a client record.  
[UserCreateAccount](Users/UserCreate.md) | Create an object of a client's trading account.  
[UserSubscribe](Users/UserSubscribe.md) | Subscribe to events associated with changes in the client base.  
[UserUnsubscribe](Users/UserUnsubscribe.md) | Unsubscribe from events associated with changes in the client base.  
[UserTotal](Users/UserTotal.md) | Get the total number of users in groups available to the gateway.  
[UserGet](Users/UserGet.md) | Get a client record by the login.  
[UserGetByAccount](Users/UserGetByAccount.md) | Get a client record, which corresponds to the account number in the external trading system.  
[UserGroup](Users/UserGroup.md) | Get the group of a client by the login.  
[UserLogins](Users/UserLogins.md) | Returns an array of logins of the clients who are included in the specified group.
