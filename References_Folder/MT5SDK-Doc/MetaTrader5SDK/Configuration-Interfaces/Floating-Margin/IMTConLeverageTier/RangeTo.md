[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageTier](../IMTConLeverageTier.md) / RangeTo

[Previous](RangeFrom.md) | [Next](MarginRateInitial.md)

# IMTConLeverageTier::RangeTo

Get the maximum range value for a level in a floating margin rule.

C++
    
    
    double  IMTConLeverageTier::RangeTo()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConLeverageTier.RangeTo()

Python (Manager API)
    
    
    MTConLeverageTier.RangeTo

### Return Value

The maximum range value for a level in a floating margin rule. The range type is determined by the [IMTConLeverageRule::RangeMode](../IMTConLeverageRule/RangeMode.md) method.

# IMTConLeverageTier::RangeTo

Set the maximum range value for a level in a floating margin rule.

C++
    
    
    MTAPIRES  IMTConLeverageTier::RangeTo(
       const double  value      // Maximum value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageTier.RangeTo(
       double        value      // Maximum value
       )

Python (Manager API)
    
    
    MTConLeverageTier.RangeTo

### Parameters

**value**  
[in] The maximum range value for a level in a floating margin rule. The range type is determined by theIMTConLeverageRule::RangeModemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
