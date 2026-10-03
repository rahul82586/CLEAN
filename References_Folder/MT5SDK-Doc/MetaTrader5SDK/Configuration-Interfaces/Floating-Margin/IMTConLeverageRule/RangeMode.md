[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / RangeMode

[Previous](Path.md) | [Next](RangeValueCurrency.md)

# IMTConSubscription::RangeMode

Get the level type for a rule in a floating margin configuration.

C++
    
    
    UINT  IMTConSubscription::RangeMode()  const

.NET (Gateway/Manager API)
    
    
    EnControlMode  CIMTConSubscription.RangeMode()

Python (Manager API)
    
    
    MTConSubscription.RangeMode

### Return Value

Level type in a rule. Passed as a value of the [IMTConLeverageRule::EnRangeMode (#enrangemode)](Enumerations.md#enrangemode) enumeration.

# IMTConSubscription::RangeMode

Set the level type for a rule in a floating margin configuration.

C++
    
    
    MTAPIRES  IMTConSubscription::RangeMode(
       const UINT      mode     // Level type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.RangeMode(
       EnControlMode   mode     // Level type
       )

Python (Manager API)
    
    
    MTConSubscription.RangeMode

### Parameters

**mode**  
[in] Level type in the rule. Passed as a value of theIMTConLeverageRule::EnRangeModeenumeration.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
