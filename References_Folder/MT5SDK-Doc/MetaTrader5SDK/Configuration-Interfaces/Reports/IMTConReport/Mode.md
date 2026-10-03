[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / Mode

[Previous](Module.md) | [Next](ParameterAdd.md)

# IMTConReport::Mode

Get the report operation mode.

C++
    
    
    UINT  IMTConReport::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnReportMode  CIMTConReport.Mode()

Python (Manager API)
    
    
    MTConReport.Mode

### Return Value

A value of the [IMTConReport::EnReportMode (#enreportmode)](Enumerations.md#enreportmode) enumeration.

# IMTConReport::Mode

Set the report operation mode.

C++
    
    
    MTAPIRES  IMTConReport::Mode(
       const UINT    mode    // Operation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.Mode(
       EnReportMode  mode    // Operation mode
       )

Python (Manager API)
    
    
    MTConReport.Mode

### Parameters

**mode**  
[in] TheIMTConReport::EnReportModeenumeration is used to pass the operation mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
