[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / Write

[Previous](Clear.md) | [Next](WriteString.md)

# IMTReportDashboardHtml::Write

Output of a line with formatting to an HTML page.
    
    
    MTAPIRES  IMTReportDashboardHtml::Write(
       LPCWSTR  format,     // output line
                ...         // optional arguments
       )

### Parameters

**format**  
[in] Output line with optional arguments.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

Maximum size of an HTML part is 128 MB. When reaching the maximum size, the IMTReportDashboardHtml::Write method returns the [MT_RET_REPORT_LIMIT_REPORT](../../../Return-Codes/Report-Generation.md) error.

Example:
    
    
    int value=100;
    Write(L"Text %d",value); // This example will display "Text 100" in the output HTML
