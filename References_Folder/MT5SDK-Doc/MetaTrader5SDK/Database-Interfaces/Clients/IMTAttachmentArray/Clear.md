[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTAttachmentArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTAttachmentArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes nested objects.
