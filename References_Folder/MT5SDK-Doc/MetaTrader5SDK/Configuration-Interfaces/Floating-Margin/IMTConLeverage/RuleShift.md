[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / RuleShift

[Previous](RuleClear.md) | [Next](RuleTotal.md)

# IMTConLeverage::RuleShift

Move a rule in a floating margin configuration.

C++
    
    
    MTAPIRES  IMTConLeverage::RuleShift(
       const UINT  pos,       // Position of the rule
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverage.RuleShift(
       uint        pos,       // Position of the rule
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConLeverage.RuleShift(
       pos,        # Position of the rule
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the rule in the list, starting from 0.

**shift**  
[in] Shift of a rule relative to its current position. A negative value means shift towards the top of the list, while a positive value shifts the item towards the end.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
