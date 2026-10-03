[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / TplProcess

[Previous](TplNext.md) | [Next](../IMTReportDashboardWidget.md)

# IMTReportAPI::TplProcess

Set the feature of the processing of all tags inside the current macro (predetermined tag).
    
    
    MTAPIRES  IMTReportAPI::TplProcess(
       const UINT  flags      // processing flag
       )

### Parameters

**flags**  
[in] Flag of a macro processing necessity. Transfered using theIMTReportAPI::EnTplProcessFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

In fact, this method determines the necessity of processing the macro received by the [IMTReportDashboardHtml::TplNext](TplNext.md) method.
