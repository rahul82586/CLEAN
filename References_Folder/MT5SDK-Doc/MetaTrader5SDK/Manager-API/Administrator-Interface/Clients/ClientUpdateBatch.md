[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / ClientUpdateBatch

[Previous](ClientUpdate.md) | [Next](ClientUpdateBatchArray.md)

# IMTAdminAPI::ClientUpdateBatch

Update a batch of clients in the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::ClientUpdateBatch(
       IMTClientArray*  clients, // array of clients
       MTAPIRES*        results  // array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ClientUpdateBatch(
       CIMTClientArray  clients, // array of clients
       MTRetCode[]      retcodes // array of results
       )

Python
    
    
    AdminAPI.ClientUpdateBatch(
       list[MTClient]   clients  # array of clients
       )

### Parameters

**clients**  
[in] A pointer to the object of theIMTClientArrayarray of clients.

**results**  
[out] An array with the results of adding of clients. The size of the 'results' array must not be less than that of 'clients'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified clients have been updated. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the clients have been updated. Analyze the 'results' array for more details of the execution results. The result of update of each client from the 'clients' array is added to 'results'. The index of a result corresponds to the index of a client in the source array.

### Note

A client can only be updated from the applications connected to the trade server, on which the client has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
