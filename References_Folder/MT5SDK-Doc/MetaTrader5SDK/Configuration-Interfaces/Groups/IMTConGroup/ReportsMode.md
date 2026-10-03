[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / ReportsMode

[Previous](CurrencyDigitsSet.md) | [Next](ReportsFlags.md)

# IMTConGroup::ReportsMode

Get the mode of report generation.

C++
    
    
    UINT  IMTConGroup::ReportsMode()  const

.NET (Gateway/Manager API)
    
    
    EnReportsMode  CIMTConGroup.ReportsMode()

Python (Manager API)
    
    
    MTConGroup.ReportsMode

### Return Value

A value from the [IMTConGroup::EnReportsMode (#enreportsmode)](Enumerations.md#enreportsmode) enumeration.

# IMTConGroup::ReportsMode

Set the mode of report generation.

C++
    
    
    MTAPIRES  IMTConGroup::ReportsMode(
       const UINT     mode   // Report generation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.ReportsMode(
       EnReportsMode  mode   // Report generation mode
       )

Python (Manager API)
    
    
    MTConGroup.ReportsMode

### Parameters

**mode**  
[in] The report generation mode is passed using theIMTConGroup::EnReportsModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
