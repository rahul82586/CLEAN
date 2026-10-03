[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / RelatedDocument

[Previous](RelatedClient.md) | [Next](Flags.md)

# IMTComment::RelatedDocument

Get the ID of the document with which the comment is associated.

C++
    
    
    UINT64  IMTComment::RelatedDocument()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTComment.RelatedDocument()

### Return Value

Document ID.

# IMTComment::RelatedDocument

Set the ID of the document with which the comment is associated.

C++
    
    
    MTAPIRES  IMTComment::RelatedDocument(
       const UINT64  record_id  // Identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.RelatedDocument(
       ulong         record_id  // Identifier
       )

### Parameters

**record_id**  
[in] Document ID. The document identifier is equal toIMTDocument::RecordID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

When adding a comment to a client, you only need to specify its ID in the [IMTComment::RelatedClient](RelatedClient.md) field. When adding a comment to a client document, you should specify appropriate IDs in two fields: [IMTComment::RelatedClient](RelatedClient.md) and IMTComment::RelatedDocument.
