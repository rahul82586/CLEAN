[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / GroupShift

[Previous](GroupClear.md) | [Next](GroupTotal.md)

# IMTConMessenger::GroupShift

Shift a group in the messenger settings.

C++
    
    
    MTAPIRES  IMTConMessenger::GroupShift(
       const UINT  pos,       // Group position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.GroupShift(
       uint        pos,       // Group position
       int         shift      // Shift
       )

Python
    
    
    MTConMessenger.GroupShift(
       pos,        # Group position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**shift**  
[in] The shift of the group relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
