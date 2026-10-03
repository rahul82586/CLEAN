[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginRateMaintenance

[Previous](MarginRateInitial.md) | [Next](MarginLong.md)

# IMTConSymbol::MarginRateMaintenance

Get the maintenance margin rate for orders of the specified type.

C++
    
    
    double  IMTConSymbol::MarginRateMaintenance(
       const UINT  type      // Order type
       )

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginRateMaintenance(
       uint        type      // Order type
       )

Python (Manager API)
    
    
    MTConSymbol.MarginRateMaintenance(
       type        # Order type
       )
    
    
    MTConSymbol.MarginRateMaintenanceGet()

### Return Value

Margin rate for orders of the specified type.

### Parameters

**type**  
[in] Order type. Specified using theIMTConSymbol::EnMarginRateTypesenumeration.

### Note

The final size of the maintenance margin for orders of the specified type previously calculated according to the [symbol calculation type](CalcMode.md) and converted to [deposit currency](../../Groups/IMTConGroup/Currency.md) is multiplied by this rate.

# IMTConSymbol::MarginRateMaintenance

Set the maintenance margin rate for orders of the specified type.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginRateMaintenance(
       const UINT    type,       // Type of order
       const double  margin_rate // Margin rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.MarginRateMaintenance(
       uint          type,       // Type of order
       double        margin_rate // Margin rate
       )

Python (Manager API)
    
    
    MTConSymbol.MarginRateMaintenance(
       type,         # Order type
       margin_rate   # Margin rate
       )
    
    
    MTConSymbol.MarginRateMaintenanceSet()

### Parameters

**type**  
[in] Order type. Specified using theIMTConSymbol::EnMarginRateTypesenumeration.

**margin_rate**  
[in] Margin rate for orders of the specified type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The final size of the initial margin for orders of the specified type previously calculated according to the [symbol calculation type](CalcMode.md) and converted to [deposit currency](../../Groups/IMTConGroup/Currency.md) is multiplied by this rate.
