[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / VolumeMaxExt

[Previous](VolumeMax.md) | [Next](VolumeStep.md)

# IMTConSymbol::VolumeMaxExt

Gets the maximum volume of trade operations for the symbol for the group with extended accuracy.

C++
    
    
    UINT64  IMTConSymbol::VolumeMaxExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSymbol.VolumeMaxExt()

Python (Manager API)
    
    
    MTConSymbol.VolumeMaxExt

### Return Value

The maximum volume of trading operations for a symbol, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConSymbol::VolumeMax](VolumeMax.md) method.

# IMTConSymbol::VolumeMaxExt

Sets the maximum volume of trade operations for the symbol for the group with extended accuracy.

C++
    
    
    MTAPIRES  IMTConSymbol::VolumeMaxExt(
       const UINT64  volume      // Maximum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.VolumeMaxExt(
       ulong         volume      // Maximum volume
       )

Python (Manager API)
    
    
    MTConSymbol.VolumeMaxExt

### Program Parameters

**volume**  
[in] The maximum volume of trading operations for a symbol, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConSymbol::VolumeMax](VolumeMax.md) method.
