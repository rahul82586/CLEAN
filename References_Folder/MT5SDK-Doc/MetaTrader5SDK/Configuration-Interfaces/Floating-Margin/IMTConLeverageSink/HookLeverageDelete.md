[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageSink](../IMTConLeverageSink.md) / HookLeverageDelete

[Previous](HookLeverageUpdate.md) | [Next](../../Managers.md)

# IMTConLeverageSink::HookLeverageDelete

Hook for deleting a floating margin configuration.
    
    
    virtual MTAPIRES  IMTConLeverageSink::HookLeverageDelete(
       const UINT64     login   // Manager login
       IMTConLeverage*  config  // Pointer to the configuration object
       )

### Parameters

**login**  
[in] Login of the manager who deletes the configuration. Corresponds toIMTConManager::Login.

**config**  
[in] Pointer to the object of the deleted configurationIMTConLeverage.

### Return Value

If there are no handlers for this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called just before making changes to the configuration database. The main purpose of this hook is prevent unwanted deletion of records.
