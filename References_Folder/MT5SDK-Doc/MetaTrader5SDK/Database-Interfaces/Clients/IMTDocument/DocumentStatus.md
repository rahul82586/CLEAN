[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / DocumentStatus

[Previous](DocumentComment.md) | [Next](AttachmentsAdd.md)

# IMTDocument::DocumentStatus

Get the document status.

C++
    
    
    UINT  IMTDocument::DocumentStatus()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDocument.DocumentStatus()

### Return Value

A value of the [IMTDocument::EnDocumentStatus (#endocumentstatus)](Enumerations.md#endocumentstatus) enumeration.

# IMTDocument::DocumentStatus

Set the document status.

C++
    
    
    MTAPIRES  IMTDocument::DocumentStatus(
       const UINT  status      // Document status
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.DocumentStatus(
       uint        status      // Document status
       )

### Parameters

**status**  
[in] Document status. The status can be passed using theIMTDocument::EnDocumentStatusenumerations.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
