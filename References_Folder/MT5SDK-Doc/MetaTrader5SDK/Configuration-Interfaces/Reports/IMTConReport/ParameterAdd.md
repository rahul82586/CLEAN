[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / ParameterAdd

[Previous](Mode.md) | [Next](ParameterUpdate.md)

# IMTConReport::ParameterAdd

Add a report parameter.

C++
    
    
    MTAPIRES  IMTConReport::ParameterAdd(
       IMTConParam*  param      // An object of a report parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.ParameterAdd(
       CIMTConParam  param      // An object of a report parameter
       )

Python (Manager API)
    
    
    MTConReport.ParameterAdd(
       param         # An object of a report parameter
       )

### Parameters

**param**  
[in] An object of a report parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
