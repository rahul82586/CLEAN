[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardHeight

[Previous](DashboardWidth.md) | [Next](DashboardTitle.md)

# IMTReportAPI::DashboardHeight

Get dashboard height.
    
    
    UINT  IMTReportAPI::DashboardHeight()  const

### Return Value

Dashboard height in pixels.

# IMTReportAPI::DashboardHeight

Set dashboard height.
    
    
    MTAPIRES  IMTReportAPI::DashboardHeight(
       const UINT  width      // height
       )

### Parameters

**width**  
[in] Dashboard height in pixels.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the height is not set, the height of the report workspace in the Manager terminal is used.
