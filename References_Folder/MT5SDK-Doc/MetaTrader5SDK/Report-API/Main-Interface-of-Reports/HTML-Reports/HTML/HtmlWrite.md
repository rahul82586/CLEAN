[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [HTML](../HTML.md) / HtmlWrite

[Previous](../HTML.md) | [Next](HtmlWriteString.md)

# IMTReportAPI::HtmlWrite

Output of a line with formatting to a HTML page.
    
    
    MTAPIRES  IMTReportAPI::HtmlWrite(
       LPCWSTR  format,     // Output line
                ...         // Options arguments
       )

### Parameters

**format**  
[in] Output line with optional arguments.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Maximum allowed size of an HTML report is 128MB. If this limit is reached, IMTReportAPI::HtmlWrite will return error [MT_RET_REPORT_LIMIT_REPORT](../../../../Return-Codes/Report-Generation.md).

Example:
    
    
    int value=100;
    HtmlWrite(L"Text %d",value); // This example will display "Text 100" in the output HTML
