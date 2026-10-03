[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeMinExtDefault

[Previous](VolumeMinDefault.md) | [Next](VolumeMax.md)

# IMTConGroupSymbol::VolumeMinExtDefault

Gets the default [minimum volume](../../Symbols/IMTConSymbol/VolumeMin.md) (with extended accuracy) of trading operations for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeMinExtDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeMinExtDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeMinExtDefault

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeMinDefault](VolumeMinDefault.md) method.
