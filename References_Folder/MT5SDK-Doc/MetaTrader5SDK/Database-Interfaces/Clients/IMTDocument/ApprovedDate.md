[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / ApprovedDate

[Previous](RelatedClient.md) | [Next](ApprovedBy.md)

# IMTDocument::ApprovedDate

Get the document approval date.

C++
    
    
    INT64  IMTDocument::ApprovedDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTDocument.ApprovedDate()

### Return Value

Document approval date in seconds since 01.01.1970.

# IMTDocument::ApprovedDate

Set the document approval date.

C++
    
    
    MTAPIRES  IMTDocument::ApprovedDate(
       const INT64  date      // Date of approval
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.ApprovedDate(
       long         date      // Date of approval
       )

### Parameters

**time**  
[in] Document approval date in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
