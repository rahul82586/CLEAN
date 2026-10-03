[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Daily Reports](../Daily-Reports.md) / DailySelect

[Previous](DailyGetLight.md) | [Next](../Price-Data.md)

# IMTReportAPI::DailySelect

Request daily reports from a database according to specified criteria.
    
    
    MTAPIRES  IMTReportAPI::DailySelect(
       const IMTDatasetRequest*  request,  // Request description
       IMTDataset*               dataset   // Data set
       )

### Parameters

**request**  
[in] TheIMTDatasetRequestobject which describes the daily report request parameters.

**dataset**  
[out] TheIMTDatasetobject to which the daily reports received from the database in accordance with the request, will be added. The object must be previously created using theIMTReportAPI::DatasetAppendmethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases for quick report generation.
