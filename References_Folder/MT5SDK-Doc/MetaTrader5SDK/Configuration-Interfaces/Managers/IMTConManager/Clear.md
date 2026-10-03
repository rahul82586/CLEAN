[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / Clear

[Previous](Assign.md) | [Next](Login.md)

# IMTConManager::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConManager::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.Clear()

Python (Manager API)
    
    
    MTConManager.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
