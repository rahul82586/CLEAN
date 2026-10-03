[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / BalancePrevMonth

[Previous](BalancePrevDay.md) | [Next](EquityPrevDay.md)

# IMTDaily::BalancePrevMonth

Get the value of a client's balance as of the end of the previous trading month.

C++
    
    
    double  IMTDaily::BalancePrevMonth()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.BalancePrevMonth()

### Return Value

A client's balance as of the end of the previous trading month.

# IMTDaily::BalancePrevMonth

Set the value of a client's balance as of the end of the previous trading month.

C++
    
    
    MTAPIRES  IMTDaily::BalancePrevMonth(
       const double  balance      // Balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.BalancePrevMonth(
       double        balance      // Balance
       )

### Parameters

**balance**  
[in] A client's balance as of the end of the previous trading month.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
