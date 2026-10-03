[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageGet

[Previous](LeverageNext.md) | [Next](../Managers.md)

# IMTAdminAPI::LeverageGet

Get a floating margin configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageGet(
       LPCWSTR              name,     // Configuration name
       IMTConLeverage*      config    // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageGet(
       string               name,     // Configuration name
       CIMTConLeverage      config    // Configuration object
       )

Python
    
    
    AdminAPI.LeverageGet(
       str                  name      # Configuration name
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConLeverage::Namevalue is used for the configuration name.

**config**  
[out] Configuration object. The config object must be previously created using theIMTAdminAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.
