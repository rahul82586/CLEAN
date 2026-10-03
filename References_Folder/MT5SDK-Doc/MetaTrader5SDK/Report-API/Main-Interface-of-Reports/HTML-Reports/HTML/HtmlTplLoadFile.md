[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [HTML](../HTML.md) / HtmlTplLoadFile

[Previous](HtmlTplLoad.md) | [Next](HtmlTplLoadResource.md)

# IMTReportAPI::HtmlTplLoadFile

Loading a template from a file.
    
    
    MTAPIRES  IMTReportAPI::HtmlTplLoadFile(
       LPCWSTR  templname      // name of a template file
       )

### Parameters

**templname**  
[in] Name of the file that contains a template.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After the loading is complete the template is ready for work at once using the [IMTReportAPI::HtmlTplNext](HtmlTplNext.md) method.
