[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Interface of Manager API Events](../Interface-of-Events.md) / Interface of Events OnDisconnect

[Previous](Interface-of-Events-OnConnect.md) | [Next](Interface-of-Events-OnTradeAccountSet.md)

# IMTManagerSink::OnDisconnect

A handler of the event of an application's disconnection from the server.

C++
    
    
    virtual void  IMTManagerSink::OnDisconnect()

.NET
    
    
    virtual void  CIMTManagerSink.OnDisconnect()

### Note

The method is called when the connection of the manager or administrator interface with the server is lost..
