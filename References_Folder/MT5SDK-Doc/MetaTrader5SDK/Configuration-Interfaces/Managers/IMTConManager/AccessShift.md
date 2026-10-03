[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / AccessShift

[Previous](AccessDelete.md) | [Next](AccessTotal.md)

# IMTConManager::AccessShift

Move a range of IP addresses, from which a manager is allowed to connect to the platform, in the list.

C++
    
    
    MTAPIRES  IMTConManager::AccessShift(
       const UINT  pos,       // Position of the range
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.AccessShift(
       uint        pos,       // Position of the range
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConManager.AccessShift(
       pos,        # Position of the range
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of a range of addresses in the list, starting with 0.

**shift**  
[in] Shift of the range of addresses relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
