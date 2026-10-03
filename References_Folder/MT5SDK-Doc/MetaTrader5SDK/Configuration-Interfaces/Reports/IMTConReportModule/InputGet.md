[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / InputGet

[Previous](InputNext.md) | [Next](../IMTConReportSink.md)

# IMTConReportModule::InputGet

Get the parameter of a report request by the name.

C++
    
    
    MTAPIRES  IMTConReportModule::InputGet(
       LPCWSTR       name,      // Parameter name
       IMTConParam*  param      // An object of the parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReportModule.InputGet(
       string        name,      // Parameter name
       CIMTConParam  param      // An object of the parameter
       )

Python (Manager API)
    
    
    MTConReportModule.InputGet()

### Parameters

**name**  
[in] Parameter Name.

**param**  
[out] An object of the parameter. The 'param' object must first be created using theIMTAdminAPI::ReportParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Parameters are set when requesting reports of the module from a manager terminal.
