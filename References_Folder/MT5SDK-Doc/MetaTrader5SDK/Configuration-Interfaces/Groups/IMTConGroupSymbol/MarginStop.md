[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginStop

[Previous](MarginLimitDefault.md) | [Next](MarginStopDefault.md)

# IMTConGroupSymbol::MarginStop

Get the group margin ratio of stop orders for a symbol.

C++
    
    
    double  IMTConGroupSymbol::MarginStop()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginStop()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginStop

### Return Value

The group margin ratio of stop orders for a symbol.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.

# IMTConGroupSymbol::MarginStop

Set the group margin ratio of stop orders for a symbol.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginStop(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginStop(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginStop

### Parameters

**margin**  
[in] The group margin ratio of stop orders for a symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.
