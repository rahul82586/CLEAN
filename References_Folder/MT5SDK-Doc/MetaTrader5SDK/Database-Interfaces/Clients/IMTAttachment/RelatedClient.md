[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachment](../IMTAttachment.md) / RelatedClient

[Previous](RecordID.md) | [Next](FileType.md)

# IMTAttachment::RelatedClient

Get the client ID with which the attachment is associated.

C++
    
    
    UINT64  IMTAttachment::RelatedClient()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTAttachment.RelatedClient()

### Return Value

Client ID.

# IMTAttachment::RelatedClient

Set the client ID with which the attachment is associated.

C++
    
    
    MTAPIRES  IMTAttachment::RelatedClient(
       const UINT64  record_id  // Identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachment.RelatedClient(
       ulong         record_id  // Identifier
       )

### Parameters

**record_id**  
[in] Client ID. The client ID is equal to theIMTClient::RecordIDvalue.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
