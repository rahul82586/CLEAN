[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTDocumentArray::UpdateCopy

Change a document at the specified position of an array by copying the parameters of a passed document object.

C++
    
    
    MTAPIRES  IMTDocumentArray::UpdateCopy(
       const UINT          pos,      // Position
       const IMTDocument*  comment   // Document object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.UpdateCopy(
       uint                pos,      // Position
       CIMTDocument        document  // Document object
       )

### Parameters

**pos**  
[in] Position of a document in an array starting with 0.

**document**  
[in]Document object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method copies the 'document' object parameters to the document object at the specified position in the array.
