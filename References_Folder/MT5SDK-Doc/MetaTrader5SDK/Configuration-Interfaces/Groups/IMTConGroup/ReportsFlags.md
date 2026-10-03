[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / ReportsFlags

[Previous](ReportsMode.md) | [Next](ReportsEmail.md)

# IMTConGroup::ReportsFlags

Get the options of reports sending.

C++
    
    
    UINT64  IMTConGroup::ReportsFlags()  const

.NET (Gateway/Manager API)
    
    
    EnReportsFlags  CIMTConGroup.ReportsFlags()

Python (Manager API)
    
    
    MTConGroup.ReportsFlags

### Return Value

A value from the [IMTConGroup::EnReportsFlags (#enreportsflags)](Enumerations.md#enreportsflags) enumeration.

# IMTConGroup::ReportsFlags

Set the options of sending reports.

C++
    
    
    MTAPIRES  IMTConGroup::ReportsFlags(
       const UINT64    flags  // Options of reports sending
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.ReportsFlags(
       EnReportsFlags  flags  // Options of reports sending
       )

Python (Manager API)
    
    
    MTConGroup.ReportsFlags

### Parameters

**flags**  
[in] TheIMTConGroup::EnReportsFlagsenumeration is used to pass report sending options.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
