[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / EquityPrevDay

[Previous](BalancePrevMonth.md) | [Next](EquityPrevMonth.md)

# IMTDaily::EquityPrevDay

Get the value of a client's equity as of the end of the previous day.

C++
    
    
    double  IMTDaily::EquityPrevDay()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.EquityPrevDay()

### Return Value

A client's equity as of the end of the previous day.

# IMTDaily::EquityPrevDay

Set the value of a client's equity as of the end of the previous day.

C++
    
    
    MTAPIRES  IMTDaily::EquityPrevDay(
       const double  balance      Equity
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.EquityPrevDay(
       double        balance      Equity
       )

### Parameters

**balance**  
[in] The client's equity as of the end of the previous day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
