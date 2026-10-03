[🏠 Document Start](../README.md) / [Database Interfaces](README.md) / Clients

[Previous](Trade/Daily-Reports/IMTDailySink/OnDailySync.md) | [Next](Clients/IMTClient.md)

# Clients

The MetaTrader 5 Server API allows managing a client database on a trade server. Using the server API, you can add or remove records, edit data and handle database change events. Use the API to expand the standard functionality of client management system in the platform, or to integrate it with external CRM systems.

A detailed description of operations with clients is provided in the [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/en/docs/mt5/platform/administration/clients).

> The client database is maintained separately for each trading server in the cluster. This includes the client database and separate auxiliary databases of comments, documents and attachments. The plugin can only manage those clients that belong to [the server, on which the plugin is running](../Server-API/Configuration-of-Plugins.md).

Operations with the clients are implemented via several interfaces which provide access to all client data and to additional database access possibilities:

  * [IMTClient](Clients/IMTClient.md) — full description of a client.
  * [IMTClientArray](Clients/IMTClientArray.md) — methods for efficient operations with client arrays.
  * [IMTClientSink](Clients/IMTClientSink.md) — handlers of client database change events. 
  * [IMTComment](Clients/IMTComment.md) — description of comments which can be added to clients and their documents.
  * [IMTCommentArray](Clients/IMTCommentArray.md) — methods for efficient operations with comment arrays.
  * [IMTCommentSink](Clients/IMTCommentSink.md) — handlers of comment database change events. 
  * [IMTDocument](Clients/IMTDocument.md) — description of client documents.
  * [IMTDocumentArray](Clients/IMTDocumentArray.md) — methods for efficient operations with document arrays.
  * [IMTDocumentSink](Clients/IMTDocumentSink.md) — handlers of document database changes events. 
  * [IMTAttachment](Clients/IMTAttachment.md) — description of attachments used in documents and client comments.
  * [IMTAttachmentArray](Clients/IMTAttachmentArray.md) — methods for efficient operations with attachment arrays.


