[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / IETimeout

[Previous](IECheckMode.md) | [Next](IESlipProfit.md)

# IMTConSymbol::IETimeout

Gets the maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price.

C++
    
    
    UINT  IMTConSymbol::IETimeout()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.IETimeout()

Python (Manager API)
    
    
    MTConSymbol.IETimeout

### Return Value

The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price; after this time interval the client gets a requote.

# IMTConSymbol::IETimeout

Sets the maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price.

C++
    
    
    MTAPIRES  IMTConSymbol::IETimeout(
       const UINT  timeout      // Time difference
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.IETimeout(
       uint        timeout      // Time difference
       )

Python (Manager API)
    
    
    MTConSymbol.IETimeout

### Parameters

**timeout**  
[in] The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
