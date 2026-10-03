[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / ExecMode

[Previous](CalcMode.md) | [Next](GTCMode.md)

# IMTConSymbol::ExecMode

Get the execution mode for a symbol.

C++
    
    
    UINT  IMTConSymbol::ExecMode()  const

.NET (Gateway/Manager API)
    
    
    EnExecutionMode  CIMTConSymbol.ExecMode()

Python (Manager API)
    
    
    MTConSymbol.ExecMode

### Return Value

One of the values of the [IMTConSymbol::EnExecutionMode (#enexecutionmode)](Enumerations.md#enexecutionmode) enumeration.

# IMTConSymbol::ExecMode

Set the execution mode for a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::ExecMode(
       const UINT       mode    // Execution mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.ExecMode(
       EnExecutionMode  mode    // Execution mode
       )

Python (Manager API)
    
    
    MTConSymbol.ExecMode

### Parameters

**mode**  
[in] To pass the execution mode, theIMTConSymbol::EnExecutionModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
