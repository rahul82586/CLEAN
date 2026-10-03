[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dashboards](../Dashboards.md) / DashboardHtmlClear

[Previous](DashboardHtmlAppend.md) | [Next](DashboardHtmlDelete.md)

# IMTReportAPI::DashboardHtmlClear

Delete all dashboard HTML data.
    
    
    MTAPIRES  IMTReportAPI::DashboardHtmlClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After calling this method, all previously created HTML data are deleted ([IMTDataset](../../Dataset-Interfaces/IMTDataset.md) objects).
