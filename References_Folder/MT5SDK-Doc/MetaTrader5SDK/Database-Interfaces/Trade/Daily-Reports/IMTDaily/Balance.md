[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Balance

[Previous](EMail.md) | [Next](Credit.md)

# IMTDaily::Balance

Get the size of a client's balance in a daily report.

C++
    
    
    double  IMTDaily::Balance()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.Balance()

### Return Value

The size of a client's balance in a daily report.

# IMTDaily::Balance

Set the size of a client's balance in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Balance(
       const double  balance      // Balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Balance(
       double        balance      // Balance
       )

### Parameters

**balance**  
[in] A client's balance in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
