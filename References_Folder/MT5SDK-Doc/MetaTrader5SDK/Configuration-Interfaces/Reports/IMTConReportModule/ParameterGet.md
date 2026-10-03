[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / ParameterGet

[Previous](ParameterNext.md) | [Next](InputTotal.md)

# IMTConReportModule::ParameterGet

Get a report module parameter by its name.

C++
    
    
    MTAPIRES  IMTConReportModule::ParameterGet(
       LPCWSTR       name,      // Parameter name
       IMTConParam*  param      // An object of a report parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReportModule.ParameterGet(
       string        name,      // Parameter name
       CIMTConParam  param      // An object of a report parameter
       )

Python (Manager API)
    
    
    MTConReportModule.ParameterGet()

### Parameters

**name**  
[in] Parameter Name.

**param**  
[out] An object of a report parameter. The 'param' object must first be created using theIMTAdminAPI::ReportParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConParam::Name](../../Additional-Parameters/IMTConParam/Name.md) value is used as the parameter name.
