[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / BalancePrevDay

[Previous](AgentMonthly.md) | [Next](BalancePrevMonth.md)

# IMTDaily::BalancePrevDay

Get the value of a client's balance as of the end of the previous day.

C++
    
    
    double  IMTDaily::BalancePrevDay()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.BalancePrevDay()

### Return Value

A client's balance as of the end of the previous day.

# IMTDaily::BalancePrevDay

Set the value of a client's balance as of the end of the previous day.

C++
    
    
    MTAPIRES  IMTDaily::BalancePrevDay(
       const double  balance      // Balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.BalancePrevDay(
       double        balance      // Balance
       )

### Parameters

**balance**  
[in] A client's balance as of the end of the previous day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
