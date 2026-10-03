[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IEVolumeMaxDefault

[Previous](IEVolumeMaxExt.md) | [Next](IEVolumeMaxExtDefault.md)

# IMTConGroupSymbol::IEVolumeMaxDefault

Gets the [default](../../Symbols/IMTConSymbol/VolumeMax.md) maximum volume of a trade operation that can be executed in the instant execution mode. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::IEVolumeMaxDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.IEVolumeMaxDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.IEVolumeMaxDefault

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::IEVolumeMaxExtDefault](IEVolumeMaxExtDefault.md) method.
