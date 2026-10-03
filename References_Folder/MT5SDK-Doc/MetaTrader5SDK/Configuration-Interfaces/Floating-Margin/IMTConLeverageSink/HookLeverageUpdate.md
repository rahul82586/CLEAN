[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageSink](../IMTConLeverageSink.md) / HookLeverageUpdate

[Previous](HookLeverageAdd.md) | [Next](HookLeverageDelete.md)

# IMTConLeverageSink::HookLeverageUpdate

Hook for editing a floating margin configuration.
    
    
    virtual MTAPIRES  IMTConLeverageSink::HookLeverageUpdate(
       const UINT64     login   // Manager login
       IMTConLeverage*  config  // Pointer to the configuration object
       )

### Parameters

**login**  
[in] Login of the manager who modifies the configuration. Corresponds toIMTConManager::Login.

**config**  
[in] Pointer to the object of the configuration being updatedIMTConLeverage.

### Return Value

If there are no handlers for this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called just before making changes to the configuration database. The main purpose of this hook is to modify the record being updated and, if necessary, to prevent unwanted modifications.
