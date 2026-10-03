[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageSink](../IMTConLeverageSink.md) / OnLeverageUpdate

[Previous](OnLeverageAdd.md) | [Next](OnLeverageDelete.md)

# IMTConLeverageSink::OnLeverageUpdate

Handler for the event of updating a floating margin configuration.

C++
    
    
    virtual void  IMTConLeverageSink::OnLeverageUpdate(
       const IMTConSubscription*   config  // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConLeverageSink.OnLeverageUpdate(
       CIMTConSubscription         config  // Configuration object
       )

### Parameters

**config**  
[in] Pointer to the updated configuration objectIMTConLeverage.

### Note

The API calls this method to notify that a floating margin configuration has been updated.
