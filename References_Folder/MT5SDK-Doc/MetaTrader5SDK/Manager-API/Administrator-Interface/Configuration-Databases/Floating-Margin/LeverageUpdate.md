[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageUpdate

[Previous](LeverageUnsubscribe.md) | [Next](LeverageUpdateBatch.md)

# IMTAdminAPI::LeverageUpdate

Add or update a floating margin configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageUpdate(
       IMTConLeverage*  config  // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageUpdate(
       CIMTConLeverage  config  // Configuration object
       )

Python
    
    
    AdminAPI.LeverageUpdate(
       MTConLeverage    config  // Configuration object
       )

### Parameters

**config**  
[in] Floating margin configuration objectIMTConLeverage.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

When the method is called, the system checks whether the record being added already exists. If the record is found, the system updates it. Otherwise, a new entry is added. The comparison is based on the configuration name field [IMTConLeverage::Name](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverage/Name.md). If an attempt is made to add a completely identical record, no changes are made, and consequently, the notification method [IMTConLeverageSink::OnLeverageUpdate](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageSink/OnLeverageUpdate.md) is not called.
