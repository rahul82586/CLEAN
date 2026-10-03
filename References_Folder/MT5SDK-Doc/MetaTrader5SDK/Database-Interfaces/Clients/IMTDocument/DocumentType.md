[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / DocumentType

[Previous](DateExpiration.md) | [Next](DocumentSubtype.md)

# IMTDocument::DocumentType

Get the document type.

C++
    
    
    UINT  IMTDocument::DocumentType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDocument.DocumentType()

### Return Value

A value of the [IMTDocument::EnDocumentTypes (#endocumenttypes)](Enumerations.md#endocumenttypes) enumeration.

# IMTDocument::DocumentType

Set the document type.

C++
    
    
    MTAPIRES  IMTDocument::DocumentType(
       const UINT  type        // Document type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.DocumentType(
       uint        type        // Document type
       )

### Parameters

**type**  
[in] Document type. The document type is passed using theIMTDocument::EnDocumentTypesenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
