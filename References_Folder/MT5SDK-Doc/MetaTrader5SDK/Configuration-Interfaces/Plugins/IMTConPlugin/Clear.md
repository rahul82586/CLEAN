[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConPlugin::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConPlugin::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.Clear()

Python (Manager API)
    
    
    MTConPlugin.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
