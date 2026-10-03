[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / EquityPrevMonth

[Previous](EquityPrevDay.md) | [Next](Margin.md)

# IMTDaily::EquityPrevMonth

Get the value of a client's equity as of the end of the previous trading month.

C++
    
    
    double  IMTDaily::EquityPrevMonth()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.EquityPrevMonth()

### Return Value

The value of a client's equity as of the end of the previous trading month.

# IMTDaily::EquityPrevMonth

Set the value of a client's equity as of the end of the previous trading month.

C++
    
    
    MTAPIRES  IMTDaily::EquityPrevMonth(
       const double  balance      // Equity
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.EquityPrevMonth(
       double        balance      // Equity
       )

### Parameters

**balance**  
[in] A client's equity as of the end of the previous trading month..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
