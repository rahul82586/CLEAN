[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadUnsubscribe

[Previous](SpreadSubscribe.md) | [Next](SpreadTotal.md)

# IMTManagerAPI::SpreadUnsubscribe

Unsubscribe from events and hooks associated with spread configuration.

C++
    
    
    MTAPIRES  IMTManagerAPI::SpreadUnsubscribe(
       IMTConSpreadSink*  sink      // pointer to IMTConSpreadSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SpreadUnsubscribe(
       CIMTConSpreadSink  sink      // CIMTConSpreadSink object
       )

Python
    
    
    ManagerAPI.SpreadUnsubscribe(
       sink               // IMTConSpreadSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implementsIMTConSymbolSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::SpreadSubscribe](SpreadSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
