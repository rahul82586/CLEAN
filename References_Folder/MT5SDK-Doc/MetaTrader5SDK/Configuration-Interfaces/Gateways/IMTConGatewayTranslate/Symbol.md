[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayTranslate](../IMTConGatewayTranslate.md) / Symbol

[Previous](Source.md) | [Next](BidMarkup.md)

# IMTConGatewayTranslate::Symbol

Get the target symbol name in the trading platform.

C++
    
    
    LPCWSTR  IMTConGatewayTranslate::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayTranslate.Symbol()

Python (Manager API)
    
    
    MTConGatewayTranslate.Symbol

### Return Value

If successful, it returns a pointer to a string with the symbol name if the trading platform. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayTranslate](../IMTConGatewayTranslate.md) object.

# IMTConGatewayTranslate::Symbol

Set the target symbol name in the trading platform.

C++
    
    
    MTAPIRES  IMTConGatewayTranslate::Symbol(
       LPCWSTR  symbol      // The name of a symbol in the trading platform
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayTranslate.Symbol(
       string   symbol      // The name of a symbol in the trading platform
       )

Python (Manager API)
    
    
    MTConGatewayTranslate.Symbol

### Parameters

**symbol**  
[in] The name of a symbol in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Symbol](../../Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
