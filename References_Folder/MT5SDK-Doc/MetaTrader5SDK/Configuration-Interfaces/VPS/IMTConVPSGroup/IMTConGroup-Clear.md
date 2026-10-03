[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSGroup](../IMTConGroup.md) / IMTConGroup Clear

[Previous](IMTConGroup-Assign.md) | [Next](IMTConGroup-Group.md)

# IMTConVPSGroup::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConVPSGroup::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSGroup.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method cleans all fields ​​and removes embedded objects.
