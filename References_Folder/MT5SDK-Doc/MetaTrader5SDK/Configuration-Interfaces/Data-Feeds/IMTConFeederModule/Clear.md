[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConFeederModule::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConFeederModule::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederModule.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
