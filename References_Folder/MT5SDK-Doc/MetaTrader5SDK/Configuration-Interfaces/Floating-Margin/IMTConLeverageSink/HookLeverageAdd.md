[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageSink](../IMTConLeverageSink.md) / HookLeverageAdd

[Previous](OnLeverageSync.md) | [Next](HookLeverageUpdate.md)

# IMTConLeverageSink::HookLeverageAdd

Hook for adding a new floating margin configuration.
    
    
    virtual MTAPIRES  IMTConLeverageSink::HookLeverageAdd(
       const UINT64     login   // Manager login
       IMTConLeverage*  config  // Pointer to the configuration object
       )

### Parameters

**login**  
[in] Login of the manager who adds the configuration. Corresponds toIMTConManager::Login.

**config**  
[in] Pointer to the object of the added configurationIMTConLeverage.

### Return Value

If there are no handlers for this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called just before adding the configuration to the database. The main purpose of this hook is to modify the added record and, if necessary, to prevent the addition of unwanted records.
