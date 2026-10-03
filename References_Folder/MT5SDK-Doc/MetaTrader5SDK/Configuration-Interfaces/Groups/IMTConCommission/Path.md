[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / Path

[Previous](Description.md) | [Next](Mode.md)

# IMTConCommission::Path

Get the path to a symbol or group of symbols that are subject to commission.

C++
    
    
    LPCWSTR  IMTConCommission::Path()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommission.Path()

Python (Manager API)
    
    
    MTConCommission.Path

### Return Value

If successful, it returns a pointer to a string with the path to a symbol or group of symbols. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConCommission](../IMTConCommission.md) object.

# IMTConCommission::Path

Specify the path to a symbol or group of symbols that are subject to commission.

C++
    
    
    MTAPIRES  IMTConCommission::Path(
       LPCWSTR  path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.Path(
       string   path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConCommission.Path

### Parameters

**path**  
[in] Path to a symbol or group of symbols in accordance with the hierarchy of symbols in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Path](../../Symbols/IMTConSymbol/Path.md) value is used as the path to the symbol.
