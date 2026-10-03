[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / CommissionMonthly

[Previous](CommissionDaily.md) | [Next](AgentDaily.md)

# IMTDaily::CommissionMonthly

Get the total amount of a client's [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) for the current month in a report.

C++
    
    
    double  IMTDaily::CommissionMonthly()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.CommissionMonthly()

### Return Value

The total amount of commissions charged from a client for the current month in a report.

# IMTDaily::CommissionMonthly

Set the total amount of a client's [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) for the current month in a report.

C++
    
    
    MTAPIRES  IMTDaily::CommissionMonthly(
       const double  comm      // Monthly commissions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.CommissionMonthly(
       double        comm      // Monthly commissions
       )

### Parameters

**comm**  
[in] The total amount of commissions charged from a client for the current month in a report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
