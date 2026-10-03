[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Clients](../Clients.md) / ClientGetHistory

[Previous](ClientGet.md) | [Next](ClientIdsAll.md)

# IMTReportAPI::ClientGetHistory

Get the history of client changes.
    
    
    MTAPIRES  IMTReportAPI::ClientGetHistory(
       const UINT64     client_id,  // ID
       const UINT64     author,     // Author
       const INT64      from,       // Period beginning
       const UINT64     to,         // Period ending
       IMTClientArray*  history     // An object of client arrays
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**author**  
[in] The login of the manager account by whom the client was changed. The login is equal to theIMTConManager::Loginvalue.

**from**  
[in] The beginning of the period for which you wish to get the history of client changes. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you wish to get the history of client changes. The date is specified in seconds since 01.01.1970.

**history**  
[out] An object of an array of clients. The 'history' object must be previously created using theIMTReportAPI::ClientCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method returns an array of client descriptions: all the client states after changes by the specified author in the specified time period.
