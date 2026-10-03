[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / PriceTrigger

[Previous](PriceOrder.md) | [Next](PriceCurrent.md)

# IMTOrder::PriceTrigger

Get the price, at which a Limit order is placed when the Stop Limit order triggers.

C++
    
    
    double  IMTOrder::PriceTrigger()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTOrder.PriceTrigger()

Python
    
    
    MTOrder.PriceTrigger()

### Return Value

The price, at which a Limit order is placed when the Stop Limit order triggers.

### Note

This method is used only when working with Stop Limit orders. The Stop Limit order trigger price is specified in [IMTOrder::PriceOrder](PriceOrder.md).

# IMTOrder::PriceTrigger

Set the price, at which a Limit order is placed when the Stop Limit order triggers.

C++
    
    
    MTAPIRES  IMTOrder::PriceTrigger(
       const double  price      // Limit order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.PriceTrigger(
       double        price      // Limit order price
       )

Python
    
    
    MTOrder.PriceTrigger()

### Parameters

**price**  
[in] The price, at which a Limit order is placed when the Stop Limit order triggers.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is used only when working with Stop Limit orders. The Stop Limit order trigger price is specified in [IMTOrder::PriceOrder](PriceOrder.md).
