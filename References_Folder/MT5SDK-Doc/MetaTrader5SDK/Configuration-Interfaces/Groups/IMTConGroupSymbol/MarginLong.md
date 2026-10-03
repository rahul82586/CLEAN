[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginLong

[Previous](MarginRateCurrencyDefault.md) | [Next](MarginLongDefault.md)

# IMTConGroupSymbol::MarginLong

Get the group margin ratio for long positions and orders for a symbol.

C++
    
    
    double  IMTConGroupSymbol::MarginLong()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginLong()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginLong

### Return Value

The group margin ratio for long positions and orders for a symbol.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.

# IMTConGroupSymbol::MarginLong

Set the group margin ratio for long positions and orders for a symbol.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginLong(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginLong(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginLong

### Parameters

**margin**  
[in] The group margin ratio for long positions and orders for a symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.
