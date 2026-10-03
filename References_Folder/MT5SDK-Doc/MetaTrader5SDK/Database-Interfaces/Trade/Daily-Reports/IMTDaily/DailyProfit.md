[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyProfit

[Previous](ProfitLiabilities.md) | [Next](DailyBalance.md)

# IMTDaily::DailyProfit

Get the amount of a client's daily profit.

C++
    
    
    double  IMTDaily::DailyProfit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyProfit()

### Return Value

The amount of a client's daily profit.

# IMTDaily::DailyProfit

Set the amount of a client's daily profit.

C++
    
    
    MTAPIRES  IMTDaily::DailyProfit(
       const double  profit      // Daily profit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyProfit(
       double        profit      // Daily profit
       )

### Parameters

**profit**  
[in] The amount of a client's daily profit.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
