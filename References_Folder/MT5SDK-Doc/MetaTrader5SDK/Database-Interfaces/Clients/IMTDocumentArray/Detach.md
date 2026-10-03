[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTDocumentArray::Detach

Detach a document object from an array.

C++
    
    
    IMTDocument*  IMTDocumentArray::Detach(
       const UINT  pos      // Position of a document
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTDocument  CIMTDocumentArray.Detach(
       uint        pos      // Position of a document
       )

### Parameters

**pos**  
[in] Position of a document in an array starting with 0.

### Return Value

Returns a pointer to the detached document object.

### Note

This method removes a pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
