[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / Description

[Previous](Vendor.md) | [Next](Module.md)

# IMTConReportModule::Description

Get the description of a report module.

C++
    
    
    LPCWSTR  IMTConReportModule::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConReportModule.Description()

Python (Manager API)
    
    
    MTConReportModule.Description

### Return Value

If successful, it returns a pointer to a string with the description of a report module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConReportModule](../IMTConReportModule.md) object.
