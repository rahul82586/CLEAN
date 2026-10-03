[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / Vendor

[Previous](Name.md) | [Next](Description.md)

# IMTConReportModule::Vendor

Get the name of the report module provider.

C++
    
    
    LPCWSTR  IMTConReportModule::Vendor()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConReportModule.Vendor()

Python (Manager API)
    
    
    MTConReportModule.Vendor

### Return Value

If successful, it returns a pointer to a string with the name of the report module provider. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConReportModule](../IMTConReportModule.md) object.
