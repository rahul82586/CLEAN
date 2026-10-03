[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / PriceOrder

[Previous](TypeTime.md) | [Next](PriceTrigger.md)

# IMTOrder::PriceOrder

Get the price, at which the order was placed.

C++
    
    
    double  IMTOrder::PriceOrder()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTOrder.PriceOrder()

Python
    
    
    MTOrder.PriceOrder()

### Return Value

The price, at which the order was placed.

# IMTOrder::PriceOrder

Set the order price.

C++
    
    
    MTAPIRES  IMTOrder::PriceOrder(
       const double  price      // Order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.PriceOrder(
       double        price      // Order price
       )

Python
    
    
    MTOrder.PriceOrder()

### Parameters

**price**  
[in] Order price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
