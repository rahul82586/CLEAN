[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / GTCMode

[Previous](ExecMode.md) | [Next](FillFlags.md)

# IMTConSymbol::GTCMode

Get the mode of keeping the orders at a trade day change.

C++
    
    
    UINT  IMTConSymbol::GTCMode()  const

.NET (Gateway/Manager API)
    
    
    EnGTCMode  CIMTConSymbol.GTCMode()

Python (Manager API)
    
    
    MTConSymbol.GTCMode

### Return Value

A value of the [IMTConSymbol::EnGTCMode (#engtcmode)](Enumerations.md#engtcmode) enumeration.

# IMTConSymbol::GTCMode

Set the mode of keeping the orders at a trade day change.

C++
    
    
    MTAPIRES  IMTConSymbol::GTCMode(
       const UINT  mode      // Mode of keeping orders
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.GTCMode(
       EnGTCMode   mode      // Mode of keeping orders
       )

Python (Manager API)
    
    
    MTConSymbol.GTCMode

### Parameters

**mode**  
[in] To pass the mode of keeping the orders, theIMTConSymbol::EnGTCModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
