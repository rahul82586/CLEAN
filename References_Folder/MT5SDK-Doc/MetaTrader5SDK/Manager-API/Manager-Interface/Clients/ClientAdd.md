[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientAdd

[Previous](ClientCreateArray.md) | [Next](ClientAddBatch.md)

# IMTManagerAPI::ClientAdd

Add a client to the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::ClientAdd(
       IMTClient*    client   // client object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ClientAdd(
       CIMTClient    client   // client object
       )

Python
    
    
    ManagerAPI.ClientAdd(
       MTClient      client   # client object
       )

### Parameters

**client**  
[in]Client object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred which corresponds to the response code.

### Note

A client can only be added to the database of the server, to which the application is connected.
