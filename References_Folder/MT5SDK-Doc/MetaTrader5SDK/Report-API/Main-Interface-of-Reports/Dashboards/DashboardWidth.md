[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardWidth

[Previous](../Dashboards.md) | [Next](DashboardHeight.md)

# IMTReportAPI::DashboardWidth

Get a dashboard width.
    
    
    UINT  IMTReportAPI::DashboardWidth()  const

### Return Value

Dashboard width in pixels.

# IMTReportAPI::DashboardWidth

Set a dashboard width.
    
    
    MTAPIRES  IMTReportAPI::DashboardWidth(
       const UINT  width      // width
       )

### Parameters

**width**  
[in] Dashboard width in pixels.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the width is not set, the width of the report workspace in the Manager terminal is used.
