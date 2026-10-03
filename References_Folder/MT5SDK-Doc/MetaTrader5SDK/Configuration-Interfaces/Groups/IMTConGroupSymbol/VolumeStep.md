[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeStep

[Previous](VolumeMaxExtDefault.md) | [Next](VolumeStepExt.md)

# IMTConGroupSymbol::VolumeStep

Gets the step of change of trade operations volume for a symbol for the group.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeStep()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeStep()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeStep

### Return Value

The step of change of the volume of trade operations on a symbol for the group in the UINT64 format (one unit is equal to 1/10,000 of a lot).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeStepExt](VolumeStepExt.md) method.

# IMTConGroupSymbol::VolumeStep

Sets the step of change of trade operations volume for a symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::VolumeStep(
       const UINT64  volume      // Volume change step
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.VolumeStep(
       ulong         volume      // Volume change step
       )

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeStep

### Parameters

**volume**  
[in] Change step of the volume of trade operations on a symbol for the group in the UINT64 format (one unit is equal to 1/10,000 of a lot).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeStepExt](VolumeStepExt.md) method.
