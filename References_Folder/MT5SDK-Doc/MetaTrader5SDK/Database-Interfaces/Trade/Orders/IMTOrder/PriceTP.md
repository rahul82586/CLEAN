[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / PriceTP

[Previous](PriceSL.md) | [Next](VolumeInitial.md)

# IMTOrder::PriceTP

Gets the [Take Profit (#take-profit)](../../General-Principles/Types-of-Orders.md#take-profit) level of an order.

C++
    
    
    double  IMTOrder::PriceTP()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTOrder.PriceTP()

Python
    
    
    MTOrder.PriceTP()

### Return Value

The Take Profit level of an order.

# IMTOrder::PriceTP

Set the [Take Profit (#take-profit)](../../General-Principles/Types-of-Orders.md#take-profit) level of an order.

C++
    
    
    MTAPIRES  IMTOrder::PriceTP(
       const double  price      // The Take Profit level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.PriceTP(
       double        price      // The Take Profit level
       )

Python
    
    
    MTOrder.PriceTP()

### Parameters

**price**  
[in] The Take Profit level of an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
