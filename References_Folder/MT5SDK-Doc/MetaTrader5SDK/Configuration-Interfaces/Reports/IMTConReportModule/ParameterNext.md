[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / ParameterNext

[Previous](ParameterTotal.md) | [Next](ParameterGet.md)

# IMTConReportModule::ParameterNext

Get report module parameters by the index.

C++
    
    
    MTAPIRES  IMTConReportModule::ParameterNext(
       const UINT    pos,       // Position of the plugin
       IMTConParam*  param      // An object of a report parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReportModule.ParameterNext(
       uint          pos,       // Position of the plugin
       CIMTConParam  param      // An object of a report parameter
       )

Python (Manager API)
    
    
    MTConReportModule.ParameterNext(
       pos           # Position of the plugin
       )

### Parameters

**pos**  
[in] Position of the report, starting with 0.

**param**  
[out] An object of a report parameter. The 'param' object must first be created using theIMTAdminAPI::ReportParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the parameters of a report module with a specified index to the param object.
