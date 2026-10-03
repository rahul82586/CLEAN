[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / IECheckMode

[Previous](RETimeout.md) | [Next](IETimeout.md)

# IMTConSymbol::IECheckMode

Get the check mode for instant execution.

C++
    
    
    UINT  IMTConSymbol::IECheckMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.IECheckMode()

Python (Manager API)
    
    
    MTConSymbol.IECheckMode

### Return Value

A value of the [IMTConSymbol::EnInstantMode (#eninstantmode)](Enumerations.md#eninstantmode) enumeration.

### Note

This method is reserved for future use and is not currently implemented.

# IMTConSymbol::IECheckMode

Set the check mode for instant execution.

C++
    
    
    MTAPIRES  IMTConSymbol::IECheckMode(
       const UINT  mode      // Mode of checking
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.IECheckMode(
       uint        mode      // Mode of checking
       )

Python (Manager API)
    
    
    MTConSymbol.IECheckMode

### Parameters

**mode**  
[in] Check mode for instant execution. To pass the mode, theIMTConSymbol::EnInstantModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is reserved for future use and is not currently implemented.
