[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginShort

[Previous](MarginLongDefault.md) | [Next](MarginShortDefault.md)

# IMTConGroupSymbol::MarginShort

Get the group margin ratio for short positions and orders for a symbol.

C++
    
    
    double  IMTConGroupSymbol::MarginShort()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginShort()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginShort

### Return Value

The group margin ratio for short positions and orders for a symbol.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.

# IMTConGroupSymbol::MarginShort

Set the group margin ratio for short positions and orders for a symbol.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginShort(
       const double  margin      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginShort(
       double        margin      // Margin ratio
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginShort

### Parameters

**margin**  
[in] The group margin ratio for short positions and orders for a symbol.

### Return Value

An indication of successful completion is the MT_RET_OK response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is obsolete. The functionality of the method in the future is not guaranteed. Use [IMTConGroupSymbol::MarginRateInitial](MarginRateInitial.md) and [IMTConGroupSymbol::MarginRateMaintenance](MarginRateMaintenance.md) instead.
