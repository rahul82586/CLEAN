[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / ParameterNext

[Previous](ParameterTotal.md) | [Next](ParameterGet.md)

# IMTConReport::ParameterNext

Get parameters of a report by the index.

C++
    
    
    MTAPIRES  IMTConReport::ParameterNext(
       const UINT    pos,       // Position of the report
       IMTConParam*  param      // An object of a report parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.ParameterNext(
       uint          pos,       // Position of the report
       CIMTConParam  param      // An object of a report parameter
       )

Python (Manager API)
    
    
    MTConReport.ParameterNext(
       pos           # Position of the report
       )

### Parameters

**pos**  
[in] Position of the plugin, starting with 0.

**param**  
[out] An object of a report parameter. The 'param' object must first be created using theIMTAdminAPI::ReportParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the parameters of a report with a specified index to the param object.
