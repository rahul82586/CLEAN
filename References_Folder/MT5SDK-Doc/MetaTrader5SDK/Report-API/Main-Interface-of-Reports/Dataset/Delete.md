[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dataset](../Dataset.md) / Delete

[Previous](Clear.md) | [Next](Total.md)

# IMTReportAPI::DatasetDelete

Delete a data set from a dashboard.
    
    
    MTAPIRES  IMTReportAPI::DatasetDelete(
       const UINT  pos      // data set position
       )

### Parameters

**pos**  
[in] Data set position to be removed beginning with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The previous name of the method was DashboardDataDelete.

### 
