[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / DocumentName

[Previous](DocumentSubtype.md) | [Next](DocumentComment.md)

# IMTDocument::DocumentName

Get the document name.

C++
    
    
    LPCWSTR  IMTDocument::DocumentName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDocument.DocumentName()

### Return Value

If successful, a pointer to a string with the document name is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDocument](../IMTDocument.md) object.

# IMTDocument::DocumentName

Set the document name.

C++
    
    
    MTAPIRES  IMTDocument::DocumentName(
       LPCWSTR       name          // Document name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.DocumentName(
       string        name          // Document name
       )

### Parameters

**type**  
[in] Document name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The document name length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
