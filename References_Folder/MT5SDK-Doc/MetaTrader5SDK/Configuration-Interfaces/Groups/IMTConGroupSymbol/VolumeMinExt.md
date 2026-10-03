[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeMinExt

[Previous](VolumeMin.md) | [Next](VolumeMinDefault.md)

# IMTConGroupSymbol::VolumeMinExt

Gets the minimum volume (with extended accuracy) of trade operations for a symbol for the group.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeMinExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeMinExt()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMinExt

### Return Value

The minimum volume of trading operations for a symbol for this group, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeMin](VolumeMin.md) method.

# IMTConGroupSymbol::VolumeMinExt

Sets the minimum volume (with extended accuracy) of trade operations for a symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::VolumeMinExt(
       const UINT64  volume      // Minimum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.VolumeMinExt(
       ulong         volume      // Minimum volume
       )

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMinExt

### Program Parameters

**volume**  
[in] The minimum volume of trading operations for a symbol for this group, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeMin](VolumeMin.md) method.
