[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / VolumeMinExt

[Previous](VolumeMin.md) | [Next](VolumeMax.md)

# IMTConSymbol::VolumeMinExt

Gets the minimum volume of trade operations for the symbol for the group with extended accuracy.

C++
    
    
    UINT64  IMTConSymbol::VolumeMinExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSymbol.VolumeMinExt()

Python (Manager API)
    
    
    MTConSymbol.VolumeMinExt

### Return Value

The minimum volume of trading operations for a symbol, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConSymbol::VolumeMin](VolumeMin.md) method.

# IMTConSymbol::VolumeMinExt

Sets the minimum volume of trade operations for the symbol for the group with extended accuracy.

C++
    
    
    MTAPIRES  IMTConSymbol::VolumeMinExt(
       const UINT64  volume      // Minimum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.VolumeMinExt(
       ulong         volume      // Minimum volume
       )

Python (Manager API)
    
    
    MTConSymbol.VolumeMinExt

### Program Parameters

**volume**  
[in] The minimum volume of trading operations for a symbol, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConSymbol::VolumeMin](VolumeMin.md) method.
