[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Administrator Interface](../Administrator-Interface.md) / Clients

[Previous](Configuration-Databases/Subscriptions/SubscriptionCfgGetByID.md) | [Next](Clients/ClientCreate.md)

# Clients

The MetaTrader 5 Manager API allows managing a database of clients on a trade server. Using the API, you can add or remove records, edit data and handle database change events. Use the API to expand the standard functionality of client management system in the platform, or to integrate it with external CRM systems.

A detailed description of operations with clients is provided in the [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/en/docs/mt5/platform/administration/clients).

> The Manager API only allows managing the clients, which are available to the manager account used by the application to [connect to the server](Connection-to-the-Server/Connect.md). A client record is available to the manager if one of the following conditions is met:

The following client operation functions are available:

Functions | Purpose  
---|---  
[ClientCreate](Clients/ClientCreate.md) | Create a client object.  
[ClientCreateArray](Clients/ClientCreateArray.md) | Create an object of the client array.  
[ClientAdd](Clients/ClientAdd.md) | Add a client to the server database.  
[ClientAddBatch](Clients/ClientAddBatch.md) | Add a batch of clients to the server database.  
[ClientAddBatchArray](Clients/ClientAddBatchArray.md) | Add a batch of clients to the server database.  
[ClientUpdate](Clients/ClientUpdate.md) | Update a client in the server database.  
[ClientUpdateBatch](Clients/ClientUpdateBatch.md) | Update a batch of clients in the server database.  
[ClientUpdateBatchArray](Clients/ClientUpdateBatchArray.md) | Update a batch of clients in the server database.  
[ClientDelete](Clients/ClientDelete.md) | Delete a client from the server database.  
[ClientDeleteBatch](Clients/ClientDeleteBatch.md) | Delete a batch of clients from the server database.  
[ClientRequest](Clients/ClientRequest.md) | Get a client by identifier.  
[ClientRequestByGroup](Clients/ClientRequestByGroup.md) | Get clients by groups.  
[ClientRequestHistory](Clients/ClientRequestHistory.md) | Get the history of client changes.  
[ClientUserAdd](Clients/ClientUserAdd.md) | Bind a trading account to a client.  
[ClientUserAddBatch](Clients/ClientUserAddBatch.md) | Bind a batch of trading accounts to a client.  
[ClientUserDelete](Clients/ClientUserDelete.md) | Unbind a trading account from a client.  
[ClientUserDeleteBatch](Clients/ClientUserDeleteBatch.md) | Unbind a batch of trading accounts from a client.  
[ClientUserRequest](Clients/ClientUserRequest.md) | Get the list of client's trading accounts.  
[DocumentCreate](Clients/DocumentCreate.md) | Create a document object.  
[DocumentCreateArray](Clients/DocumentCreateArray.md) | Create an object of the array of documents.  
[DocumentAdd](Clients/DocumentAdd.md) | Add a document to a client record.  
[DocumentAddBatch](Clients/DocumentAddBatch.md) | Add a document to a client record.  
[DocumentAddBatchArray](Clients/DocumentAddBatchArray.md) | Add a document to a client record.  
[DocumentUpdate](Clients/DocumentUpdate.md) | Change a document in the client record.  
[DocumentUpdateBatch](Clients/DocumentUpdateBatch.md) | Change a document in the client record.  
[DocumentUpdateBatchArray](Clients/DocumentUpdateBatchArray.md) | Change a document in the client record.  
[DocumentDelete](Clients/DocumentDelete.md) | Delete a document from a client record.  
[DocumentDeleteBatch](Clients/DocumentDeleteBatch.md) | Delete a document from a client record.  
[DocumentRequest](Clients/DocumentRequest.md) | Get a document by identifier.  
[DocumentRequestByClient](Clients/DocumentRequestByClient.md) | Get client documents.  
[DocumentRequestHistory](Clients/DocumentRequestHistory.md) | Get the history of client document changes.  
[CommentCreate](Clients/CommentCreate.md) | Create a comment object.  
[CommentCreateArray](Clients/CommentCreateArray.md) | Create an object of the array of comments.  
[CommentAdd](Clients/CommentAdd.md) | Add a comment to a document or client.  
[CommentAddBatch](Clients/CommentAddBatch.md) | Add a batch of comments to a document or client.  
[CommentAddBatchArray](Clients/CommentAddBatchArray.md) | Add a batch of comments to a document or client.  
[CommentUpdate](Clients/CommentUpdate.md) | Change a comment to a document or client.  
[CommentUpdateBatch](Clients/CommentUpdateBatch.md) | Update a batch of comments to a document or client.  
[CommentUpdateBatchArray](Clients/CommentUpdateBatchArray.md) | Update a batch of comments to a document or client.  
[CommentDelete](Clients/CommentDelete.md) | Delete a comment from a document or client.  
[CommentDeleteBatch](Clients/CommentDeleteBatch.md) | Delete a batch of comments from a document or client.  
[CommentRequest](Clients/CommentRequest.md) | Get a comment by identifier.  
[CommentRequestByClient](Clients/CommentRequestByClient.md) | Get comments on a client by position.  
[CommentRequestByDocument](Clients/CommentRequestByDocument.md) | Get comments on client documents by position.  
[AttachmentCreate](Clients/AttachmentCreate.md) | Create an attachment object.  
[AttachmentCreateArray](Clients/AttachmentCreateArray.md) | Create an object of the array of attachments.  
[AttachmentAdd](Clients/AttachmentAdd.md) | Create an attachment file for a document or a comment.  
[AttachmentAddBatch](Clients/AttachmentAddBatch.md) | Create attachment files for documents or comments in batch.  
[AttachmentAddBatchArray](Clients/AttachmentAddBatchArray.md) | Create attachment files for documents or comments in batch.  
[AttachmentRequest](Clients/AttachmentRequest.md) | Get attachments by identifiers.
