[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyInterest

[Previous](DailyAgent.md) | [Next](PositionAdd.md)

# IMTDaily::DailyInterest

Get the amount accrued to a client as part of the annual interest rate for the reported day.

C++
    
    
    double  IMTDaily::DailyInterest()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyInterest()

### Return Value

The amount accrued to a client as part of the annual interest rate for the reported day.

# IMTDaily::DailyInterest

Set the amount accrued to a client as part of the annual interest rate for the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyInterest(
       const double  interest      // Daily charges at an annual interest rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyInterest(
       double        interest      // Daily charges at an annual interest rate
       )

### Parameters

**interest**  
[in] The amount accrued to a client as part of the annual interest rate for the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
