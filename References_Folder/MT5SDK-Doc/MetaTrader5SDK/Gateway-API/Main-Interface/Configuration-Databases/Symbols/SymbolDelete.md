[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolDelete

[Previous](SymbolUpdate.md) | [Next](SymbolTotal.md)

# IMTGatewayAPI::SymbolDelete

Delete a symbol configuration by the index or name.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SymbolDelete(
       LPCWSTR  name      // Symbol name
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SymbolDelete(
       string   name      // Symbol name
       )

### Parameters

**name**  
[in] Symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
