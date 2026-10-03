[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / ExecMode

[Previous](TradeModeDefault.md) | [Next](ExecModeDefault.md)

# IMTConGroupSymbol::ExecMode

Get the symbol execution mode for the group.

C++
    
    
    UINT  IMTConGroupSymbol::ExecMode()  const

.NET (Gateway/Manager API)
    
    
    EnExecutionMode  CIMTConGroupSymbol.ExecMode()

Python (Manager API)
    
    
    MTConGroupSymbol.ExecMode

### Return Value

One of the values of the [IMTConSymbol::EnExecutionMode (#enexecutionmode)](../../Symbols/IMTConSymbol/Enumerations.md#enexecutionmode) enumeration.

# IMTConGroupSymbol::ExecMode

Set the symbol execution mode for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::ExecMode(
       const UINT       mode  // Execution mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.ExecMode(
       EnExecutionMode  mode  // Execution mode
       )

Python (Manager API)
    
    
    MTConGroupSymbol.ExecMode

### Parameters

**mode**  
[in] To pass the execution mode, theIMTConSymbol::EnExecutionModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
