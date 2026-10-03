[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageNext

[Previous](LeverageTotal.md) | [Next](LeverageGet.md)

# IMTAdminAPI::LeverageNext

Get a floating margin configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageNext(
       const UINT           pos,      // Configuration position
       IMTConLeverage*      config    // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageNext(
       uint                 pos,      // Configuration position
       CIMTConLeverage      config    // Configuration object
       )

Python
    
    
    AdminAPI.LeverageNext(
       int                  pos       # Configuration position
       )

### Parameters

**pos**  
[in] Configuration position starting from 0.

**config**  
[out] Configuration object. The config object must be previously created using theIMTAdminAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method copies the floating margin configuration with a specified index to the 'config' object.
