[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadNext

[Previous](SpreadTotal.md) | [Next](../Plugins.md)

# IMTManagerAPI::SpreadNext

Receiving a spread configuration by the index.

C++
    
    
    MTAPIRES  IMTManagerAPI::SpreadNext(
       const UINT     pos,        // Position of the configuration
       IMTConSymbol*  spread      // Spread configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SpreadNext(
       uint           pos,        // Position of the configuration
       CIMTConSymbol  spread      // Spread configuration object
       )

Python
    
    
    ManagerAPI.SpreadNext(
       pos            # configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**spread**  
[out] Spread configuration object. The spread object must be first created usingIMTManagerAPI::SpreadCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a spread with a specified index to spread object.
