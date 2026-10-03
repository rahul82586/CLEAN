[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageTier](../IMTConLeverageTier.md) / MarginRateMaintenance

[Previous](MarginRateInitial.md) | [Next](../IMTConLeverageSink.md)

# IMTConLeverageTier::MarginRateMaintenance

Get the maintenance margin rate for a level in a floating margin rule.

C++
    
    
    double  IMTConLeverageTier::MarginRateMaintenance()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConLeverageTier.MarginRateMaintenance()

Python (Manager API)
    
    
    MTConLeverageTier.MarginRateMaintenance

### Return Value

Margin rate.

### Note

The resulting maintenance margin calculated in accordance with the [instrument calculation type](../../Symbols/IMTConSymbol/CalcMode.md) is multiplied by this rate.

# IMTConLeverageTier::MarginRateMaintenance

Set the maintenance margin rate for a level in a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageTier::MarginRateMaintenance(
       const double  value       // Margin rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageTier.MarginRateMaintenance(
       double        value       // Margin rate
       )

Python (Manager API)
    
    
    MTConLeverageTier.MarginRateMaintenance

### Parameters

**margin_rate**  
[in] Margin rate.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The resulting maintenance margin calculated in accordance with the [instrument calculation type](../../Symbols/IMTConSymbol/CalcMode.md) is multiplied by this rate.
