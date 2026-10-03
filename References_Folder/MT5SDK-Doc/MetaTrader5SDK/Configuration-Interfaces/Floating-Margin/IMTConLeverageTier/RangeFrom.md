[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageTier](../IMTConLeverageTier.md) / RangeFrom

[Previous](Clear.md) | [Next](RangeTo.md)

# IMTConLeverageTier::RangeFrom

Get the minimum range value for a level in a floating margin rule.

C++
    
    
    double  IMTConLeverageTier::RangeFrom()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConLeverageTier.RangeFrom()

Python (Manager API)
    
    
    MTConLeverageTier.RangeFrom

### Return Value

The minimum range value for a level in a floating margin rule. The range type is determined by the [IMTConLeverageRule::RangeMode](../IMTConLeverageRule/RangeMode.md) method.

# IMTConLeverageTier::RangeFrom

Set the minimum range value for a level in a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageTier::RangeFrom(
       const double  value      // Minimum value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageTier.RangeFrom(
       double        value      // Minimum value
       )

Python (Manager API)
    
    
    MTConLeverageTier.RangeFrom

### Parameters

**value**  
[in] The minimum range value for a level in a floating margin rule. The range type is determined by theIMTConLeverageRule::RangeModemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
