[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / IEFlags

[Previous](IEVolumeMaxExt.md) | [Next](PriceSettle.md)

# IMTConSymbol::IEFlags

Get flags for the instant execution mode ([IMTConSymbol::EXECUTION_INSTANT (#enexecutionmode)](Enumerations.md#enexecutionmode)).

C++
    
    
    UINT  IMTConSymbol::IEFlags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.IEFlags()

Python (Manager API)
    
    
    MTConSymbol.IEFlags

### Return Value

A value from the [IMTConSymbol::EnInstantFlags (#eninstantflags)](Enumerations.md#eninstantflags) enumeration.

# IMTConSymbol::IEFlags

Set flags for the instant execution mode ([IMTConSymbol::EXECUTION_INSTANT (#enexecutionmode)](Enumerations.md#enexecutionmode)).

C++
    
    
    MTAPIRES  IMTConSymbol::IEFlags(
       const UINT  flags      // Instant execution flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.IEFlags(
       uint        flags      // Instant execution flags
       )

Python (Manager API)
    
    
    MTConSymbol.IEFlags

### Parameters

**flags**  
[in] Instant execution flags. They are passed using theIMTConSymbol::EnInstantFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
