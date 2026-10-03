[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / REFlags

[Previous](SessionTradeNext.md) | [Next](RETimeout.md)

# IMTConSymbol::REFlags

Get the flags of request execution ([IMTConSymbol::EXECUTION_REQUEST (#enexecutionmode)](Enumerations.md#enexecutionmode)).

C++
    
    
    UINT  IMTConSymbol::REFlags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.REFlags()

Python (Manager API)
    
    
    MTConSymbol.REFlags

### Return Value

A value of the [IMTConSymbol::EnRequestFlags (#enrequestflags)](Enumerations.md#enrequestflags) enumeration.

# IMTConSymbol::REFlags

Set the flags of request execution ([IMTConSymbol::EXECUTION_REQUEST (#enexecutionmode)](Enumerations.md#enexecutionmode)).

C++
    
    
    MTAPIRES  IMTConSymbol::REFlags(
       const UINT  flags      // Flags of request execution
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.REFlags(
       uint        flags      // Flags of request execution
       )

Python (Manager API)
    
    
    MTConSymbol.REFlags

### Parameters

**flags**  
[in] The request execution flags. The flags are passed using theIMTConSymbol::EnRequestFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
