[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IETimeout

[Previous](IECheckModeDefault.md) | [Next](IETimeoutDefault.md)

# IMTConGroupSymbol::IETimeout

Gets the maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price.

C++
    
    
    UINT  IMTConGroupSymbol::IETimeout()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroupSymbol.IETimeout()

Python (Manager API)
    
    
    MTConGroupSymbol.IETimeout

### Return Value

The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price; after this time interval the client gets a requote.

### Note

This method operates with individual symbol settings for groups.

# IMTConGroupSymbol::IETimeout

Sets the maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::IETimeout(
       const UINT  timeout      // Time difference
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.IETimeout(
       uint        timeout      // Time difference
       )

Python (Manager API)
    
    
    MTConGroupSymbol.IETimeout

### Parameters

**timeout**  
[in] The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price; after this time interval the client gets a requote.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method operates with individual symbol settings for groups.
