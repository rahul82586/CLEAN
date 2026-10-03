[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Spread

[Previous](ExpirFlags.md) | [Next](SpreadBalance.md)

# IMTConSymbol::Spread

Get the size of the symbol spread.

C++
    
    
    UINT  IMTConSymbol::Spread()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.Spread()

Python (Manager API)
    
    
    MTConSymbol.Spread

### Return Value

Symbol spread size. The 0 value means that the spread is floating.

# IMTConSymbol::Spread

Set the size of the symbol spread.

C++
    
    
    MTAPIRES  IMTConSymbol::Spread(
       const UINT  spread      // Spread size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Spread(
       uint        spread      // Spread size
       )

Python (Manager API)
    
    
    MTConSymbol.Spread

### Parameters

**spread**  
[in] The symbol spread size. The 0 value means that the spread is floating.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
