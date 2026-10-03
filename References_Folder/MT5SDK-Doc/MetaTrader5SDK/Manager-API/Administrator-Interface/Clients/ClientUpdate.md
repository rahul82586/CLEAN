[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / ClientUpdate

[Previous](ClientAddBatchArray.md) | [Next](ClientUpdateBatch.md)

# IMTAdminAPI::ClientUpdate

Update a client in the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::ClientUpdate(
       IMTClient*    client  // client object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ClientUpdate(
       CIMTClient    client  // client object
       )

Python
    
    
    AdminAPI.ClientUpdate(
       MTClient      client  # client object
       )

### Parameters

**client**  
[in]Client object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client can only be updated from the applications connected to the trade server, on which the client has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.

All required fields in the 'client' object must be filled, not only the ones that need to be changed. It is recommended that you first receive a client object from the server, change the required fields in it, and then send the changed object back to the server.

During update, a client record is checked for integrity. The [IMTClient::PersonName](../../../Database-Interfaces/Clients/IMTClient/PersonName.md) field must be filled in the record.
