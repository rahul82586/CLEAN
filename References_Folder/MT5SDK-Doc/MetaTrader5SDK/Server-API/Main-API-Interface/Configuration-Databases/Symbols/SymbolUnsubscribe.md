[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolUnsubscribe

[Previous](SymbolSubscribe.md) | [Next](SymbolAdd.md)

# IMTServerAPI::SymbolUnsubscribe

Unsubscribe from events and hooks associated with the configuration of symbols.
    
    
    MTAPIRES  IMTServerAPI::SymbolUnsubscribe(
       IMTConSymbolSink*  sink      // A pointer to the IMTConSymbolSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implementsIMTConSymbolSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::SymbolSubscribe](SymbolSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
