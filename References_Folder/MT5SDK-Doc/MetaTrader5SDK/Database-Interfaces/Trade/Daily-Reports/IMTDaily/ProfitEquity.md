[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / ProfitEquity

[Previous](ProfitCommission.md) | [Next](ProfitAssets.md)

# IMTDaily::ProfitEquity

Get the amount of the current floating equity of a client in a daily report.

C++
    
    
    double  IMTDaily::ProfitEquity()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.ProfitEquity()

### Return Value

The amount of a client's floating equity in a daily report.

# IMTDaily::ProfitEquity

Set the amount of the current floating equity of a client in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::ProfitEquity(
       const double  equity      // Equity
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.ProfitEquity(
       double        equity      // Equity
       )

### Parameters

**equity**  
[in] The amount of the current floating equity of a client in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
