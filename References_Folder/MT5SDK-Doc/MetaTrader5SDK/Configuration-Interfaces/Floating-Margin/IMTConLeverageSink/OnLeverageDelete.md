[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageSink](../IMTConLeverageSink.md) / OnLeverageDelete

[Previous](OnLeverageUpdate.md) | [Next](OnLeverageSync.md)

# IMTConLeverageSink:OnLeverageDelete

Handler for the event of deleting a floating margin configuration.

C++
    
    
    virtual void  IMTConLeverageSink::OnLeverageDelete(
       const IMTConSubscription*   config  // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConLeverageSink.OnLeverageDelete(
       CIMTConSubscription         config  // Configuration object
       )

### Parameters

**config**  
Pointer to the object of the deleted configurationIMTConLeverage.

### Note

The API calls this method to notify that a floating margin configuration has been deleted.
