[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / Clear

[Previous](Assign.md) | [Next](RecordID.md)

# IMTDocument::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTDocument::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears all fields ​​and removes nested objects.
