[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionSelect

[Previous](PositionGetByTicket.md) | [Next](../Trading-Data.md)

# IMTReportAPI::PositionSelect

Request trading positions from a database according to specified criteria.
    
    
    MTAPIRES  IMTReportAPI::PositionSelect(
       const IMTDatasetRequest*  request,  // Request description
       IMTDataset*               dataset   // Data set
       )

### Parameters

**request**  
[in] TheIMTDatasetRequestobject which described the position request criteria.

**dataset**  
[out] TheIMTDatasetobject to which positions received from the database in accordance with the request will be added. The object must be previously created using theIMTReportAPI::DatasetAppendmethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases for quick report generation.
