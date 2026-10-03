[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / RETimeout

[Previous](REFlags.md) | [Next](IECheckMode.md)

# IMTConSymbol::RETimeout

Get the time during which the price issued by a dealer in the request execution mode is valid.

C++
    
    
    UINT  IMTConSymbol::RETimeout()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.RETimeout()

Python (Manager API)
    
    
    MTConSymbol.RETimeout

### Return Value

Time in seconds during which the price issued by a dealer in the request execution mode is valid.

# IMTConSymbol::RETimeout

Set the time during which the price issued by a dealer in the request execution mode is valid.

C++
    
    
    MTAPIRES  IMTConSymbol::RETimeout(
       const UINT  timeout      // Price validity period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.RETimeout(
       uint        timeout      // Price validity period
       )

Python (Manager API)
    
    
    MTConSymbol.RETimeout

### Parameters

**timeout**  
[in] Time in seconds during which the price issued by a dealer in the request execution mode is valid.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
