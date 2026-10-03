[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / RETimeout

[Previous](SwapRateSaturdayDefault.md) | [Next](RETimeoutDefault.md)

# IMTConGroupSymbol::RETimeout

Get the time during which the price issued by a dealer in the request execution mode is valid.

C++
    
    
    UINT  IMTConGroupSymbol::RETimeout()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroupSymbol.RETimeout()

Python (Manager API)
    
    
    MTConGroupSymbol.RETimeout

### Return Value

Time in seconds during which the price issued by a dealer in the request execution mode is valid.

### Note

This method operates with individual symbol settings for groups.

# IMTConGroupSymbol::RETimeout

Set the time during which the price issued by a dealer in the request execution mode is valid.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::RETimeout(
       const UINT  timeout      // Price validity period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.RETimeout(
       uint        timeout      // Price validity period
       )

Python (Manager API)
    
    
    MTConGroupSymbol.RETimeout

### Parameters

**timeout**  
[in] Time in seconds during which the price issued by a dealer in the request execution mode is valid.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method operates with individual symbol settings for groups.
