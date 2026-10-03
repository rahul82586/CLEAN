[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerShift

[Previous](DealerClear.md) | [Next](DealerTotal.md)

# IMTConRoute::DealerShift

Move an entry of a dealer to whom requests under the conditions of this rule will be sent for processing.

C++
    
    
    MTAPIRES  IMTConRoute::DealerShift(
       const UINT  pos,       // Position of a dealer entry
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.DealerShift(
       uint        pos,       // Position of a dealer entry
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConRoute.DealerShift(
       pos,        # Position of a dealer entry
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of a dealer entry in the list, starting with 0.

**shift**  
[in] Shift the dealer entry relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
