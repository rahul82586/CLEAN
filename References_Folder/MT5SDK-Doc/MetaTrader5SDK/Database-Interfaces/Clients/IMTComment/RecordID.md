[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / RecordID

[Previous](Clear.md) | [Next](RelatedClient.md)

# IMTComment::RecordID

Get the comment identifier.

C++
    
    
    UINT64  IMTComment::RecordID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTComment.RecordID()

### Return Value

Comment ID.

# IMTComment::RecordID

Set the comment identifier.

C++
    
    
    MTAPIRES  IMTComment::RecordID(
       const UINT64  record_id  // Identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.RecordID(
       ulong         record_id  // Identifier
       )

### Parameters

**record_id**  
[in] Comment identifier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
