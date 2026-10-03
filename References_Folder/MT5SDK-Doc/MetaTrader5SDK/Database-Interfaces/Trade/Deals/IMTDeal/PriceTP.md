[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / PriceTP

[Previous](PriceSL.md) | [Next](Volume.md)

# IMTDeal::PriceTP

Gets the [Take Profit (#take-profit)](../../General-Principles/Types-of-Orders.md#take-profit) level of a deal.

C++
    
    
    double  IMTDeal::PriceTP()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.PriceTP()

### Return Value

The Take Profit level of an order.

### Note

Take Profit values for entry and reversal deals are set in accordance with the Take Profit of orders, which initiated these deals. The Take Profit values ​​of appropriate positions as of the time of position closing are used for exit deals. 

# IMTOrder::PriceTP

Set the [Take Profit (#take-profit)](../../General-Principles/Types-of-Orders.md#take-profit) level of a deal.

C++
    
    
    MTAPIRES  IMTDeal::PriceTP(
       const double  price      // The Take Profit level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.PriceTP(
       double        price      // The Take Profit level
       )

### Parameters

**price**  
[in] The Take Profit level of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
