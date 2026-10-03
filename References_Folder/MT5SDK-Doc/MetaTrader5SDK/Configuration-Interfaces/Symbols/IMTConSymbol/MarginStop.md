[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginStop

[Previous](MarginLimit.md) | [Next](MarginStopLimit.md)

# IMTConSymbol::MarginStop

Get the margin ratio for stop orders.

C++
    
    
    double  IMTConSymbol::MarginStop()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginStop()

Python (Manager API)
    
    
    MTConSymbol.MarginStop

### Return Value

The margin ratio for stop orders.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).

# IMTConSymbol::MarginStop

Set the margin ratio for stop orders.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginStop(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.MarginStop(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConSymbol.MarginStop

### Parameters

**margin**  
[in] The margin ratio for stop orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Instead of it one should use [IMTConSymbol::MarginRateInitial](MarginRateInitial.md) or [IMTConSymbol::MarginRateMaintenance](MarginRateMaintenance.md).
