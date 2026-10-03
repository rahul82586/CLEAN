[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageRequest

[Previous](LeverageGet.md) | [Next](LeverageRequestArray.md)

# IMTManagerAPI::LeverageRequest

Request a floating margin configuration from the server by name.

C++
    
    
    MTAPIRES  IMTManagerAPI::LeverageRequest(
       LPCWSTR              name,     // Configuration name
       IMTConLeverage*      config    // Configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.LeverageRequest(
       string               name,     // Configuration name
       CIMTConLeverage      config    // Configuration object
       )

Python
    
    
    ManagerAPI.LeverageRequest(
       name                 # Configuration name
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConLeverage::Namevalue is used for the configuration name.

**config**  
[out] Configuration object. The 'config' object must be created in advance using theIMTManagerAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
