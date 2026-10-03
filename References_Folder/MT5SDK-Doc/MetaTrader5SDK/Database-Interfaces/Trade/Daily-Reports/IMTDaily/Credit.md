[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Credit

[Previous](Balance.md) | [Next](InterestRate.md)

# IMTDaily::Credit

Get the amount of a client's credit funds in a daily report.

C++
    
    
    double  IMTDaily::Credit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.Credit()

### Return Value

The amount of a client's credit funds in a daily report.

# IMTDaily::Credit

Set the amount of a client's credit funds in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Credit(
       const double  credit      // Credit funds
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Credit(
       double        credit      // Credit funds
       )

### Parameters

**credit**  
[in] The amount of a client's credit funds in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
