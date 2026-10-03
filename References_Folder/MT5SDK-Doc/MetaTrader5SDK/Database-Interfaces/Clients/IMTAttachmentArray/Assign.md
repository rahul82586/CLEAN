[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTAttachmentArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTAttachmentArray::Assign(
       const IMTAttachmentArray*  array     // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.Assign(
       CIMTAttachmentArray        array     // source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
