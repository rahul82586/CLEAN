[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / TickValue

[Previous](PricePosition.md) | [Next](TickSize.md)

# IMTDeal::TickValue

Get the tick price for a deal.

C++
    
    
    double  IMTDeal::TickValue()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.TickValue()

### Return Value

The tick price for a deal.

# IMTDeal::TickValue

Set the tick price for a deal.

C++
    
    
    MTAPIRES  IMTDeal::TickValue(
       const double  value      // Tick price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.TickValue(
       double        value      // Tick price
       )

### Parameters

**value**  
[in] The tick price for a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
