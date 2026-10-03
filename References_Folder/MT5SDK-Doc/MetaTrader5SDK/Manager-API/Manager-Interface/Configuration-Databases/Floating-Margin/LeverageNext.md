[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageNext

[Previous](LeverageTotal.md) | [Next](LeverageGet.md)

# IMTManagerAPI::LeverageNext

Get a floating margin configuration by index.

C++
    
    
    MTAPIRES  IMTManagerAPI::LeverageNext(
       const UINT           pos,      // Configuration position
       IMTConLeverage*      config    // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.LeverageNext(
       uint                 pos,      // Configuration position
       CIMTConLeverage      config    // Configuration object
       )

Python
    
    
    ManagerAPI.LeverageNext(
       int                  pos       # Configuration positi
       )

### Parameters

**pos**  
[in] Configuration position starting from 0.

**config**  
[out] Configuration object. The 'config' object must be created in advance using theIMTManagerAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method copies the subscription configuration with a specified index to the 'config' object.
