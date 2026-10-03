[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Report Parameters](../Report-Parameters.md) / ParamSymbols

[Previous](ParamGroups.md) | [Next](ParamIEVersion.md)

# IMTReportAPI::ParamSymbols

Get the "Symbols" parameter value line set in a manager terminal.
    
    
    LPCWSTR  IMTReportAPI::ParamSymbols()

### Return Value

If successful, it returns a pointer to the string with the "Symbols" parameter value. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConParam](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) object.
