[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [HTML](../HTML.md) / HtmlWriteString

[Previous](HtmlWrite.md) | [Next](HtmlWriteSafe.md)

# IMTReportAPI::HtmlWriteString

Output an unformatted string into an HTML page (faster output).
    
    
    MTAPIRES  IMTReportAPI::HtmlWriteString(
       LPCWSTR  string      // output string
       )

### Parameters

**string**  
[in] Output line.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The maximum size of an HTML report is 128 megabytes. When the maximum size is reached, the IMTReportAPI::HtmlWrite method will return the [MT_RET_REPORT_LIMIT_REPORT](../../../../Return-Codes/Report-Generation.md) error.
