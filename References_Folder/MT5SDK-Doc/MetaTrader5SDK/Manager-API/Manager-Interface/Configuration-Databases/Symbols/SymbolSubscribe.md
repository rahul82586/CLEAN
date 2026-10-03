[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolSubscribe

[Previous](SymbolSessionCreate.md) | [Next](SymbolUnsubscribe.md)

# IMTManagerAPI::SymbolSubscribe

Subscribe to events associated with the configuration of symbols.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolSubscribe(
       IMTConSymbolSink*  sink      // A pointer to the IMTConSymbolSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolSubscribe(
       CIMTConSymbolSink  sink      // CIMTConSymbolSink object
       )

Python
    
    
    ManagerAPI.SymbolSubscribe(
       sink               # IMTConSymbolSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implementsIMTConSymbolSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConSymbolSink](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
