[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / DocumentSubtype

[Previous](DocumentType.md) | [Next](DocumentName.md)

# IMTDocument::DocumentSubtype

Get the document subtype.

C++
    
    
    UINT  IMTDocument::DocumentSubtype()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDocument.DocumentSubtype()

### Return Value

A value of the [IMTDocument::EnDocumentSubtype (#endocumentsubtype)](Enumerations.md#endocumentsubtype) enum.

# IMTDocument::DocumentSubtype

Set the document type.

C++
    
    
    MTAPIRES  IMTDocument::DocumentSubtype(
       const UINT  type        // Document subtype
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.DocumentSubtype(
       uint        type        // Document subtype
       )

### Parameters

**subtype**  
[in] Document subtype. The document subtype is passed using theIMTDocument::EnDocumentSubtypeenum.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
