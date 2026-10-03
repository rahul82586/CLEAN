[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [HTML](../HTML.md) / HtmlWriteSafe

[Previous](HtmlWriteString.md) | [Next](HtmlTplLoad.md)

# IMTReportAPI::HtmlWriteSafe

Output of a line in HTML with HTML service symbols screening.
    
    
    MTAPIRES  IMTReportAPI::HtmlWriteSafe(
       LPCWSTR     html,      // Output line
       const UINT  flags      // Output flags
       )

### Parameters

**html**  
[in] Output line.

**flags**  
[in] Additional output flags transferred using theIMTReportAPI::EnHtmlSafeFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

During the output of a line with the use of this method special symbols used in HTML are replaced with special codes. E.g., "<" is replaced with "&lt;".
