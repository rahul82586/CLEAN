[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientSink](../IMTClientSink.md) / OnClientUpdate

[Previous](OnClientAdd.md) | [Next](OnClientDelete.md)

# IMTClientSink::OnClientUpdate

Client update event handler.

C++
    
    
    virtual void  IMTClientSink::OnClientUpdate(
       const IMTClient*  client    // A pointer to the client
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTClientSink.OnClientUpdate(
       CIMTClient        client    // Client object
       )

### Parameters

**client**  
[in] A pointer to the client object.

### Note

This method is called by the API to notify of a client update.
