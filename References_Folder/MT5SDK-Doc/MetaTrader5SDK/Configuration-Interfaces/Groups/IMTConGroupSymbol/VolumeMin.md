[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeMin

[Previous](FreezeLevelDefault.md) | [Next](VolumeMinExt.md)

# IMTConGroupSymbol::VolumeMin

Gets the minimum volume of trade operations for a symbol for the group.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeMin()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeMin()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMin

### Return Value

The minimum volume of trade operations on a symbol for the group in the UINT64 format (one unit is equal to 1/10,000 of a lot).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeMinExt](VolumeMinExt.md) method.

# IMTConGroupSymbol::VolumeMin

Sets the minimum volume of trade operations for a symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::VolumeMin(
       const UINT64  volume      // Minimum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.VolumeMin(
       ulong         volume      // Minimum volume
       )

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMin

### Parameters

**volume**  
[in] The minimum volume of trade operations on a symbol for the group in the UINT64 format (one unit is equal to 1/10,000 of a lot).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeMinExt](VolumeMinExt.md) method.
