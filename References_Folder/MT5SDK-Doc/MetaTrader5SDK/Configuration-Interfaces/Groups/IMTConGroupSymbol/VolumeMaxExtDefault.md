[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeMaxExtDefault

[Previous](VolumeMaxDefault.md) | [Next](VolumeStep.md)

# IMTConGroupSymbol::VolumeMaxExtDefault

Gets the default [maximum volume](../../Symbols/IMTConSymbol/VolumeMax.md) of trade operations for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeMaxExtDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeMaxExtDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMaxExtDefault

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeMaxDefault](VolumeMaxDefault.md) method.
