[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientSink](../IMTClientSink.md) / OnClientAdd

[Previous](../IMTClientSink.md) | [Next](OnClientUpdate.md)

# IMTClientSink::OnClientAdd

New client adding event handler.

C++
    
    
    virtual void  IMTClientSink::OnClientAdd(
       const IMTClient*  client    // A pointer to the client object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTClientSink.OnClientAdd(
       CIMTClient        client    // Client object
       )

### Parameters

**client**  
[in] A pointer to the client object.

### Note

This method is called by the API to notify that a new client has been added.
