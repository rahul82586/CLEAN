[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IEFlags

[Previous](IEVolumeMaxExtDefault.md) | [Next](IEFlagsDefault.md)

# IMTConGroupSymbol::IEFlags

Get flags for the instant execution mode ([IMTConSymbol::EXECUTION_INSTANT (#enexecutionmode)](../../Symbols/IMTConSymbol/Enumerations.md#enexecutionmode)).

C++
    
    
    UINT  IMTConGroupSymbol::IEFlags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroupSymbol.IEFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.IEFlags

### Return Value

A value from the [IMTConSymbol::EnInstantFlags (#eninstantflags)](../../Symbols/IMTConSymbol/Enumerations.md#eninstantflags) enumeration.

### Note

This method operates with individual symbol settings for groups.

# IMTConGroupSymbol::IEFlags

Set flags for the instant execution mode ([IMTConSymbol::EXECUTION_INSTANT (#enexecutionmode)](../../Symbols/IMTConSymbol/Enumerations.md#enexecutionmode)).

C++
    
    
    MTAPIRES  IMTConGroupSymbol::IEFlags(
       const UINT  flags      // Instant execution flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.IEFlags(
       uint        flags      // Instant execution flags
       )

Python (Manager API)
    
    
    MTConGroupSymbol.IEFlags

### Parameters

**flags**  
[in] Instant execution flags. They are passed using theIMTConSymbol::EnInstantFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method operates with individual symbol settings for groups.
