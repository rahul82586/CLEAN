[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderSelectByLogins

[Previous](OrderSelectByGroup.md) | [Next](HistorySubscribe.md)

# IMTServerAPI::OrderSelectByLogins

Request open orders from a database for a list of logins using additional criteria.
    
    
    MTAPIRES  IMTReportAPI::OrderSelectByLogins(
       const UINT64*             logins,       // logins
       const UINT                logins_total, // number of logins
       const IMTDatasetRequest*  request,      // Request description
       IMTDataset*               dataset       // Data set
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**request**  
[in] TheIMTDatasetRequestobject, which describes order request criteria.

**dataset**  
[out] TheIMTDatasetobject to which orders received from the database in accordance with the request will be added. The object must be previously created using theIMTServerAPI::DatasetCreatemethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases.
