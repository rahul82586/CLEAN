[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / TplLoadFile

[Previous](TplLoad.md) | [Next](TplLoadResource.md)

# IMTReportDashboardHtml::TplLoadFile

Load a template from a file.
    
    
    MTAPIRES  IMTReportDashboardHtml::TplLoadFile(
       LPCWSTR  templname      // name of a template file
       )

### Parameters

**templname**  
[in] Name of the file that contains a template.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

After the loading is complete, the template is ready for work at once using the [IMTReportDashboardHtml::TplNext](TplNext.md) method.
