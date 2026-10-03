[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueVolume

[Previous](ValueMoney.md) | [Next](ValueVolumeExt.md)

# IMTConCondition::ValueVolume

Gets the value of a condition that expresses the volume.

C++
    
    
    UINT64  IMTConCondition::ValueVolume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConCondition.ValueVolume()

Python (Manager API)
    
    
    MTConCondition.ValueVolume

### Return Value

A value in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConCondition::ValueVolumeExt](ValueVolumeExt.md) method.

# IMTConCondition::ValueVolume

Sets the value of a condition that expresses the volume.

C++
    
    
    MTAPIRES  IMTConCondition::ValueVolume(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueVolume(
       ulong         value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueVolume

### Parameters

**value**  
[in] A value in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConCondition::ValueVolumeExt](ValueVolumeExt.md) method.
