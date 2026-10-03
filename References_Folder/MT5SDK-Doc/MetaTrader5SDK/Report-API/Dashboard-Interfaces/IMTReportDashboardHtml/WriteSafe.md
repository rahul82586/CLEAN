[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / WriteSafe

[Previous](WriteString.md) | [Next](WriteChart.md)

# IMTReportDashboardHtml::WriteSafe

Output of a line in HTML with HTML service symbols screening.
    
    
    MTAPIRES  IMTReportDashboardHtml::WriteSafe(
       LPCWSTR     html,      // output line
       const UINT  flags      // output flags
       )

### Parameters

**html**  
[in] Output line.

**flags**  
[in] Additional output flags transferred using theIMTReportAPI::EnHtmlSafeFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

During the output of a line, special symbols used in HTML are replaced with special codes with the use of this method. E.g., "<" is replaced with "&lt;".
