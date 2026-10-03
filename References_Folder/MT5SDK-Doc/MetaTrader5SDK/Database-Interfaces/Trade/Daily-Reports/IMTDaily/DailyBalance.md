[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyBalance

[Previous](DailyProfit.md) | [Next](DailyCredit.md)

# IMTDaily::DailyBalance

Get the amount accrued to a client's balance during the reported day.

C++
    
    
    double  IMTDaily::DailyBalance()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyBalance()

### Return Value

The amount accrued to a client's balance during the reported day.

# IMTDaily::DailyBalance

Set the amount accrued to a client's balance during the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyBalance(
       const double  balance      // Daily balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyBalance(
       double        balance      // Daily balance
       )

### Parameters

**balance**  
[in] The amount accrued to a client's balance during the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
