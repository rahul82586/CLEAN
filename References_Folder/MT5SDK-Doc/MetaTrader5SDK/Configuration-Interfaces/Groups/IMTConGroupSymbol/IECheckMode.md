[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IECheckMode

[Previous](REFlagsDefault.md) | [Next](IECheckModeDefault.md)

# IMTConGroupSymbol::IECheckMode

Get the mode of checking during instant execution set for a group.

C++
    
    
    UINT  IMTConGroupSymbol::IECheckMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroupSymbol.IECheckMode()

Python (Manager API)
    
    
    MTConGroupSymbol.IECheckMode

### Return Value

A value of the [IMTConSymbol::EnInstantMode (#eninstantmode)](../../Symbols/IMTConSymbol/Enumerations.md#eninstantmode) enumeration.

### Note

This method is reserved for future use and is not currently implemented.

# IMTConGroupSymbol::IECheckMode

Set the mode of checking during instant execution for a group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::IECheckMode(
       const UINT  mode      // Mode of checking
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.IECheckMode(
       uint        mode      // Mode of checking
       )

Python (Manager API)
    
    
    MTConGroupSymbol.IECheckMode

### Parameters

**mode**  
[in] Check mode for instant execution. To pass the check mode, theIMTConSymbol::EnInstantModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is reserved for future use and is not currently implemented.
