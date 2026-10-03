[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Clients

[Previous](Configuration-Databases/Floating-Margin/LeverageGet.md) | [Next](Clients/ClientCreate.md)

# Clients

The MetaTrader 5 Server API allows managing a client database on a trade server. Using the server API, you can add or remove records, edit data and handle database change events. Use the API to expand the standard functionality of client management system in the platform, or to integrate it with external CRM systems.

A detailed description of operations with clients is provided in the [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/en/docs/mt5/platform/administration/clients).

> The client database is maintained separately for each trading server in the cluster. The plugin can only manage those clients that belong to [the server, on which the plugin is running](../Configuration-of-Plugins.md).

The following client operation functions are available:

Functions | Purpose  
---|---  
[ClientCreate](Clients/ClientCreate.md) | Create a client object.  
[ClientCreateArray](Clients/ClientCreateArray.md) | Create an object of the client array.  
[ClientSubscribe](Clients/ClientSubscribe.md) | Subscribe to events and hooks associated with changes in the client base.  
[ClientUnsubscribe](Clients/ClientUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the client base.  
[ClientAdd](Clients/ClientAdd.md) | Add a client to the server database.  
[ClientUpdate](Clients/ClientUpdate.md) | Update a client in the server database.  
[ClientDelete](Clients/ClientDelete.md) | Delete a client from the server database.  
[ClientGet](Clients/ClientGet.md) | Get a client by identifier.  
[ClientGetHistory](Clients/ClientGetHistory.md) | Get the history of client changes.  
[ClientIdsAll](Clients/ClientIdsAll.md) | Get the list of identifiers of all clients in the server database.  
[ClientIdsByGroup](Clients/ClientIdsByGroup.md) | Get the list of identifiers of all clients in the server database filtered by the list of groups.  
[ClientIdsByManager](Clients/ClientIdsByManager.md) | Get the list client identifiers available to the manager.  
[ClientUserAdd](Clients/ClientUserAdd.md) | Bind a trading account to a client.  
[ClientUserDelete](Clients/ClientUserDelete.md) | Unbind a trading account from a client.  
[ClientUserLogins](Clients/ClientUserLogins.md) | Get the list of client's trading accounts.  
[DocumentCreate](Clients/DocumentCreate.md) | Create a document object.  
[DocumentCreateArray](Clients/DocumentCreateArray.md) | Create an object of the array of documents.  
[DocumentSubscribe](Clients/DocumentSubscribe.md) | Subscribe to events and hooks associated with changes in the document database.  
[DocumentUnsubscribe](Clients/DocumentUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the document database.  
[DocumentAdd](Clients/DocumentAdd.md) | Add a document to a client record.  
[DocumentUpdate](Clients/DocumentUpdate.md) | Change a document in the client record.  
[DocumentDelete](Clients/DocumentDelete.md) | Delete a document from a client record.  
[DocumentGet](Clients/DocumentGet.md) | Get a document by identifier.  
[DocumentGetByClient](Clients/DocumentGetByClient.md) | Get client documents by position.  
[DocumentGetHistory](Clients/DocumentGetHistory.md) | Get the history of client document changes.  
[CommentCreate](Clients/CommentCreate.md) | Create a comment object.  
[CommentCreateArray](Clients/CommentCreateArray.md) | Create an object of the array of comments.  
[CommentSubscribe](Clients/CommentSubscribe.md) | Subscribe to events and hooks associated with changes in the comment database.  
[CommentUnsubscribe](Clients/CommentUnsubscribe.md) | Unsubscribe from the events and hooks associated with changes in the comment database.  
[CommentAdd](Clients/CommentAdd.md) | Add a comment to a document or client.  
[CommentUpdate](Clients/CommentUpdate.md) | Change a comment to a document or client.  
[CommentDelete](Clients/CommentDelete.md) | Delete a comment from a document or client.  
[CommentGet](Clients/CommentGet.md) | Get a comment by identifier.  
[CommentGetByClient](Clients/CommentGetByClient.md) | Get comments on a client by position.  
[CommentGetByDocument](Clients/CommentGetByDocument.md) | Get comments on client documents by position.  
[AttachmentCreate](Clients/AttachmentCreate.md) | Create an attachment object.  
[AttachmentAdd](Clients/AttachmentAdd.md) | Create an attachment file for a document or a comment.  
[AttachmentGet](Clients/AttachmentGet.md) | Get an attachment by identifier.
