[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerSink](../IMTConManagerSink.md) / OnManagerSync

[Previous](OnManagerDelete.md) | [Next](HookManagerAdd.md)

# IMTConManagerSink::OnManagerSync

A handler of the event of synchronization of manager configurations.

C++
    
    
    virtual void  IMTConManagerSink::OnManagerSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConManagerSink.OnManagerSync()

### Note

This method is called by the API to notify that manager configurations have been synchronized.
