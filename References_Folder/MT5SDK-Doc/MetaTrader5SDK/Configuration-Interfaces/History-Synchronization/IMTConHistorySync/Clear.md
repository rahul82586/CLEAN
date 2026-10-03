[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / Clear

[Previous](Assign.md) | [Next](Server.md)

# IMTConHistorySync::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConHistorySync::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.Clear()

Python (Manager API)
    
    
    bool  MTConHistorySync.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
