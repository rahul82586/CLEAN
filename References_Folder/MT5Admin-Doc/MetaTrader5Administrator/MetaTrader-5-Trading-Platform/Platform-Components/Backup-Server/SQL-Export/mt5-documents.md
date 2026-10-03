[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_documents

[Previous](mt5-clients.md) | [Next](mt5-users.md)

# mt5_documents

Data about [client documents (#documents)](../../../Platform-Setup/Clients.md#documents) is exported to this table. The table contains the following fields:

Name | Type | Description  
DocumentID | Integer | Initial key. Unique document ID.  
Timestamp | Integer | A unique values within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has changed.  
RelatedClient | Integer | The ID of the client to whom the document belongs. Corresponds to Client ID from the [mt5_clients](mt5-clients.md) table.  
ApprovedDate | DateTime | Document approval date, in the format of YYYY-MM-DD HH:MM:SS  
ApprovedBy | Integer | The login of the manager by whom the document was approved.  
DateIssue | DateTime | Document issue date, in the format of YYYY-MM-DD HH:MM:SS  
DateExpiration | DateTime | Document expiration date, in the format of YYYY-MM-DD HH:MM:SS  
DocumentType | Integer | Document type:

  * 0 — Other
  * 1 — Proof of identity
  * 2 — Proof of address
  * 3 — Registration address
  * 4 — CEO's ID document
  * 5 — Certificate of Registration
  * 6 — Certificate of Directors
  * 7 — Certificate of good standing

  
DocumentName | String | Document name.  
DocumentComment | String | Comment to the document.  
DocumentStatus | Integer | Document status:

  * 0 — New
  * 1 — Approved
  * 2 — Rejected
  * 3 — Archived
  * 4 — Deleted

  
  
> Only document data is exported to SQL. Document files themselves are not exported.
