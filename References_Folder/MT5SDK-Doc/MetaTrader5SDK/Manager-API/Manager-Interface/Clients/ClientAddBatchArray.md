[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientAddBatchArray

[Previous](ClientAddBatch.md) | [Next](ClientUpdate.md)

# IMTManagerAPI::ClientAddBatchArray

Add a batch of clients to the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::ClientAddBatchArray(
       IMTClient**    clients,       // array of clients
       const UINT     clients_total, // number of clients in the array
       MTAPIRES*      results        // array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ClientAddBatchArray(
       IMTClient[]    clients,       // array of clients
       MTRetCode[]    retcodes       // array of results
       )

### Parameters

**clients**  
[in] A pointer to the array ofclients.

**clients_total**  
[in] The number of clients in the 'clients' array.

**results**  
[out] An array with the results of adding of clients. The size of the 'results' array must not be less than that of 'clients'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified clients have been added. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the clients have been added. Analyze the 'results' array for more details of the execution results. The result of adding of each client from the 'clients' array is added to 'results'. The index of a result corresponds to the index of a client in the source array.

### Note

A client can only be added to the database of the server, to which the application is connected.

When creating a client, the server automatically assigns to this client a unique identifier [IMTClient::RecordID](../../../Database-Interfaces/Clients/IMTClient/RecordID.md).

During addition, the integrity of client records is checked. The [IMTClient::PersonName](../../../Database-Interfaces/Clients/IMTClient/PersonName.md) field must be filled in the record.
