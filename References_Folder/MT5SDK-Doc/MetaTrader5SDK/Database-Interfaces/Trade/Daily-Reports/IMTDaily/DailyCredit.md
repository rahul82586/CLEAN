[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyCredit

[Previous](DailyBalance.md) | [Next](DailyCharge.md)

# IMTDaily::DailyCredit

Gets the amount of credit given to a client during the reported day.

C++
    
    
    double  IMTDaily::DailyCredit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyCredit()

### Return Value

The amount of credit given to a client during the reported day.

# IMTDaily::DailyCredit

Set the amount of credit given to a client during the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyCredit(
       const double  comm      // Credit for a day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyCredit(
       double        comm      // Credit for a day
       )

### Parameters

**comm**  
[in] The amount of credit given to a client during the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
