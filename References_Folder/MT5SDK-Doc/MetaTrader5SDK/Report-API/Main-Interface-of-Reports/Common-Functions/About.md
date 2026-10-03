[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Common Functions](../Common-Functions.md) / About

[Previous](LicenseCheck.md) | [Next](../Report-Parameters.md)

# IMTReportAPI::About

Quickly receive the description of the server on which the module is running.
    
    
    MTAPIRES  IMTReportAPI::About(
       MTReportServerInfo&  info  // Reference to MTReportServerInfo
       )

### Parameters

**info**  
[in] A reference to theMTReportServerInfostructure.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This function copies the [MTReportServerInfo](../../../Structures/MTReportServerInfo.md) structure to the info parameter.
