[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Gateway Symbols](../Gateway-Symbols.md) / GatewaySymbolDelete

[Previous](GatewaySymbolAdd.md) | [Next](GatewaySymbolClear.md)

# IMTGatewayAPI::GatewaySymbolDelete

Deletes a symbol from the list available to the gateway (by name).

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewaySymbolDelete(
       LPCWSTR  name      // Symbol name
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewaySymbolDelete(
       string   name      // Symbol name
       )

### Parameters

**name**  
[in] Symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method can only be called from gateways.
