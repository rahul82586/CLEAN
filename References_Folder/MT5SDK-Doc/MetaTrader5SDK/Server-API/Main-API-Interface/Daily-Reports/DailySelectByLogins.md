[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailySelectByLogins

[Previous](DailySelectByGroup.md) | [Next](../Subscriptions.md)

# IMTServerAPI::DailySelectByLogins

Request daily reports from a database for a list of logins using additional criteria.
    
    
    MTAPIRES  IMTReportAPI::DailySelectByLogins(
       LPCWSTR                   group,    // Group
       const INT64               from,     // Period from
       const INT64               to,       // Period to
       const IMTDatasetRequest*  request,  // Request description
       IMTDataset*               dataset   // Data set
       )

### Parameters

**group**  
[in] The groups the daily reports are requested for. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex.

**from**  
[in] The beginning of the period for which you need to get daily reports. The date is specified in seconds which have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get daily reports. The date is specified in seconds which have elapsed since 01.01.1970.

**request**  
[in] TheIMTDatasetRequestobject which describes the daily report request parameters.

**dataset**  
[out] TheIMTDatasetobject to which the daily reports received from the database in accordance with the request, will be added. The object must be previously created using theIMTServerAPI::DatasetCreatemethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables highly efficient sampling of relevant databases.
