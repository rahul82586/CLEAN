[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineGet

[Previous](OnlineNext.md) | [Next](OnlineDisconnect.md)

# IMTServerAPI::OnlineGet

Get connection record by login.
    
    
    MTAPIRES  IMTServerAPI::OnlineGet(
       const UINT64     login,     // Client login
       IMTOnlineArray*  online     // Connection record array object
       )

### Parameters

**login**  
[in] The login of a client.

**online**  
[out] Connection record array object. The online object should be first created usingIMTServerAPI::OnlineCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a connection with the specified login to the online object.
