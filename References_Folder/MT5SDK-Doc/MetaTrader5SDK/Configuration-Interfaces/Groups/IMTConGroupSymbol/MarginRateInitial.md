[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginRateInitial

[Previous](MarginMaintenanceDefault.md) | [Next](MarginRateInitialDefault.md)

# IMTConGroupSymbol::MarginRateInitial

Get the initial margin rate for orders of the specified type for the given group.

C++
    
    
    double  IMTConGroupSymbol::MarginRateInitial(
       const UINT  type      // Order type
       )

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginRateInitial(
       uint        type      // Order type
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateInitial(
       type        # Order type
       )
    
    
    MTConGroupSymbol.MarginRateInitialGet()

### Return Value

Margin rate for orders of the specified type.

### Parameters

**type**  
[in] Order type. Specified using theIMTConSymbol::EnMarginRateTypesenumeration.

### Note

The final size of the initial margin for orders of the specified type previously calculated according to the [symbol calculation type](../../Symbols/IMTConSymbol/CalcMode.md) and converted to [deposit currency](../IMTConGroup/Currency.md) is multiplied by this rate.

# IMTConGroupSymbol::MarginRateInitial

Set the initial margin rate for orders of the specified type for the given group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginRateInitial(
       const UINT    type,       // Type of order
       const double  margin_rate // Margin rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginRateInitial(
       uint          type,       // Type of order
       double        margin_rate // Margin rate
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateInitial(
       type,         # Order type
       margin_rate   # Margin rate
       )
    
    
    MTConGroupSymbol.MarginRateInitialSet(
       rate_dict     # Margin rate
       )

### Parameters

**type**  
[in] Order type. Specified using theIMTConSymbol::EnMarginRateTypesenumeration.

**margin_rate**  
[in] Margin rate for orders of the specified type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The final size of the initial margin for orders of the specified type previously calculated according to the [symbol calculation type](../../Symbols/IMTConSymbol/CalcMode.md) and converted to [deposit currency](../IMTConGroup/Currency.md) is multiplied by this rate.
