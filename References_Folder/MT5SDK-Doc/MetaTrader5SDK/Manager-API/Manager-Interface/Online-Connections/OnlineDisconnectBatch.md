[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineDisconnectBatch

[Previous](OnlineDisconnect.md) | [Next](OnlineDisconnectBatchArray.md)

# IMTManagerAPI::OnlineDisconnectBatch

Forced disconnection of multiple clients from the server.

C++
    
    
    MTAPIRES  IMTManagerAPI::OnlineDisconnectBatch(
       IMTOnlineArray* online,        // Array of connection objects
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OnlineDisconnectBatch(
       CIMTOnlineArray online,        // Array of connection objects
       MTRetCode[]     results        // Array of results
       )

Python
    
    
    ManagerAPI.OnlineDisconnectBatch(
       online          # Array of connection objects
       )

### Parameters

**online**  
[in] A pointer to the array of connectionsIMTOnlineArray.

**results**  
[out] Array with connection drop results. The size of the 'results' array must not be less than that of the 'online' array.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all connections were dropped. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the connections were dropped. Analyze the 'results' array for more details concerning the execution results. The result of an attempt to drop each connection from the 'online' array is added to 'results'. The index of a result corresponds to the index of a position in the source array.

### Note

Connection drop can only be performed from the applications connected to the same server, to which the clients are connected. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
