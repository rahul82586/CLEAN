[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginLimit

[Previous](MarginShort.md) | [Next](MarginStop.md)

# IMTConSymbol::MarginLimit

Get the margin ratio for limit orders.

C++
    
    
    double  IMTConSymbol::MarginLimit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginLimit()

Python (Manager API)
    
    
    MTConSymbol.MarginLimit

### Return Value

Margin ratio for limit orders.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).

# IMTConSymbol::MarginLimit

Set the margin ratio for limit orders.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginLimit(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.MarginLimit(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConSymbol.MarginLimit

### Parameters

**margin**  
[in] Margin ratio for limit orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).
