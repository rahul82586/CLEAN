[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Clients](../Clients.md) / ClientIdsByGroup

[Previous](ClientIdsAll.md) | [Next](ClientUserLogins.md)

# IMTReportAPI::ClientIdsByGroup

Get the list of identifiers of all clients in the server database filtered by the list of groups.
    
    
    MTAPIRES  IMTReportAPI::ClientIdsByGroup(
       const LPCWSTR  groups,    // List of groups
       UINT64*&       ids,       // Array of identifiers
       UINT&          ids_total  // Number of identifiers
       )

### Parameters

**group**  
[in] Groups with which the requested clients are connected. Clients are selected according to the following rules:

**ids**  
[out] An array with client identifiers in the server database (IMTClient::RecordID).

**ids_total**  
[out] The number of identifiers in the 'ids' array.

  * If the client's [IMTClient::TradingGroup](../../../Database-Interfaces/Clients/IMTClient/TradingGroup.md) parameter value is in the list of specified groups.
  * If any of the client accounts ([IMTReportAPI::ClientUserLogins](ClientUserLogins.md)) belongs to one of the specified groups.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method allocates and fills an array of identifiers. A pointer to the passed block is placed to the 'ids' parameter. After use, the array placed in the 'ids' variable must be released using the [IMTReportAPI::Free](../Common-Functions/Free.md) Server API method.
