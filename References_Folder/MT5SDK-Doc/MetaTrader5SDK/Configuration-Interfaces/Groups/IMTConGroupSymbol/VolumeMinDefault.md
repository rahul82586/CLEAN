[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeMinDefault

[Previous](VolumeMinExt.md) | [Next](VolumeMinExtDefault.md)

# IMTConGroupSymbol::VolumeMinDefault

Get the default value of [the minimum volume](../../Symbols/IMTConSymbol/VolumeMin.md) of trade operations for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeMinDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeMinDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMinDefault

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeMinExtDefault](VolumeMinExtDefault.md) method.
