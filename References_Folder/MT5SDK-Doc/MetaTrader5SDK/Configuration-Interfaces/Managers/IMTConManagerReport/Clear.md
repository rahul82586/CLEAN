[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerReport](../IMTConManagerReport.md) / Clear

[Previous](Assign.md) | [Next](Report.md)

# IMTConManagerReport::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConManagerReport::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManagerReport.Clear()

Python (Manager API)
    
    
    bool  MTConManagerReport.Clear()

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.

### Note

This method cleans all fields ​​and removes embedded objects.
