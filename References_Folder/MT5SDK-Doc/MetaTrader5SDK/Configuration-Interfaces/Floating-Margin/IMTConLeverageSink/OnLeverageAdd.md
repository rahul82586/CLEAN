[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageSink](../IMTConLeverageSink.md) / OnLeverageAdd

[Previous](../IMTConLeverageSink.md) | [Next](OnLeverageUpdate.md)

# IMTConLeverageSink::OnLeverageAdd

Handler for the event of adding a new floating margin configuration.

C++
    
    
    virtual void  IMTConLeverageSink::OnLeverageAdd(
       const IMTConLeverage*  config  // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConLeverageSink.OnLeverageAdd(
       CIMTConLeverage        config  // Configuration object
       )

### Parameters

**config**  
[in] Pointer to the object of the added configurationIMTConLeverage.

### Note

The API calls this method to notify that a new floating margin configuration has been added.
