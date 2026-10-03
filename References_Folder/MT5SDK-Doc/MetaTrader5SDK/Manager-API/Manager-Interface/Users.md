[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Manager Interface](../Manager-Interface.md) / Users

[Previous](Clients/AttachmentRequest.md) | [Next](Users/Enumerations.md)

# User Functions

Functions allow managing the server database of users and their access to the trading platform, as well subscribe and unsubscribe from events associated with changes in the user base.

The following functions for managing users are available:

Functions | Purpose  
---|---  
[UserCreate](Users/UserCreate.md) | Create an object of a client record.  
[UserCreateArray](Users/UserCreateArray.md) | Create an object of an array of client records.  
[UserCreateAccount](Users/UserCreateAccount.md) | Create an object of a client's trading account.  
[UserCreateAccountArray](Users/UserCreateAccountArray.md) | Create an object of an array trading accounts.  
[UserSubscribe](Users/UserSubscribe.md) | Subscribe to events associated with changes in the client base.  
[UserUnsubscribe](Users/UserUnsubscribe.md) | Unsubscribe from events associated with changes in the client base.  
[UserAdd](Users/UserAdd.md) | Add a client record.  
[UserDelete](Users/UserDelete.md) | Delete a client record.  
[UserDeleteBatch](Users/UserDeleteBatch.md) | Delete multiple accounts.  
[UserUpdate](Users/UserUpdate.md) | Update a client record.  
[UserUpdateBatch](Users/UserUpdateBatch.md) | Update multiple accounts.  
[UserUpdateBatchArray](Users/UserUpdateBatchArray.md) | Update multiple accounts.  
[UserTotal](Users/UserTotal.md) | Get the total number of users on a trade server.  
[UserGet](Users/UserGet.md) | Get a client record by the login.  
[UserGetByGroup](Users/UserGetByGroup.md) | Get accounts by one or more groups.  
[UserGetByLogins](Users/UserGetByLogins.md) | Get accounts by the list of logins.  
[UserRequest](Users/UserRequest.md) | Request a client record by the login from a server.  
[UserRequestArray](Users/UserRequestArray.md) | Request an array of client records by the group name.  
[UserRequestByLogins](Users/UserRequestByLogins.md) | Request accounts from the server by a list of logins.  
[UserGroup](Users/UserGroup.md) | Get the group of a client by the login.  
[UserLogins](Users/UserLogins.md) | Returns an array of logins of the clients who are included in the specified group.  
[UserPasswordCheck](Users/UserPasswordCheck.md) | Check the user's password.  
[UserPasswordChange](Users/UserPasswordChange.md) | Change the user's password.  
[UserCertCreate](Users/UserCertCreate.md) | Create an object of a certificate.  
[UserCertUpdate](Users/UserCertUpdate.md) | Add or update a client certificate.  
[UserCertGet](Users/UserCertGet.md) | Get the certificate of a client by the login.  
[UserCertDelete](Users/UserCertDelete.md) | Reset the user certificate.  
[UserCertConfirm](Users/UserCertConfirm.md) | Confirm the user certificate.  
[UserAccountSubscribe](Users/UserAccountSubscribe.md) | Subscribe to receive events related to changes in the account trading state.  
[UserAccountUnsubscribe](Users/UserAccountUnsubscribe.md) | Unsubscribe from the events related to changes in the account trading state.  
[UserAccountGet](Users/UserAccountGet.md) | Get client trading account by a login.  
[UserAccountGetByGroup](Users/UserAccountGetByGroup.md) | Get trading accounts for one or several groups.  
[UserAccountGetByLogins](Users/UserAccountGetByLogins.md) | Get trading accounts for a list of logins.  
[UserAccountRequest](Users/UserAccountRequest.md) | Request a client's account trade order from a server by the ticket.  
[UserAccountRequestByLogins](Users/UserAccountRequestByLogins.md) | Request accounts' trading statuses from the server by a list of logins.  
[UserAccountRequestArray](Users/UserAccountRequestArray.md) | Request an array of trade accounts from a server by the group name.  
[UserExternalGet](Users/UserExternalGet.md) | Get a client record by the [gateway identifier](../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md) and/or the [account number in an external trading system](../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md).  
[UserExternalRequest](Users/UserExternalRequest.md) | Request a client record from a server by the [gateway identifier](../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md) and/or the [account number in an external trading system](../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md).  
[UserExternalSync](Users/UserExternalSync.md) | Synchronizing client's trading status with an external trading system.  
[UserBalanceCheck](Users/UserBalanceCheck.md) | Check and adjust a client's balance and credit assets.  
[UserBalanceCheckBatch](Users/UserBalanceCheckBatch.md) | Check and adjust balance and credit funds for multiple clients.  
[NotificationsSend](Users/NotificationsSend.md) | Sends push notifications to mobile devices.  
[EmailSend](Users/EmailSend.md) | Send an email to a selected address.  
[MessengerVerifyPhone](Users/MessengerVerifyPhone.md) | Verify the validity of a passed phone number based on local phone number formation rules.  
[MessengerSend](Users/MessengerSend.md) | Send an SMS message.
