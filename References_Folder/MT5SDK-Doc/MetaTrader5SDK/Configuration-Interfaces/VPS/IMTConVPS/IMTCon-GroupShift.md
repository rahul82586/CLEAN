[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon GroupShift

[Previous](IMTCon-GroupClear.md) | [Next](IMTCon-GroupTotal.md)

# IMTConVPS::GroupShift

Move an entry in the list of groups in which the Sponsored VPS is allowed.

C++
    
    
    MTAPIRES  IMTConVPS::GroupShift(
       const UINT  pos,       // Group position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.GroupShift(
       uint        pos,       // Group position
       int         shift      // Shift
       )

Python
    
    
    MTConVPS.GroupShift(
       pos,        # Group position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**shift**  
[in] Shift of a group relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
