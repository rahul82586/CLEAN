[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolUpdate

[Previous](SymbolAddPreliminary.md) | [Next](SymbolDelete.md)

# IMTGatewayAPI::SymbolUpdate

Add or update a symbol configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SymbolUpdate(
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SymbolUpdate(
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

The method can only be called after receiving the [IMTGatewaySink::OnServerSynchronized](../../../Event-Interface/OnServerSynchronized.md) notification for the main trade server. Otherwise, the call will return the [MT_RET_OK_NONE](../../../../Return-Codes/Successful-completion.md) error.
