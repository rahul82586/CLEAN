[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderSelectByGroup

[Previous](OrderGetByTickets.md) | [Next](OrderSelectByLogins.md)

# IMTServerAPI::OrderSelectByGroup

Request open orders from a database for a group of accounts using additional criteria.
    
    
    MTAPIRES  IMTServerAPI::OrderSelectByGroup(
       LPCWSTR                   group,    // Group
       const IMTDatasetRequest*  request,  // Request description
       IMTDataset*               dataset   // Data set
       )

### Parameters

**group**  
[in] The group for which the orders are requested.

**request**  
[in] TheIMTDatasetRequestobject, which describes order request criteria.

**dataset**  
[out] TheIMTDatasetobject to which orders received from the database in accordance with the request will be added. The object must be previously created using theIMTServerAPI::DatasetCreatemethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases.
