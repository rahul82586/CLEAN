[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / TickSize

[Previous](TickValue.md) | [Next](Flags.md)

# IMTDeal::TickSize

Get the tick size for a deal.

C++
    
    
    double  IMTDeal::TickSize()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.TickSize()

### Return Value

The tick size for a deal.

# IMTDeal::TickSize

Set the tick size for a deal.

C++
    
    
    MTAPIRES  IMTDeal::TickSize(
       const double  size      // Tick size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.TickSize(
       double        size      // Tick size
       )

### Parameters

**value**  
[in] The tick size for a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
