[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Report Parameters](../Report-Parameters.md) / ParamGroups

[Previous](ParamTo.md) | [Next](ParamSymbols.md)

# IMTReportAPI::ParamGroups

Get the "Groups" parameter value line set in a manager terminal.
    
    
    LPCWSTR  IMTReportAPI::ParamGroups()

### Return Value

If successful, it returns a pointer to the string with the "Groups" parameter value. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConParam](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) object.
