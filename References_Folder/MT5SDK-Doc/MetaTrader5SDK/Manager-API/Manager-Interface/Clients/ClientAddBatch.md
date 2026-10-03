[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientAddBatch

[Previous](ClientAdd.md) | [Next](ClientAddBatchArray.md)

# IMTManagerAPI::ClientAddBatch

Add a batch of clients to the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::ClientAddBatch(
       IMTClientArray*  clients, // array of clients
       MTAPIRES*        results  // array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ClientAddBatch(
       CIMTClientArray  clients, // array of clients
       MTRetCode[]      retcodes // array of results
       )

Python
    
    
    ManagerAPI.ClientAddBatch(
       list[MTClient]   clients  # array of clients
       )

### Parameters

**clients**  
[in] A pointer to the object of theIMTClientArrayarray of clients.

**results**  
[out] An array with the results of adding of clients. The size of the 'results' array must not be less than that of 'clients'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified clients have been added. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the clients have been added. Analyze the 'results' array for more details of the execution results. The result of adding of each client from the 'clients' array is added to 'results'. The index of a result corresponds to the index of a client in the source array.

### Note

A client can only be added to the database of the server, to which the application is connected.
