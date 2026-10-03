[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / VolumeStep

[Previous](VolumeMaxExt.md) | [Next](VolumeStepExt.md)

# IMTConSymbol::VolumeStep

Gets the volume change step for trade operations for a symbol.

C++
    
    
    UINT64  IMTConSymbol::VolumeStep()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSymbol.VolumeStep()

Python (Manager API)
    
    
    MTConSymbol.VolumeStep

### Return Value

The volume change step for trade operations for a symbol in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConSymbol::VolumeStepExt](VolumeStepExt.md) method.

# IMTConSymbol::VolumeStep

Sets the volume change step for trade operations for a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::VolumeStep(
       const UINT64  volume      // Volume change step
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.VolumeStep(
       ulong         volume      // Volume change step
       )

Python (Manager API)
    
    
    MTConSymbol.VolumeStep

### Parameters

**volume**  
[in] The volume change step for trade operations for a symbol in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConSymbol::VolumeStepExt](VolumeStepExt.md) method.
