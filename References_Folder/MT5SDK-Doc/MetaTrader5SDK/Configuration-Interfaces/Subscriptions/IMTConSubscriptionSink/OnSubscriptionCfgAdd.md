[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionSink](../IMTConSubscriptionSink.md) / OnSubscriptionCfgAdd

[Previous](../IMTConSubscriptionSink.md) | [Next](OnSubscriptionCfgUpdate.md)

# IMTConSubscriptionSink::OnSubscriptionCfgAdd

Event handler for adding a new subscription configuration.

C++
    
    
    virtual void  IMTConSubscriptionSink::OnSubscriptionCfgAdd(
       const IMTConSubscription*  config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSubscriptionSink.OnSubscriptionCfgAdd(
       CIMTConSubscription        config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the addedIMTConSubscriptionconfiguration.

### Note

The API calls this method to notify that a new subscription configuration has been added.
