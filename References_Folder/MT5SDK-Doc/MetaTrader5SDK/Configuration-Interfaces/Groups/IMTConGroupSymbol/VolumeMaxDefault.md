[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeMaxDefault

[Previous](VolumeMaxExt.md) | [Next](VolumeMaxExtDefault.md)

# IMTConGroupSymbol::VolumeMaxDefault

Gets the default value of [the maximum volume](../../Symbols/IMTConSymbol/VolumeMax.md) of trade operations for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeMaxDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeMaxDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMaxDefault

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeMaxExtDefault](VolumeMaxExtDefault.md) method.
