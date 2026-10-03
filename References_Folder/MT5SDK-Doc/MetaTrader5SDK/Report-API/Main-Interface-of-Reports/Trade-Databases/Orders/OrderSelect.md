[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderSelect

[Previous](OrderGet.md) | [Next](HistoryGet.md)

# IMTReportAPI::OrderSelect

Request open orders from a database according to specified criteria.
    
    
    MTAPIRES  IMTReportAPI::OrderSelect(
       const IMTDatasetRequest*  request,  // Request description
       IMTDataset*               dataset   // Data set
       )

### Parameters

**request**  
[in] TheIMTDatasetRequestobject, which describes order request criteria.

**dataset**  
[out] TheIMTDatasetobject to which orders received from the database in accordance with the request will be added. The object must be previously created using theIMTReportAPI::DatasetAppendmethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases for quick report generation.
