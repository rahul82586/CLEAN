[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon RuleShift

[Previous](IMTCon-RuleClear.md) | [Next](IMTCon-RuleTotal.md)

# IMTConVPS::RuleShift

Move the VPS allocation rule in the list.

C++
    
    
    MTAPIRES  IMTConVPS::RuleShift(
       const UINT  pos,       // Rule position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.RuleShift(
       uint        pos,       // Rule position
       int         shift      // Shift
       )

Python
    
    
    MTConVPS.RuleShift(
       pos,        # Rule position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Rule position in the list starting from 0.

**shift**  
[in] Shift of a rule relative to its current position. A negative value means shift towards the top of the list, and a positive value shifts the item towards the end.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
