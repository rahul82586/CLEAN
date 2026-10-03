[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / ALegShift

[Previous](ALegClear.md) | [Next](ALegTotal.md)

# IMTConSpread::ALegShift

Shift spread A leg configuration.

C++
    
    
    MTAPIRES  IMTConSpread::ALegShift(
       const UINT  pos,       // Spread leg position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.ALegShift(
       uint        pos,       // Spread leg position
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConSpread.ALegShift(
       pos,        # Spread leg position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Spread leg configuration position starting from 0.

**shift**  
[in] Shift of a leg relative to its current position in minutes. A negative value means the shift to an earlier time, a positive value - to a later time.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
