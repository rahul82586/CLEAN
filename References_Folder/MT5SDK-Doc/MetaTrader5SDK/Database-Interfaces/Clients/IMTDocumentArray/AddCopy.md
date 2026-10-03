[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTDocumentArray::AddCopy

Add a copy of a document object at the end of an array.

C++
    
    
    MTAPIRES  IMTDocumentArray::AddCopy(
       const IMTDocument*  document  // Document to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.AddCopy(
       CIMTDocument        document  // Document to be added
       )

### Parameters

**document**  
[in]Document object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'client' object and places it at the end of the array.

# IMTDocumentArray::AddCopy

Add copies of document objects into an array.

C++
    
    
    MTAPIRES  IMTDocumentArray::AddCopy(
       const IMTDocumentArray*  array     // Array of documents to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.AddCopy(
       CIMTDocumentArray        array      // Array of documents to be added
       )

### Parameters

**array**  
[in] Object of the array of documents.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates copies of comment objects belonging to the 'array' object and inserts them at the end of the current array.
