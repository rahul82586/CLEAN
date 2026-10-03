[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyAgent

[Previous](DailySOCompensationCredit.md) | [Next](DailyInterest.md)

# IMTDaily::DailyAgent

Get the amount of agent [commission](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged for a client's trade operations for a reported day.

C++
    
    
    double  IMTDaily::DailyAgent()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyAgent()

### Return Value

The size of agent commissions charged for a client's trade operations for a reported day.

# IMTDaily::DailyAgent

Set the amount of agent [commission](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged for a client's trade operations for a reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyAgent(
       const double  comm      // Agent commissions for a day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyAgent(
       double        comm      // Agent commissions for a day
       )

### Parameters

**comm**  
[in] The size of agent commissions charged for a client's trade operations for a reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
