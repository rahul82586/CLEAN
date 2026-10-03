[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IEVolumeMaxExtDefault

[Previous](IEVolumeMaxDefault.md) | [Next](IEFlags.md)

# IMTConGroupSymbol::IEVolumeMaxExtDefault

Gets the [default](../../Symbols/IMTConSymbol/VolumeMax.md) maximum volume of a trade operation which can be executed in the instant execution mode. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::IEVolumeMaxExtDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.IEVolumeMaxExtDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.IEVolumeMaxExtDefault

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::IEVolumeMaxDefault](IEVolumeMaxDefault.md) method.
