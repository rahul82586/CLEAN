[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [HTML Reports](../../HTML-Reports.md) / [HTML](../HTML.md) / HtmlTplLoadResource

[Previous](HtmlTplLoadFile.md) | [Next](HtmlTplNext.md)

# IMTReportAPI::HtmlTplLoadResource

Loading a template from a resource.
    
    
    MTAPIRES  IMTReportAPI::HtmlTplLoadResource(
       const UINT  resid,       // Resource ID
       LPCWSTR     restype      // Type of a resource
       )

### Parameters

**resid**  
[in] Resource ID in DLL.

**restype**  
[in] Type of a resource. One of the types predetermined in MSDN (http://msdn.microsoft.com/en-us/library/ms648009%28VS.85%29.aspx) or a custom type may be specified as a resource.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A resource file must necessarily be saved in the Unicode format.

Example:
    
    
    //--- using a template from a resource
    if((res=api->HtmlTplLoadResource(IDR_ACCOUNTS_GROUPS,RT_HTML))!=MT_RET_OK)
       return(res);
