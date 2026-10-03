[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TickFlags

[Previous](Multiply.md) | [Next](TickBookDepth.md)

# IMTConSymbol::TickFlags

Get the settings of working with tick data.

C++
    
    
    UINT64  IMTConSymbol::TickFlags()  const

.NET (Gateway/Manager API)
    
    
    EnTickFlags  CIMTConSymbol.TickFlags()

Python (Manager API)
    
    
    MTConSymbol.TickFlags

### Return Value

To pass the settings, the [IMTConSymbol::EnTickFlags (#entickflags)](Enumerations.md#entickflags) enumeration is used.

# IMTConSymbol::TickFlags

Set the settings of working with tick data.

C++
    
    
    MTAPIRES  IMTConSymbol::TickFlags(
       const UINT64  flags      // Flags of settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TickFlags(
       EnTickFlags   flags      // Flags of settings
       )

Python (Manager API)
    
    
    MTConSymbol.TickFlags

### Parameters

**flags**  
[in] To pass the settings, theIMTConSymbol::EnTickFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
