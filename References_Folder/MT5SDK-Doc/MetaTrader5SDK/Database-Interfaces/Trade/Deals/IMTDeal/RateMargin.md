[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / RateMargin

[Previous](RateProfit.md) | [Next](ExpertID.md)

# IMTDeal::RateMargin

Gets the exchange rate of the margin currency of a deal to the client's deposit currency.

C++
    
    
    double  IMTDeal::RateMargin()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.RateMargin()

### Return Value

The exchange rate of the margin currency of a deal to the client's deposit currency.

# IMTDeal::RateMargin

Sets the exchange rate of the margin currency of a deal to the client's deposit currency.

C++
    
    
    MTAPIRES  IMTDeal::RateMargin(
       const double  rate      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.RateMargin(
       double        rate      // Margin ratio
       )

### Parameters

**rate**  
[in] The exchange rate of the margin currency of a deal to the client's deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
