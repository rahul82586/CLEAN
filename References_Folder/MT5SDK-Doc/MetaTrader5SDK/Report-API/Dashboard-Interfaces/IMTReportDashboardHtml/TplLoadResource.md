[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dashboard Interfaces](../../Dashboard-Interfaces.md) / [IMTReportDashboardHtml](../IMTReportDashboardHtml.md) / TplLoadResource

[Previous](TplLoadFile.md) | [Next](TplNext.md)

# IMTReportDashboardHtml::TplLoadResource

Load a template from a resource.
    
    
    MTAPIRES  IMTReportDashboardHtml::TplLoadResource(
       const UINT  resid,       // resource ID
       LPCWSTR     restype      // resource type
       )

### Parameters

**resid**  
[in] Resource ID in DLL.

**restype**  
[in] Resource type. One of the types predetermined in MSDN (http://msdn.microsoft.com/en-us/library/ms648009%28VS.85%29.aspx) or a custom type may be specified as a resource.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

A resource file should necessarily be saved in the Unicode format.

Example:
    
    
    //--- use a template from a resource
    if((res=api->TplLoadResource(IDR_ACCOUNTS_GROUPS,RT_HTML))!=MT_RET_OK)
       return(res);
