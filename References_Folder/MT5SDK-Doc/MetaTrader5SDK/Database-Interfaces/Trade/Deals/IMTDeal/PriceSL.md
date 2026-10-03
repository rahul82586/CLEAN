[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / PriceSL

[Previous](Price.md) | [Next](PriceTP.md)

# IMTDeal::PriceSL

Gets the [Stop Loss (#stop-loss)](../../General-Principles/Types-of-Orders.md#stop-loss) level of a deal.

C++
    
    
    double  IMTDeal::PriceSL()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.PriceSL()

### Return Value

The Stop Loss level of a deal.

### Note

Stop Loss values for entry and reversal deals are set in accordance with the Stop Loss of orders, which initiated these deals. The Stop Loss values ​​of appropriate positions as of the time of position closing are used for exit deals.

# IMTDeal::PriceSL

Sets the [Stop Loss (#stop-loss)](../../General-Principles/Types-of-Orders.md#stop-loss) Stop Loss of a deal.

C++
    
    
    MTAPIRES  IMTDeal::PriceSL(
       const double  price      // The Stop Loss level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.PriceSL(
       double        price      // The Stop Loss level
       )

### Parameters

**price**  
[in] The Stop Loss level of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
