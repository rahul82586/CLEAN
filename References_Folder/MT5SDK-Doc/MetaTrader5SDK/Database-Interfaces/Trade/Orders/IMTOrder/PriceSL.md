[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / PriceSL

[Previous](PriceCurrent.md) | [Next](PriceTP.md)

# IMTOrder::PriceSL

Gets the [Stop Loss (#stop-loss)](../../General-Principles/Types-of-Orders.md#stop-loss) level of an order.

C++
    
    
    double  IMTOrder::PriceSL()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTOrder.PriceSL()

Python
    
    
    MTOrder.PriceSL()

### Return Value

The Stop Loss level of an order.

# IMTOrder::PriceSL

Sets the [Stop Loss (#stop-loss)](../../General-Principles/Types-of-Orders.md#stop-loss) Stop Loss.

C++
    
    
    MTAPIRES  IMTOrder::PriceSL(
       const double  price      // The Stop Loss level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.PriceSL(
       double        price      // The Stop Loss level
       )

Python
    
    
    MTOrder.PriceSL()

### Parameters

**price**  
[in] The Stop Loss level of an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
