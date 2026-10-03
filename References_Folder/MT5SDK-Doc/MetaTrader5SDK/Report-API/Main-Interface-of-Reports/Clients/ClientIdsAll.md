[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Clients](../Clients.md) / ClientIdsAll

[Previous](ClientGetHistory.md) | [Next](ClientIdsByGroup.md)

# IMTReportAPI::ClientIdsAll

Get the list of identifiers of all clients in the server database.
    
    
    MTAPIRES  IMTReportAPI::ClientIdsAll(
       UINT64*&      ids,        // Array of identifiers
       UINT&         ids_total   // Number of identifier
       )

### Parameters

**ids**  
[out] An array with identifiers of all clients in the server database (IMTClient::RecordID).

**ids_total**  
[out] The number of identifiers in the 'ids' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method allocates and fills an array of identifiers. A pointer to the passed block is placed to the 'ids' parameter. After use, the array placed in the 'ids' variable must be released using the [IMTReportAPI::Free](../Common-Functions/Free.md) Server API method.
