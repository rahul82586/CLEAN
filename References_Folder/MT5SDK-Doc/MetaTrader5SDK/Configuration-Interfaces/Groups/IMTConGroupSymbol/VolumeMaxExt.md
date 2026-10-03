[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeMaxExt

[Previous](VolumeMax.md) | [Next](VolumeMaxDefault.md)

# IMTConGroupSymbol::VolumeMaxExt

Gets the maximum volume (with extended accuracy) of trade operations for a symbol for the group.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeMaxExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeMaxExt()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMaxExt

### Return Value

The maximum volume of trading operations for a symbol for this group, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeMax](VolumeMax.md) method.

# IMTConGroupSymbol::VolumeMaxExt

Sets the maximum volume (with extended accuracy) of trade operations for a symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::VolumeMaxExt(
       const UINT64  volume      // Maximum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.VolumeMaxExt(
       ulong         volume      // Maximum volume
       )

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMaxExt

### Program Parameters

**volume**  
[in] The maximum volume of trading operations for a symbol for this group, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeMax](VolumeMax.md) method.
