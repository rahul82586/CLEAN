[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Profit

[Previous](VolumeClosedExt.md) | [Next](Value.md)

# IMTDeal::Profit

Get the value of the profit from the deal execution.

C++
    
    
    double  IMTDeal::Profit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.Profit()

### Return Value

Profit from a deal.

# IMTDeal::Profit

Set the value of the profit from the deal execution.

C++
    
    
    MTAPIRES  IMTDeal::Profit(
       const double  profit      // Profit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Profit(
       double        profit      // Profit
       )

### Parameters

**profit**  
[in] Profit from a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
