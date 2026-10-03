[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginStopLimit

[Previous](MarginStop.md) | [Next](MarginHedged.md)

# IMTConSymbol::MarginStopLimit

Get the margin ratio for stop-limit orders.

C++
    
    
    double  IMTConSymbol::MarginStopLimit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginStopLimit()

Python (Manager API)
    
    
    MTConSymbol.MarginStopLimit

### Return Value

Margin ratio for stop-limit orders.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).

# IMTConSymbol::MarginStopLimit

Set the margin ratio for stop-limit orders.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginStopLimit(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.MarginStopLimit(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConSymbol.MarginStopLimit

### Parameters

**margin**  
[in] Margin ratio for stop-limit orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).
