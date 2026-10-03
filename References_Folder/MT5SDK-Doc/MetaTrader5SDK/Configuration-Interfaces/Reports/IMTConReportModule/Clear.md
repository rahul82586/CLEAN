[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConReportModule::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConReportModule::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReportModule.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
