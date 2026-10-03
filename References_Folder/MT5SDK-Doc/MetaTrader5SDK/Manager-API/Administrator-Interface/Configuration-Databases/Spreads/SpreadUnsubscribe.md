[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadUnsubscribe

[Previous](SpreadSubscribe.md) | [Next](SpreadUpdate.md)

# IMTAdminAPI::SpreadUnsubscribe

Unsubscribe from events and hooks associated with spread configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::SpreadUnsubscribe(
       IMTConSpreadSink*  sink      // pointer to IMTConSpreadSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SpreadUnsubscribe(
       CIMTConSpreadSink  sink      // CIMTConSpreadSink object
       )

Python
    
    
    AdminAPI.SpreadSubscribe(
       sink               # IMTConSpreadSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implementsIMTConSymbolSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::SpreadSubscribe](SpreadSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
