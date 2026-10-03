[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageGet

[Previous](LeverageNext.md) | [Next](LeverageRequest.md)

# IMTManagerAPI::LeverageGet

Get a floating margin configuration by name.

C++
    
    
    MTAPIRES  IMTManagerAPI::LeverageGet(
       LPCWSTR              name,     // Configuration name
       IMTConLeverage*      config    // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.LeverageGet(
       string               name,     // Configuration name
       CIMTConLeverage      config    // Configuration object
       )

Python
    
    
    ManagerAPI.LeverageGet(
       str                  name      # Configuration name
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConLeverage::Namevalue is used for the configuration name.

**config**  
[out] Configuration object. The 'config' object must be created in advance using theIMTManagerAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.
