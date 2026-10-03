[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyDividend

[Previous](DailyCommFee.md) | [Next](DailyTaxes.md)

# IMTDaily::DailyDividend

Get the amount of [dividends (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) accrued to the client for a reported day.

C++
    
    
    double  IMTDaily::DailyDividend()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyDividend()

### Return Value

The amount of dividends accrued to the client for a reported day.

# IMTDaily::DailyDividend

Set the amount of [dividends (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) accrued to the client for a reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyDividend(
       const double  dividend  // daily dividends
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyDividend(
       double        dividend  // daily dividends
       )

### Parameters

**dividend**  
[in] The amount of dividends accrued to the client for a reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
