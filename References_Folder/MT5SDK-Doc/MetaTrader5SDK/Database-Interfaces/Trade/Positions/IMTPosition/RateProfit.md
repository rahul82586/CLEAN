[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / RateProfit

[Previous](Storage.md) | [Next](RateMargin.md)

# IMTPosition::RateProfit

Get the exchange rate of the profit currency of a position to the deposit currency of a client group.

C++
    
    
    double  IMTPosition::RateProfit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.RateProfit()

### Return Value

The exchange rate of the profit currency of a position to the deposit currency of a client group.

# IMTPosition::RateProfit

Set the exchange rate of the profit currency of a position to the deposit currency of a client group.

C++
    
    
    MTAPIRES  IMTPosition::RateProfit(
       const double  rate      // Profit ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.RateProfit(
       double        rate      // Profit ratio
       )

### Parameters

**rate**  
[in] The exchange rate of the profit currency of a position to the deposit currency of a client group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
