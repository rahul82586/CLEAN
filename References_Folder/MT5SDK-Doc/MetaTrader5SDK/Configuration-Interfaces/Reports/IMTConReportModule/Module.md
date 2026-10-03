[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / Module

[Previous](Description.md) | [Next](Index.md)

# IMTConReportModule::Module

Get the name of the file of a report module.

C++
    
    
    LPCWSTR  IMTConReportModule::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConReportModule.Module()

Python (Manager API)
    
    
    MTConReportModule.Module

### Return Value

If successful, it returns a pointer to a string with the file name of the report module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConReportModule](../IMTConReportModule.md) object.
