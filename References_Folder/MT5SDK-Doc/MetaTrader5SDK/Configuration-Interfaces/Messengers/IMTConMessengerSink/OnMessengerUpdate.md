[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerSink](../IMTConMessengerSink.md) / OnMessengerUpdate

[Previous](OnMessengerAdd.md) | [Next](OnMessengerDelete.md)

# IMTConMessengerSink::OnMessengerUpdate

A handler of the messenger configuration update event.

C++
    
    
    virtual void  IMTConMessengerSink::OnMessengerUpdate(
       const IMTConMessenger*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConMessengerSink.OnMessengerUpdate(
       CIMTConMessenger         config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the updated configuration object.

### Note

This method is called by the API to notify that a messenger configuration has been updated.
