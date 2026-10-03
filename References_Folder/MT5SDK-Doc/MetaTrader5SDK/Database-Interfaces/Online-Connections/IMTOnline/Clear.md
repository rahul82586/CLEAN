[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnline](../IMTOnline.md) / Clear

[Previous](Assign.md) | [Next](SessionID.md)

# IMTOnline::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTOnline::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnline.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
