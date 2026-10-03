[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginLong

[Previous](MarginRateMaintenance.md) | [Next](MarginShort.md)

# IMTConSymbol::MarginLong

Get the margin ratio for long positions and orders.

C++
    
    
    double  IMTConSymbol::MarginLong()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginLong()

Python (Manager API)
    
    
    MTConSymbol.MarginLong

### Return Value

The margin ratio for long positions and orders.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).

# IMTConSymbol::MarginLong

Set the margin ratio for long positions and orders.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginLong(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.MarginLong(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConSymbol.MarginLong

### Parameters

**margin**  
[in] The margin ratio for long positions and orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).
