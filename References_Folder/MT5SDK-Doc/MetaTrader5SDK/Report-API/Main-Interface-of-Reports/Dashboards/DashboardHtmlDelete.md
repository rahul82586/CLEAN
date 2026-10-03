[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardHtmlDelete

[Previous](DashboardHtmlClear.md) | [Next](DashboardHtmlTotal.md)

# IMTReportAPI::DashboardHtmlDelete

Delete a set of HTML data from a dashboard.
    
    
    MTAPIRES  IMTReportAPI::DashboardHtmlDelete(
       const UINT  pos      // data set position
       )

### Parameters

**pos**  
[in] Data set position to be removed beginning with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
