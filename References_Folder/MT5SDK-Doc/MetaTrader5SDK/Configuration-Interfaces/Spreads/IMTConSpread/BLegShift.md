[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / BLegShift

[Previous](BLegClear.md) | [Next](BLegTotal.md)

# IMTConSpread::BLegShift

Shift spread B leg configuration.

C++
    
    
    MTAPIRES  IMTConSpread::BLegShift(
       const UINT  pos,       // Spread leg position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.BLegShift(
       uint        pos,       // Spread leg position
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConSpread.BLegShift(
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
