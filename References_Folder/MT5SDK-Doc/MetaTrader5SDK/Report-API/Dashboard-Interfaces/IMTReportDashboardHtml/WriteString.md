[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / WriteString

[Previous](Write.md) | [Next](WriteSafe.md)

# IMTReportDashboardHtml::WriteString

Output an unformatted string into an HTML page (faster output).
    
    
    MTAPIRES  IMTReportDashboardHtml::WriteString(
       LPCWSTR  html        // output string
       )

### Parameters

**html**  
[in] Output sting with optional arguments.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Compared to [IMTReportDashboardHtml::Write](Write.md), which formats the output, this method uses less resources.
