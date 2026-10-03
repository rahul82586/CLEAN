[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / RateProfit

[Previous](Fee.md) | [Next](RateMargin.md)

# IMTDeal::RateProfit

Gets the exchange rate of the profit currency of a deal to the deposit currency of a client group.

C++
    
    
    double  IMTDeal::RateProfit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.RateProfit()

### Return Value

The exchange rate of the profit currency of a deal to the deposit currency of a client group.

# IMTDeal::RateProfit

Sets the exchange rate of the profit currency of a deal to the deposit currency of a client group.

C++
    
    
    MTAPIRES  IMTDeal::RateProfit(
       const double  rate      // Profit ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.RateProfit(
       double        rate      // Profit ratio
       )

### Parameters

**rate**  
[in] The exchange rate of the profit currency of a deal to the deposit currency of a client group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
