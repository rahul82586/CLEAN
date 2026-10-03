[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Administrator Interface](../Administrator-Interface.md) / Users

[Previous](Clients/AttachmentRequest.md) | [Next](Users/Enumerations.md)

# User Functions

Using these functions, you can manage the user database on the server and user access to the trading platform. The following functions for managing users are available:

Functions | Purpose  
---|---  
[UserCreate](Users/UserCreate.md) | Create an object of a client record.  
[UserCreateArray](Users/UserCreateArray.md) | Create an object of an array of client records.  
[UserAdd](Users/UserAdd.md) | Add a user.  
[UserDelete](Users/UserDelete.md) | Delete a user.  
[UserDeleteBatch](Users/UserDeleteBatch.md) | Delete multiple accounts.  
[UserUpdate](Users/UserUpdate.md) | Update a user.  
[UserUpdateBatch](Users/UserUpdateBatch.md) | Update multiple accounts.  
[UserUpdateBatchArray](Users/UserUpdateBatchArray.md) | Update multiple accounts.  
[UserRequest](Users/UserRequest.md) | Request a client record by the login from a server.  
[UserRequestArray](Users/UserRequestArray.md) | Request an array of client records by the group name.  
[UserRequestByLogins](Users/UserRequestByLogins.md) | Request accounts from the server by a list of logins.  
[UserPasswordCheck](Users/UserPasswordCheck.md) | Check the user's password.  
[UserPasswordChange](Users/UserPasswordChange.md) | Change the user's password.  
[UserCertCreate](Users/UserCertCreate.md) | Create an object of a certificate.  
[UserCertUpdate](Users/UserCertUpdate.md) | Add or update a client certificate.  
[UserCertGet](Users/UserCertGet.md) | Get the certificate of a client by the login.  
[UserCertDelete](Users/UserCertDelete.md) | Reset the user certificate.  
[UserCertConfirm](Users/UserCertConfirm.md) | Confirm the user certificate.  
[UserArchive](Users/UserArchive.md) | Move a user to an archive database.  
[UserArchiveBatch](Users/UserArchiveBatch.md) | Move multiple accounts to an archive database.  
[UserArchiveRequest](Users/UserArchiveRequest.md) | Request a client record from an archive database.  
[UserArchiveRequestArray](Users/UserArchiveRequestArray.md) | Request accounts from an archive databased, filtered by groups.  
[UserArchiveRequestByLogins](Users/UserArchiveRequestByLogins.md) | Request accounts from an archive databased, filtered by logins.  
[UserBackupRequest](Users/UserBackupRequest.md) | Request a client record from a backup database.  
[UserBackupRequestArray](Users/UserBackupRequestArray.md) | Request accounts from the specified server's backup, filtered by groups.  
[UserBackupRequestByLogins](Users/UserBackupRequestByLogins.md) | Request accounts from the specified server's backup, filtered by a list of logins.  
[UserBackupList](Users/UserBackupList.md) | Request the dates of backup databases of users for the specified time range.  
[UserRestore](Users/UserRestore.md) | Restore a user from an archive or backup database.  
[UserRestoreBatch](Users/UserRestoreBatch.md) | Restore multiple accounts from an archive or backup database.  
[UserRestoreBatchArray](Users/UserRestoreBatchArray.md) | Restore multiple accounts from an archive or backup database.  
[UserBalanceCheck](Users/UserBalanceCheck.md) | Check and adjust a client's balance and credit assets.  
[UserBalanceCheckBatch](Users/UserBalanceCheckBatch.md) | Check and adjust balance and credit funds for multiple clients.  
[UserExternalRequest](Users/UserExternalRequest.md) | Request a client record from a server by the [gateway identifier](../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md) and/or the [account number in an external trading system](../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md).  
[UserExternalSync](Users/UserExternalSync.md) | Synchronizing client's trading status with an external trading system.  
[UserLogins](Users/UserLogins.md) | Returns an array of logins of the clients who are included in the specified group.  
[NotificationsSend](Users/NotificationsSend.md) | Sends push notifications to mobile devices.
