[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Clients](../Clients.md) / IMTDocument

[Previous](IMTCommentSink/OnCommentDelete.md) | [Next](IMTDocument/Enumerations.md)

# IMTDocument

The IMTDocument class is designed for working with [client](IMTClient.md) documents. The interface contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDocument/Release.md) | Delete the current object.  
[Assign](IMTDocument/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDocument/Clear.md) | Clear an object.  
[RecordID](IMTDocument/RecordID.md) | Get and set the document identifier.  
[RelatedClient](IMTDocument/RelatedClient.md) | Get and set the client ID with which the document is associated.  
[ApprovedDate](IMTDocument/ApprovedDate.md) | Get and set the document approval date.  
[ApprovedBy](IMTDocument/ApprovedBy.md) | Get and set the manager who approved/checked the document.  
[DateIssue](IMTDocument/DateIssue.md) | Get and set the document issue date.  
[DateExpiration](IMTDocument/DateExpiration.md) | Get and set the document expiry date.  
[DocumentType](IMTDocument/DocumentType.md) | Get and set the document type.  
[DocumentSubtype](IMTDocument/DocumentSubtype.md) | Get and set the document subtype.  
[DocumentName](IMTDocument/DocumentName.md) | Get and set the document name.  
[DocumentComment](IMTDocument/DocumentComment.md) | Get and set a comment to a document.  
[DocumentStatus](IMTDocument/DocumentStatus.md) | Get and set the document status.  
[AttachmentsAdd](IMTDocument/AttachmentsAdd.md) | Add a file to a document.  
[AttachmentsClear](IMTDocument/AttachmentsClear.md) | Clear the list of document files.  
[AttachmentsTotal](IMTDocument/AttachmentsTotal.md) | Get and set the number of files in a document.  
[AttachmentsNext](IMTDocument/AttachmentsNext.md) | Get and set the file ID from a document, by index.  
  
The IMTDocument class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnDocumentTypes (#endocumenttypes)](IMTDocument/Enumerations.md#endocumenttypes) | Document types.  
[EnDocumentSubtype (#endocumenttypes)](IMTDocument/Enumerations.md#endocumenttypes) | Document subtypes.  
[EnDocumentStatus (#endocumentstatus)](IMTDocument/Enumerations.md#endocumentstatus) | Document statuses.
