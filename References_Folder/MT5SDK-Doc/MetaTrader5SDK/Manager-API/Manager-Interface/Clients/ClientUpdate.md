[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientUpdate

[Previous](ClientAddBatchArray.md) | [Next](ClientUpdateBatch.md)

# IMTManagerAPI::ClientUpdate

Update a client in the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::ClientUpdate(
       IMTClient*    client  // client object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ClientUpdate(
       CIMTClient    client  // client object
       )

Python
    
    
    ManagerAPI.ClientUpdate(
       MTClient      client  # client object
       )

### Parameters

**client**  
[in]Client object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client can only be updated from the applications connected to the trade server, on which the client has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
