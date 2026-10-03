[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Price

[Previous](Symbol.md) | [Next](PriceSL.md)

# IMTDeal::Price

Get the price of a deal.

C++
    
    
    double  IMTDeal::Price()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.Price()

### Return Value

The price at which the deal was executed.

# IMTDeal::Price

Set the price of a deal.

C++
    
    
    MTAPIRES  IMTDeal::Price(
       const double  price      // Deal price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Price(
       double        price      // Deal price
       )

### Parameters

**price**  
[in] The price at which the deal is executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
