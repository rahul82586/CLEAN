[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueVolumeExt

[Previous](ValueVolume.md) | [Next](ValueDatetime.md)

# IMTConCondition::ValueVolumeExt

Gets the value of a condition that expresses the volume with extended accuracy.

C++
    
    
    UINT64  IMTConCondition::ValueVolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConCondition.ValueVolumeExt()

Python (Manager API)
    
    
    MTConCondition.ValueVolumeExt

### Return Value

Value in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConCondition::ValueVolume](ValueVolume.md) method.

# IMTConCondition::ValueVolumeExt

Sets the value of a condition that expresses the volume with extended accuracy.

C++
    
    
    MTAPIRES  IMTConCondition::ValueVolumeExt(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueVolumeExt(
       ulong         value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueVolumeExt

### Program Parameters

**value**  
[in] Value in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConCondition::ValueVolume](ValueVolume.md) method.
