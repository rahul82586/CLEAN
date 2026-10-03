[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / TplNext

[Previous](TplLoadResource.md) | [Next](TplProcess.md)

# IMTReportDashboardHtml::TplNext

Get the next macro (predetermined tag) from a template for processing.
    
    
    MTAPIRES  IMTReportDashboardHtml::TplNext(
       MTAPISTR&  tag,          // name of a macro
       UINT       *counter      // processings counter
       )

### Parameters

**tag**  
[in] Name of a macro (predetermined tag).

***counter**  
[in] A pointer to the counter where the number of the previous processings of a received (current) tag is placed. This parameter may not be considered, if the number of processings of the current tag is not important.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Predetermined tag has the look <mt5:name/> or <mt5:name>...</mt5:name>. This method returns the name of a received tag (in this example, it is "name").
