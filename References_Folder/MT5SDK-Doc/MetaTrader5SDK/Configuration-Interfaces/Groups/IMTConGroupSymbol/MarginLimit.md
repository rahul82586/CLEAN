[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginLimit

[Previous](MarginShortDefault.md) | [Next](MarginLimitDefault.md)

# IMTConGroupSymbol::MarginLimit

Get the group margin ratio of limit orders for a symbol.

C++
    
    
    double  IMTConGroupSymbol::MarginLimit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginLimit()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginLimit

### Return Value

The group margin ratio of limit orders for a symbol.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.

# IMTConGroupSymbol::MarginLimit

Set the group margin ratio of limit orders for a symbol.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginLimit(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginLimit(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginLimit

### Parameters

**margin**  
[in] The group margin ratio of limit orders for a symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.
