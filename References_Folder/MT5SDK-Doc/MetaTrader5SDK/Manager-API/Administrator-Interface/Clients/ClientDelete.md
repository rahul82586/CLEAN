[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / ClientDelete

[Previous](ClientUpdateBatchArray.md) | [Next](ClientDeleteBatch.md)

# IMTAdminAPI::ClientDelete

Delete a client from the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::ClientDelete(
       const UINT64   client_id  // identifier
       )

.NET
    
    
    MTRetCode  IMTAdminAPI.ClientDelete(
       ulong          client_id  // identifier
       )

Python
    
    
    AdminAPI.ClientDelete(
       int           client_id   # identifier
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

A client can only be deleted from the applications connected to the trade server, on which the client has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
