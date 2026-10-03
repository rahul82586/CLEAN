[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / DateIssue

[Previous](ApprovedBy.md) | [Next](DateExpiration.md)

# IMTDocument::DateIssue

Get the document issue date.

C++
    
    
    INT64  IMTDocument::DateIssue()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTDocument.DateIssue()

### Return Value

Document issue date in seconds since 01.01.1970.

# IMTDocument::DateIssue

Set the document issue date.

C++
    
    
    MTAPIRES  IMTDocument::DateIssue(
       const INT64  date      // Date of issue
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.DateIssue(
       long         date      // Date of issue
       )

### Parameters

**date**  
[in] Document issue date in seconds since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
