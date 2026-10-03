[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTAttachmentArray::Shift

Change the attachment position in an array.

C++
    
    
    MTAPIRES  IMTAttachmentArray::Shift(
       const UINT  pos,       // attachment position
       const int   shift      // shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.Shift(
       uint        pos,       // attachment position
       int         shift      // shift
       )

### Parameters

**pos**  
[in] Position of an attachment in the array, starting with 0.

**shift**  
[in] The shift of the attachment relative to its current position. A negative value means shift towards the array beginning, a positive value means shift towards its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
