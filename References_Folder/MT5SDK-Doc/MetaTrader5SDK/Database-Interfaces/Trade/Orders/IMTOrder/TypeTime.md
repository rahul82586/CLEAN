[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / TypeTime

[Previous](TypeFill.md) | [Next](PriceOrder.md)

# IMTOrder::TypeTime

Get the order expiration type.

C++
    
    
    UINT  IMTOrder::TypeTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTOrder.TypeTime()

Python
    
    
    MTOrder.TypeTime()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](Enumerations.md#enordertime) enumeration.

# IMTOrder::TypeTime

Set the order expiration type.

C++
    
    
    MTAPIRES  IMTOrder::TypeTime(
       const UINT  type      // Expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.TypeTime(
       uint         type     // Expiration type
       )

Python
    
    
    MTOrder.TypeTime()

### Parameters

**type**  
[in] Order expiration type. To pass the type, theIMTOrder::EnOrderTimeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
