[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageSink](../IMTConLeverageSink.md) / OnLeverageSync

[Previous](OnLeverageDelete.md) | [Next](HookLeverageAdd.md)

# IMTConLeverageSink::OnLeverageSync

Handler for the event of synchronizing a floating margin configuration.

C++
    
    
    virtual void  IMTConLeverageSink::OnLeverageSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConLeverageSink.OnLeverageSync()

### Note

The API calls this method to notify that a floating margin configuration has been synchronized.
