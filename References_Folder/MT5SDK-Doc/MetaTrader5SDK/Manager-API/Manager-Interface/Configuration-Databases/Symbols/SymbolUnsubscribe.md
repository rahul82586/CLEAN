[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolUnsubscribe

[Previous](SymbolSubscribe.md) | [Next](SymbolUpdate.md)

# IMTManagerAPI::SymbolUnsubscribe

Unsubscribe from events associated with the configuration of symbols.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolUnsubscribe(
       IMTConSymbolSink*  sink      // A pointer to the IMTConSymbolSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolUnsubscribe(
       CIMTConSymbolSink  sink      // CIMTConSymbolSink object
       )

Python
    
    
    ManagerAPI.SymbolUnsubscribe(
       sink               // IMTConSymbolSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implementsIMTConSymbolSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is pared to [IMTManagerAPI::SymbolSubscribe](SymbolSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
