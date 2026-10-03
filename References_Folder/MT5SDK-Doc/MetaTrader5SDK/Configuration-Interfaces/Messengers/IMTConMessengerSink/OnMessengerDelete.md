[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerSink](../IMTConMessengerSink.md) / OnMessengerDelete

[Previous](OnMessengerUpdate.md) | [Next](OnMessengerSync.md)

# IMTConMessengerSink:OnMessengerDelete

A handler of the messenger configuration deletion event.

C++
    
    
    virtual void  IMTConMessengerSink::OnMessengerDelete(
       const IMTConMessenger*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConMessengerSink.OnMessengerDelete(
       CIMTConMessenger         config  // Configuration object
       )

### Parameters

**config**  
A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify of deletion of a messenger configuration.
