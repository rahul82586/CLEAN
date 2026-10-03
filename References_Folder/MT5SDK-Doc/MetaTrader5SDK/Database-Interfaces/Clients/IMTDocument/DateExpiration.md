[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / DateExpiration

[Previous](DateIssue.md) | [Next](DocumentType.md)

# IMTDocument::DateExpiration

Get the document expiry date.

C++
    
    
    INT64  IMTDocument::DateExpiration()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTDocument.DateExpiration()

### Return Value

Document expiry date in seconds since 01.01.1970.

# IMTDocument::DateExpiration

Set the document expiry date.

C++
    
    
    MTAPIRES  IMTDocument::DateExpiration(
       const INT64  date      // Expiry date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.DateExpiration(
       long         date      // Expiry date
       )

### Parameters

**date**  
[in] Document expiry date in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
