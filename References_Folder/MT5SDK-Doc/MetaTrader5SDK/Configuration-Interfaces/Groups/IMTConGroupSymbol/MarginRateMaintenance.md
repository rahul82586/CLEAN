[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginRateMaintenance

[Previous](MarginRateInitialDefault.md) | [Next](MarginRateMaintenanceDefault.md)

# IMTConGroupSymbol::MarginRateMaintenance

Get the maintenance margin rate for orders of the specified type for the given group.

C++
    
    
    double  IMTConGroupSymbol::MarginRateMaintenance(
       const UINT  type      // Order type
       )

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginRateMaintenance(
       uint        type      // Order type
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateMaintenance(
       type        # Order type
       )
    
    
    MTConGroupSymbol.MarginRateMaintenanceGet()

### Return Value

Margin rate for orders of the specified type.

### Parameters

**type**  
[in] Order type. Specified using theIMTConSymbol::EnMarginRateTypesenumeration.

### Note

The final size of the maintenance margin for orders of the specified type previously calculated according to the [symbol calculation type](../../Symbols/IMTConSymbol/CalcMode.md) and converted to [deposit currency](../IMTConGroup/Currency.md) is multiplied by this rate.

# IMTConGroupSymbol::MarginRateMaintenance

Set the maintenance margin rate for orders of the specified type for the given group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginRateMaintenance(
       const UINT    type,       // Type of order
       const double  margin_rate // Margin rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginRateMaintenance(
       uint          type,       // Type of order
       double        margin_rate // Margin rate
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateMaintenance(
       type,         # Order type
       margin_rate   # Margin rate
       )
    
    
    MTConGroupSymbol.MarginRateMaintenanceSet()

### Parameters

**type**  
[in] Order type. Specified using theIMTConSymbol::EnMarginRateTypesenumeration.

**margin_rate**  
[in] Margin rate for orders of the specified type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The final size of the maintenance margin for orders of the specified type previously calculated according to the [symbol calculation type](../../Symbols/IMTConSymbol/CalcMode.md) and converted to [deposit currency](../IMTConGroup/Currency.md) is multiplied by this rate.
