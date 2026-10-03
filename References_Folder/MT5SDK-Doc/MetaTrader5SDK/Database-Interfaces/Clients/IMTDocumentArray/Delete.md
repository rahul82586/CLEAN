[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTDocumentArray::Delete

Delete a document object by its position.

C++
    
    
    MTAPIRES  IMTDocumentArray::Delete(
       const UINT  pos      // Position of a document
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.Delete(
       uint        pos      // Position of a document
       )

### Parameters

**pos**  
[in] Position of a document in an array starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTDocument::Release](../IMTDocument/Release.md) method.
