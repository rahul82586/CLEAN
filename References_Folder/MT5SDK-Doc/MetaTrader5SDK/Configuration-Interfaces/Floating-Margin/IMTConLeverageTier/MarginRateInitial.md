[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageTier](../IMTConLeverageTier.md) / MarginRateInitial

[Previous](RangeTo.md) | [Next](MarginRateMaintenance.md)

# IMTConLeverageTier::MarginRateInitial

Get the initial margin rate for a level in a floating margin rule.

C++
    
    
    double  IMTConLeverageTier::MarginRateInitial()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConLeverageTier.MarginRateInitial()

Python (Manager API)
    
    
    MTConLeverageTier.MarginRateInitial

### Return Value

Margin rate.

### Note

The resulting initial margin calculated in accordance with the [instrument calculation type](../../Symbols/IMTConSymbol/CalcMode.md) is multiplied by this rate.

# IMTConLeverageTier::MarginRateInitial

Set the initial margin rate for a level in a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageTier::MarginRateInitial(
       const double  value       // Margin rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageTier.MarginRateInitial(
       double        value       // Margin rate
       )

Python (Manager API)
    
    
    MTConLeverageTier.MarginRateInitial

### Parameters

**margin_rate**  
[in] Margin rate.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The resulting initial margin calculated in accordance with the [instrument calculation type](../../Symbols/IMTConSymbol/CalcMode.md) is multiplied by this rate.
