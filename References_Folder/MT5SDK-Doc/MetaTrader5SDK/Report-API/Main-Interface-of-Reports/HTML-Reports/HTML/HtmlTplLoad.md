[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [HTML](../HTML.md) / HtmlTplLoad

[Previous](HtmlWriteSafe.md) | [Next](HtmlTplLoadFile.md)

# IMTReportAPI::HtmlTplLoad

Loading a template from the submitted line.
    
    
    MTAPIRES  IMTReportAPI::HtmlTplLoad(
       LPCWSTR  templstr      // Template line
       )

### Parameters

**templstr**  
[in] The line, describing a template.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After the loading is complete the template is ready for work at once using the [IMTReportAPI::HtmlTplNext](HtmlTplNext.md) method.
