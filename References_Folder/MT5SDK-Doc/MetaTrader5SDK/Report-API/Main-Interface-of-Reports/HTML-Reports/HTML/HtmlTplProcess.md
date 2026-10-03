[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [HTML](../HTML.md) / HtmlTplProcess

[Previous](HtmlTplNext.md) | [Next](../Charts.md)

# IMTReportAPI::HtmlTplProcess

Set the feature of the processing of all tags inside the current macros (predetermined tag).
    
    
    MTAPIRES  IMTReportAPI::HtmlTplProcess(
       const UINT  flags      // processing flag
       )

### Parameters

**flags**  
[in] Flag of a macros processing necessity. Transfered using theIMTReportAPI::EnTplProcessFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

In fact, this method dermines the necessity of processing of the macros received by the [IMTReportAPI::HtmlTplNext](HtmlTplNext.md) method.
