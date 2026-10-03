[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealSelect

[Previous](DealGet.md) | [Next](../Positions.md)

# IMTReportAPI::DealSelect

Request deals from a database according to specified criteria.
    
    
    MTAPIRES  IMTReportAPI::UserSelect(
       const IMTDatasetRequest*  request,  // Request description
       IMTDataset*               dataset   // Data set
       )

### Parameters

**request**  
[in] TheIMTDatasetRequestobject, which describes deal request criteria.

**dataset**  
[out] TheIMTDatasetobject to which deals received from the data base in accordance with the request will be added. The object must be previously created using theIMTReportAPI::DatasetAppendmethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases for quick report generation.
