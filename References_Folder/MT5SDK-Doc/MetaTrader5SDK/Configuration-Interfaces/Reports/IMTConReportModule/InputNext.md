[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / InputNext

[Previous](InputTotal.md) | [Next](InputGet.md)

# IMTConReportModule::InputNext

Get the parameter of a report request by the index.

C++
    
    
    MTAPIRES  IMTConReportModule::InputNext(
       const UINT    pos,       // Position of the parameter
       IMTConParam*  param      // An object of the parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReportModule.InputNext(
       uint          pos,       // Position of the parameter
       CIMTConParam  param      // An object of the parameter
       )

Python (Manager API)
    
    
    MTConReportModule.InputNext(
       pos           # Position of the parameter
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**param**  
[out] An object of the parameter. The 'param' object must first be created using theIMTAdminAPI::ReportParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Parameters are set when requesting reports of the module from a manager terminal.
