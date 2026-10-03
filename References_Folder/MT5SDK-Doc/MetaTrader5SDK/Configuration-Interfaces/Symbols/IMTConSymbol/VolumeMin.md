[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / VolumeMin

[Previous](QuotesTimeout.md) | [Next](VolumeMinExt.md)

# IMTConSymbol::VolumeMin

Gets the minimum volume of trade operations for a symbol.

C++
    
    
    UINT64  IMTConSymbol::VolumeMin()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSymbol.VolumeMin()

Python (Manager API)
    
    
    MTConSymbol.VolumeMin

### Return Value

The minimum volume of trade operations for a symbol in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConSymbol::VolumeMinExt](VolumeMinExt.md) method.

# IMTConSymbol::VolumeMin

Sets the minimum volume of trade operations for a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::VolumeMin(
       const UINT64  volume      // Minimum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.VolumeMin(
       ulong         volume      // Minimum volume
       )

Python (Manager API)
    
    
    MTConSymbol.VolumeMin

### Parameters

**volume**  
[in] The minimum volume of trade operations for a symbol in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConSymbol::VolumeMinExt](VolumeMinExt.md) method.
