[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Users](../Users.md) / IMTUserSink

[Previous](IMTUserArray/SearchRight.md) | [Next](IMTUserSink/OnUserAdd.md)

# IMTUserSink

The IMTUserSink contains the following methods:

Method | Purpose  
---|---  
[OnUserAdd](IMTUserSink/OnUserAdd.md) | A handler of the event of adding a new account.  
[OnUserAddExt](IMTUserSink/OnUserAddExt.md) | An extended handler of a new account addition event. It additionally passes the passwords of the created account. This method can only be used in the MetaTrader 5 Server API.  
[OnUserUpdate](IMTUserSink/OnUserUpdate.md) | A handler of an event of account update.  
[OnUserDelete](IMTUserSink/OnUserDelete.md) | A handler of an event of account deletion.  
[OnUserClean](IMTUserSink/OnUserClean.md) | A handler of the event of deletion of obsolete demo account on a trade server.  
[OnUserLogin](IMTUserSink/OnUserLogin.md) | A handler of the event of an account's connection to the server.  
[OnUserLoginExt](IMTUserSink/OnUserLoginExt.md) | A handle of the event of client connection to the server. Passes an extended description of the connection.  
[OnUserLogout](IMTUserSink/OnUserLogout.md) | A handler of the event of a client's disconnection from the server.  
[OnUserLogoutExt](IMTUserSink/OnUserLogoutExt.md) | An extended handler of the event of an account's connection to the server. Passes an extended description of the connection.  
[OnUserChangePassword](IMTUserSink/OnUserChangePassword.md) | Account password change event handler. This method can only be used in the MetaTrader 5 Server API.  
[OnUserSync](IMTUserSink/OnUserSync.md) | A handler of the event of the account base synchronization.  
[OnUserArchive](IMTUserSink/OnUserArchive.md) | A handler of the event of moving an account to the archive database. This method is used only in the MetaTrader 5 Server API.  
[OnUserRestore](IMTUserSink/OnUserRestore.md) | A handler of the event of account restoring from an archive or backup database. This method is used only in the MetaTrader 5 Server API.  
[HookUserAdd](IMTUserSink/HookUserAdd.md) | A hook of an event of adding a new account. This method is used only in the MetaTrader 5 Server API.  
[HookUserAddExt](IMTUserSink/HookUserAddExt.md) | An extended hook for the new account addition event. It additionally passes the passwords of the created account. This method can only be used in the MetaTrader 5 Server API.  
[HookUserUpdate](IMTUserSink/HookUserUpdate.md) | A hook of an event of account record update. This method is used only in the MetaTrader 5 Server API.  
[HookUserDelete](IMTUserSink/HookUserDelete.md) | A hook of an event of account record deletion. This method is used only in the MetaTrader 5 Server API.  
[HookUserLogin](IMTUserSink/HookUserLogin.md) | A hook of an account's connection to the server. This method is used only in the MetaTrader 5 Server API.  
[HookUserLoginExt](IMTUserSink/HookUserLoginExt.md) | A hook of a account's connection to the server. Passes an extended description of the connection. This method can only be used in the MetaTrader 5 Server API.  
[HookUserChangePassword](IMTUserSink/HookUserChangePassword.md) | Account password change event hook. This method can only be used in the MetaTrader 5 Server API.  
[HookUserArchive](IMTUserSink/HookUserArchive.md) | A hook of the event of moving an account to the archive database. The method is only used in MetaTrader 5 Server API.
