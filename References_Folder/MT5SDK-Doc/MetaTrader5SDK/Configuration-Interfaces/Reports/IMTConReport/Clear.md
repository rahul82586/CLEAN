[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConReport::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConReport::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.Clear()

Python (Manager API)
    
    
    MTConReport.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
