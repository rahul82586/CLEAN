[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / CommissionDaily

[Previous](InterestRate.md) | [Next](CommissionMonthly.md)

# IMTDaily::CommissionDaily

Get the amount of a client's [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) for a day in the report.

C++
    
    
    double  IMTDaily::CommissionDaily()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.CommissionDaily()

### Return Value

The amount of commissions charged from a client for a day in the report.

# IMTDaily::CommissionDaily

Set the amount of a client's [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) for a day in the report.

C++
    
    
    MTAPIRES  IMTDaily::CommissionDaily(
       const double  comm      // Daily commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.CommissionDaily(
       double        comm      // Daily commission
       )

### Parameters

**comm**  
[in] The amount of commissions charged from a client for a day in the report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
