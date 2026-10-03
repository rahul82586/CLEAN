[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadUpdate

[Previous](SpreadUnsubscribe.md) | [Next](SpreadUpdateBatch.md)

# IMTAdminAPI::SpreadUpdate

Add or update a spread configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::SpreadUpdate(
       IMTSpreadSymbol*  spread      // Spread configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SpreadUpdate(
       CIMTSpreadSymbol  spread      // Spread configuration object
       )

Python
    
    
    AdminAPI.SpreadUpdate(
       spread            # Spread configuration object
       )

### Parameters

**spread**  
[in] Spread configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the plugins that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
