[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / ParameterClear

[Previous](ParameterDelete.md) | [Next](ParameterShift.md)

# IMTConReport::ParameterClear

Clear the list of report parameters.

C++
    
    
    MTAPIRES  IMTConReport::ParameterClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.ParameterClear()

Python (Manager API)
    
    
    MTConReport.ParameterClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of report parameters.
