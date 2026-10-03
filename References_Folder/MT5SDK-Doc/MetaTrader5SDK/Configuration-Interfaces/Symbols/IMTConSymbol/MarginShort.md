[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginShort

[Previous](MarginLong.md) | [Next](MarginLimit.md)

# IMTConSymbol::MarginShort

Get the margin ratio for short positions and orders.

C++
    
    
    double  IMTConSymbol::MarginShort()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginShort()

Python (Manager API)
    
    
    MTConSymbol.MarginShort

### Return Value

The margin ratio for short positions and orders.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).

# IMTConSymbol::MarginShort

Margin for short positions and orders.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginShort(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)s
    
    
    MTRetCode  CIMTConSymbol.MarginShort(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConSymbol.MarginShort

### Parameters

**margin**  
[in] The margin ratio for short positions and orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).
