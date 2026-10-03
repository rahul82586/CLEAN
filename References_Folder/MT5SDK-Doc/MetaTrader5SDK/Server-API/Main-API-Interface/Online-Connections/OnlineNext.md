[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineNext

[Previous](OnlineTotal.md) | [Next](OnlineGet.md)

# IMTServerAPI::OnlineNext

Get connection record by index.
    
    
    MTAPIRES  IMTServerAPI::OnlineNext(
       const UINT     pos,        // Connection record position
       IMTOnline*     online      // Connection record object
       )

### Parameters

**pos**  
[in] Position of the record, starting with 0.

**online**  
[out] Connection record object. The online object should be first created usingIMTServerAPI::OnlineCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a connection records with the specified index to the online object.
