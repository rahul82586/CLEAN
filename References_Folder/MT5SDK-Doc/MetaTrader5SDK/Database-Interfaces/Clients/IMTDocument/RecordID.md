[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / RecordID

[Previous](Clear.md) | [Next](RelatedClient.md)

# IMTDocument

Get the document identifier.

C++
    
    
    UINT64  IMTDocument::RecordID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDocument.RecordID()

### Return Value

Document ID.

# IMTDocument::RecordID

Set the document identifier.

C++
    
    
    MTAPIRES  IMTDocument::RecordID(
       const UINT64  record_id  // Identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.RecordID(
       ulong         record_id  // Identifier
       )

### Parameters

**record_id**  
[in] Document ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
