[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / RateMargin

[Previous](RateProfit.md) | [Next](ExpertID.md)

# IMTPosition::RateMargin

Get the exchange rate of the margin currency of a position to the client's deposit currency.

C++
    
    
    double  IMTPosition::RateMargin()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.RateMargin()

### Return Value

The exchange rate of the margin currency of a position to the client's deposit currency.

# IMTPosition::RateMargin

Set the exchange rate of the margin currency of a position to the client's deposit currency.

C++
    
    
    MTAPIRES  IMTPosition::RateMargin(
       const double  rate      // Margin ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.RateMargin(
       double        rate      // Margin ratio
       )

### Parameters

**rate**  
[in] The exchange rate of the margin currency of a position to the client's deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
