[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientSink](../IMTClientSink.md) / OnClientDelete

[Previous](OnClientUpdate.md) | [Next](../IMTComment.md)

# IMTClientSink::OnClientDelete

Client deletion event handler.

C++
    
    
    virtual void  IMTClientSink::OnClientDelete(
       const IMTClient*  client    // A pointer to the client object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTClientSink.OnClientDelete(
       CIMTClient        client    // Client object
       )

### Parameters

**client**  
[in] A pointer to the deleted client object.

### Note

This method is called by the API to notify of a client deletion.
