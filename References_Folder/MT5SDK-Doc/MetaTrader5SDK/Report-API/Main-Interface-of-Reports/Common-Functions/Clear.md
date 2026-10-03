[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Common Functions](../Common-Functions.md) / Clear

[Previous](IsStopeed.md) | [Next](LicenseCheck.md)

# IMTReportAPI::Clear

Clear all the results added to the report.
    
    
    MTAPIRES  IMTReportAPI::Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects. E.g., fully clears the report HTML contents or a table data.
