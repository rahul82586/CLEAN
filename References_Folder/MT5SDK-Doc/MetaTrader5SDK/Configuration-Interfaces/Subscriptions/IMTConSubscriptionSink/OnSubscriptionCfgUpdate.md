[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionSink](../IMTConSubscriptionSink.md) / OnSubscriptionCfgUpdate

[Previous](OnSubscriptionCfgAdd.md) | [Next](OnSubscriptionCfgDelete.md)

# IMTConSubscriptionSink::OnSubscriptionCfgUpdate

Event handler for updating subscription configuration.

C++
    
    
    virtual void  IMTConSubscriptionSink::OnSubscriptionCfgUpdate(
       const IMTConSubscription*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSubscriptionSink.OnSubscriptionCfgUpdate(
       CIMTConSubscription         config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the updatedIMTConSubscriptionconfiguration object.

### Note

The API calls this method to notify of an update of a subscription configuration.
