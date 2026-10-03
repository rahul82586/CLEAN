[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginStopLimit

[Previous](MarginStopDefault.md) | [Next](MarginStopLimitDefault.md)

# IMTConGroupSymbol::MarginStopLimit

Get the group margin ratio for stop-limit orders for a symbol.

C++
    
    
    double  IMTConGroupSymbol::MarginStopLimit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginStopLimit()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginStopLimit

### Return Value

The group margin ratio for stop-limit orders for a symbol.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.

# IMTConGroupSymbol::MarginStopLimit

Set the group margin ratio for stop-limit orders for a symbol.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginStopLimit(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginStopLimit(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginStopLimit

### Parameters

**margin**  
[in] The group margin ratio for stop-limit orders for a symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.
