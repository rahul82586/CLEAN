[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTDocumentArray::Next

Get a document object by its position.

C++
    
    
    IMTDocument*  IMTDocumentArray::Next(
       const UINT  pos      // Position of a document
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTDocument  CIMTDocumentArray.Next(
       uint        pos      // Document position
       )

### Parameters

**pos**  
[in] Position of a document in an array starting with 0.

### Return Value

If successful, a pointer to the document object at the specified position is returned. Otherwise, NULL is returned.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
