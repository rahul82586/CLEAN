[🏠 Document Start](../../README.md) / [Web API](../README.md) / [Manager Interface (Rest API)](../Manager-Interface-(Rest-API).md) / Clients

[Previous](Users/Send-Push-Notifications.md) | [Next](Clients/Data-Structure.md)

# Clients

The following commands are available for working with clients (trading accounts) on the server:

Request | Description  
---|---  
[/api/client/add](Clients/Add.md) | Create a client on the server.  
[/api/client/update](Clients/Update.md) | Update client data on the server.  
[/api/client/delete](Clients/Delete.md) | Delete a client from the server.  
[/api/client/get](Clients/Get.md) | Get client information by the client ID.  
[/api/client/history/get](Clients/Get-Change-History.md) | Get the history of client record changes in the specified period of time.  
[/api/client/get_ids](Clients/Get-Identifiers.md) | Get the list of identifiers of all clients available to the manager.  
[/api/client/user/add](Clients/Bind-Account.md) | Bind a trading account to a client.  
[/api/client/user/delete](Clients/Unbind-Account.md) | Unbind a trading account from a client.  
[/api/client/user/get_logins](Clients/Get-Accounts.md) | Get the list of clients bound to a client record.  
[/api/document/add](Clients/Add-Document.md) | Add a document to a client record.  
[/api/document/update](Clients/Update-Document.md) | Change a document bound to a client record.  
[/api/document/delete](Clients/Delete-Document.md) | Delete a document from a client record.  
[/api/document/get](Clients/Get-Document.md) | Get a document from a client record.  
[/api/document/history/get](Clients/Get-Document-History.md) | Get the history of changes in the document bound to a client record.  
[/api/comment/add](Clients/Add-Comment.md) | Add a comment to a client record or to a document.  
[/api/comment/update](Clients/Update-Comment.md) | Edit a comment to a client record or to a document.  
[/api/comment/delete](Clients/Delete-Comment.md) | Delete a comment from a client record or from a document.  
[/api/comment/get](Clients/Get-Comment.md) | Get a comment added to a document or a client record.  
[/api/attachment/add](Clients/Add-Attachment.md) | Add an attachment file to a file database.  
[/api/attachment/get](Clients/Get-Attachment.md) | Get an attachment from the database by its identifier.  
[/api/attachment/attach](Clients/BindUnbind-Attachment.md) | Attach or detach a file from a comment or document.  
  
The client data format is described in the "[Data Structure](Clients/Data-Structure.md)" section.
