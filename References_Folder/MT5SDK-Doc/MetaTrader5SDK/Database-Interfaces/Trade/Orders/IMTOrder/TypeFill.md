[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / TypeFill

[Previous](Type.md) | [Next](TypeTime.md)

# IMTOrder::TypeFill

Get the order filling type.

C++
    
    
    UINT  IMTOrder::TypeFill()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTOrder.TypeFill()

Python
    
    
    MTOrder.TypeFill()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](Enumerations.md#enorderfilling) enumeration.

# IMTOrder::TypeFill

Set the order filling type.

C++
    
    
    MTAPIRES  IMTOrder::TypeFill(
       const UINT  type      // Type of filling
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.TypeFill(
       uint        type      // Type of filling
       )

Python
    
    
    MTOrder.TypeFill()

### Parameters

**type**  
[in] Order filling type. To pass the type, theIMTOrder::EnOrderFillingenumeration is used..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
