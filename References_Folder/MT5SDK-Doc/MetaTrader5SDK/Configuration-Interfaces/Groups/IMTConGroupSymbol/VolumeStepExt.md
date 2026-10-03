[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeStepExt

[Previous](VolumeStep.md) | [Next](VolumeStepDefault.md)

# IMTConGroupSymbol::VolumeStepExt

Gets the step of change of trade operations volume (with extended accuracy) for a symbol for the group.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeStepExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeStepExt()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeStepExt

### Return Value

Step of change of the volume of trading operations for a symbol for this group, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeStep](VolumeStep.md) method.

# IMTConGroupSymbol::VolumeStepExt

Sets the step of change of trade operations volume (with extended accuracy) for a symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::VolumeStepExt(
       const UINT64  volume      // Volume change step
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.VolumeStepExt(
       ulong         volume      // Volume change step
       )

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeStepExt

### Program Parameters

**volume**  
[in] Step of change of the volume of trading operations for a symbol for this group, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeStep](VolumeStep.md) method.
