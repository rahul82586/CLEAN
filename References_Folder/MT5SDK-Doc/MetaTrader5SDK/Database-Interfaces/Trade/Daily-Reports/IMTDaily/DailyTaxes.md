[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyTaxes

[Previous](DailyDividend.md) | [Next](DailySOCompensation.md)

# IMTDaily::DailyTaxes

Get the amount of [taxes (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) withheld from the client's funds for the reported day.

C++
    
    
    double  IMTDaily::DailyTaxes()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyTaxes()

### Return Value

The amount of taxes withheld from the client for the reported day.

# IMTDaily::DailyTaxes

Set the amount of [taxes (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) withheld from the client's funds for the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyTaxes(
       const double  taxes     // daily taxes
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyTaxes(
       double        taxes     // daily taxes
       )

### Parameters

**taxes**  
[in] The amount of taxes withheld from the client for the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
