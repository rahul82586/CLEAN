[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeStepExtDefault

[Previous](VolumeStepDefault.md) | [Next](VolumeLimit.md)

# IMTConGroupSymbol::VolumeStepExtDefault

Gets the default value of the [volume change step](../../Symbols/IMTConSymbol/VolumeStep.md) (with extended accuracy) for trade operations for a symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeStepExtDefault()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeStepExtDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeStepExtDefault

### Note

The method operates with [the extended volume accuracy (#volume)](../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTConGroupSymbol::VolumeStepDefault](VolumeStepDefault.md) method.
