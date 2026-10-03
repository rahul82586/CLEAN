[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionSink](../IMTConSubscriptionSink.md) / OnSubscriptionCfgDelete

[Previous](OnSubscriptionCfgUpdate.md) | [Next](OnSubscriptionCfgSync.md)

# IMTConSubscriptionSink:OnSubscriptionCfgDelete

Event handler for deleting subscription configuration.

C++
    
    
    virtual void  IMTConSubscriptionSink::OnSubscriptionCfgDelete(
       const IMTConSubscription*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSubscriptionSink.OnSubscriptionCfgDelete(
       CIMTConSubscription         config  // Configuration object
       )

### Parameters

**config**  
A pointer to the deletedIMTConSubscriptionconfiguration object.

### Note

This method is called by the API to notify of deletion of a subscription configuration.
