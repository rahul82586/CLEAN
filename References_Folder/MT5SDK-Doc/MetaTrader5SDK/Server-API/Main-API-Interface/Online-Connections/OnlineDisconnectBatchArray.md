[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineDisconnectBatchArray

[Previous](OnlineDisconnectBatch.md) | [Next](../Certificates.md)

# IMTServerAPI::OnlineDisconnectBatchArray

Forced disconnection of multiple clients from the server.
    
    
    MTAPIRES  IMTServerAPI::OnlineDisconnectBatchArray(
       IMTOnline**     online,        // Array of connection objects
       const UINT      online_total,  // Number of objects in the array
       MTAPIRES*       results        // Array of results
       )

### Parameters

**online**  
[in] A pointer to the array of connection objectsIMTOnline.

**online_total**  
[in] Number of object in the 'online' array.

**results**  
[out] Array with connection drop results. The size of the 'results' array must not be less than that of the 'online' array.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all connections were dropped. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the connections were dropped. Analyze the 'results' array for more details concerning the execution results. The result of an attempt to drop each connection from the 'online' array is added to 'results'. The index of a result corresponds to the index of a position in the source array.

### Note

Connection drop can only be performed from the applications connected to the same server, to which the clients are connected. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
