[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailySOCompensation

[Previous](DailyTaxes.md) | [Next](DailySOCompensationCredit.md)

# IMTDaily::DailySOCompensation

Get the amount of [negative balance compensation (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) accrued to the client for a reported day.

C++
    
    
    double  IMTDaily::DailySOCompensation()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailySOCompensation()

### Return Value

The amount of negative balance compensation accrued to the client for a reported day.

# IMTDaily::DailySOCompensation

Set the amount of [negative balance compensation (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) accrued to the client for a reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailySOCompensation(
       const double  socompensation  // daily compensation
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailySOCompensation(
       double        socompensation  // daily compensation
       )

### Parameters

**socompensation**  
[in] The amount of negative balance compensation accrued to the client for a reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
