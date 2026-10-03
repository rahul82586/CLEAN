[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionSelectByGroup

[Previous](PositionGetByTickets.md) | [Next](PositionSelectByLogins.md)

# IMTServerAPI::PositionSelectByGroup

Request trading positions from a database for a group of accounts using additional criteria.
    
    
    MTAPIRES  IMTReportAPI::PositionSelectByGroup(
       LPCWSTR                   group,    // Group
       const INT64               from,     // Period from
       const INT64               to,       // Period to
       const IMTDatasetRequest*  request,  // Request description
       IMTDataset*               dataset   // Data set
       )

### Parameters

**group**  
[in] The group for which the positions are requested.

**from**  
[in] The beginning of the period for which you want to receive positions. The date is specified in seconds which have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you want to receive positions. The date is specified in seconds which have elapsed since 01.01.1970.

**request**  
[in] TheIMTDatasetRequestobject which described the position request criteria.

**dataset**  
[out] TheIMTDatasetobject to which positions received from the database in accordance with the request will be added. The object must be previously created using theIMTServerAPI::DatasetCreatemethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases.
