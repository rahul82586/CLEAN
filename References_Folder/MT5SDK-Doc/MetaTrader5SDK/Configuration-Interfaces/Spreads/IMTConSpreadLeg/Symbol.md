[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / Symbol

[Previous](Mode.md) | [Next](TimeFrom.md)

# IMTConSpreadLeg::Symbol

Getting a trade symbol specified for a spread leg.

C++
    
    
    LPCWSTR  IMTConSpreadLeg::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSpreadLeg.Symbol()

Python (Manager API)
    
    
    MTConSpreadLeg.Symbol

### Return Value

Spread leg symbol.

# IMTConSpreadLeg::Symbol

Setting a spread leg symbol.

C++
    
    
    MTAPIRES  IMTConSpreadLeg::Symbol(
       LPCWSTR  symbol      // symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpreadLeg.Symbol(
       string   symbol      // symbol
       )

Python (Manager API)
    
    
    MTConSpreadLeg.Symbol

### Parameters

**open**  
[in] Spread leg symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

According to the symbols specification type ([IMTConSpreadLeg::Mode](Mode.md)) set for a spread leg, the name of a specific symbol ([IMTConSymbol::Symbol](../../Symbols/IMTConSymbol/Symbol.md)) or a basic asset ([IMTConSymbol::Basis](../../Symbols/IMTConSymbol/Basis.md)) is specified in the method.
