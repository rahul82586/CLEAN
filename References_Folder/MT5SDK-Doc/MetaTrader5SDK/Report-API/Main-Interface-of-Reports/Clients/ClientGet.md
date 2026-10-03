[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Clients](../Clients.md) / ClientGet

[Previous](ClientCreateArray.md) | [Next](ClientGetHistory.md)

# IMTReportAPI::ClientGet

Get a client by identifier.
    
    
    MTAPIRES  IMTReportAPI::ClientGet(
       const UINT64  client_id,  // ID
       IMTClient*    client      // Client object
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**client**  
[out] Client object. The 'client' object must be previously created using theIMTReportAPI::ClientCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method copies data of a client with the specified ID, to the 'client' object.
