[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Type

[Previous](TimeDoneMsc.md) | [Next](TypeFill.md)

# IMTOrder::Type

Get the order type.

C++
    
    
    UINT  IMTOrder::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTOrder.Type()

Python
    
    
    MTOrder.Type()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](Enumerations.md#enordertype) enumeration.

# IMTOrder::Type

Set the order type.

C++
    
    
    MTAPIRES  IMTOrder::Type(
       const UINT  type      // Order type
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.Type(
       uint        type      // Order type
       )

Python
    
    
    MTOrder.Type()

### Parameters

**type**  
[in] Order type. To pass the order type, theIMTOrder::EnOrderTypeenumeration is used..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
