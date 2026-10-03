[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeStepDefault

[Previous](VolumeStepExt.md) | [Next](VolumeStepExtDefault.md)

# IMTConGroupSymbol::VolumeStepDefault

Gets the default value of [the volume change step](../../Symbols/IMTConSymbol/VolumeStep.md) for trade operations on a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeStepDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeStepDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeStepDefault

### Note

The method operates with [the standard volume accuracy (#volume)](../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTConGroupSymbol::VolumeStepExtDefault](VolumeStepExtDefault.md) method.
