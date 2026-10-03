[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolAdd

[Previous](SymbolUnsubscribe.md) | [Next](SymbolDelete.md)

# IMTServerAPI::SymbolAdd

Add or update a symbol configuration.
    
    
    MTAPIRES  IMTServerAPI::SymbolAdd(
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the name of the symbol [IMTConSymbol::Symbol()](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConSymbolSink::OnSymbolUpdate](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSink/OnSymbolUpdate.md) notification method is not called.
