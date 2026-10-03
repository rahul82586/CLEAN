[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / RelatedClient

[Previous](RecordID.md) | [Next](ApprovedDate.md)

# IMTDocument::RelatedClient

Get the identifier of the client with which the document is associated.

C++
    
    
    UINT64  IMTDocument::RelatedClient()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDocument.RelatedClient()

### Return Value

Client ID.

# IMTDocument::RelatedClient

Set the identifier of the client with which the document is associated.

C++
    
    
    MTAPIRES  IMTDocument::RelatedClient(
       const UINT64  record_id  // Identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.RelatedClient(
       ulong         record_id  // Identifier
       )

### Parameters

**record_id**  
[in] Client ID. The client ID is equal to theIMTClient::RecordIDvalue.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
