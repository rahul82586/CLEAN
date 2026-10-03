[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / TplLoad

[Previous](WriteChart.md) | [Next](TplLoadFile.md)

# IMTReportDashboardHtml::TplLoad

Load a template from the submitted line.
    
    
    MTAPIRES  IMTReportDashboardHtml::TplLoad(
       LPCWSTR  templstr      // template line
       )

### Parameters

**templstr**  
[in] The line describing a template.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

After the loading is complete the template is ready for work at once using the [IMTReportDashboardHtml::TplNext](TplNext.md) method.
