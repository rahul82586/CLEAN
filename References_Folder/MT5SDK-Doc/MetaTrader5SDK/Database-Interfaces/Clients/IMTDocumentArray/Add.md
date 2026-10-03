[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTDocumentArray::Add

Add a document object to the end of an array.

C++
    
    
    MTAPIRES  IMTDocumentArray::Add(
       IMTDocument*  document  // Document to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.Add(
       CIMTDocument  document  // Document to be added
       )

### Parameters

**document**  
[in]Document object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the lifetime of the 'document' object is passed to the array object. Thus, when deleting an array object (by a call of [IMTDocumentArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTDocumentArray::Add

Add a document array object to the end of an array.

C++
    
    
    MTAPIRES  IMTDocumentArray::Add(
       IMTDocumentArray*  array    // Array of documents to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.Add(
       CIMTDocumentArray  array    // Array of documents to be added
       )

### Parameters

**array**  
[in] Object of the array of documents.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the 'array' object, at the end of the current array and clears the 'array' object.

### Example
    
    
    //--- example
       IMTDocumentArray *array   =api->DocumentCreateArray();   
       IMTDocument      *document=api->DocumentCreate();
    //---
       array->Add(document);  // after that the lifetime is controlled by the array
       array->Delete(0);      // delete the first element, after that a pointer in 'document' becomes invalid ('Release' was called)
     
    //--- Incorrect use example
       IMTDocumentArray *array   =api->DocumentCreateArray();   
       IMTDocument      *document=api->DocumentCreate();
    //---
       array->Add(document);
       array->Add(document); // in this case the array will contain two pointers to one and the same object!
       //--- an attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
