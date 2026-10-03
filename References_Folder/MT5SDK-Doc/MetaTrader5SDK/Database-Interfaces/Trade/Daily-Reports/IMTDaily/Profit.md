[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Profit

[Previous](MarginLeverage.md) | [Next](ProfitStorage.md)

# IMTDaily::Profit

Get the size of the current profit for all open positions of a client in a daily report.

C++
    
    
    double  IMTDaily::Profit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.Profit()

### Return Value

The size of the current profit for all open positions of a client in a daily report.

# IMTDaily::Profit

Set the size of the current profit for all open positions of a client in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Profit(
       const double  profit      // Profit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Profit(
       double        profit      // Profit
       )

### Parameters

**profit**  
[in] The size of the current profit for all open positions of a client in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
