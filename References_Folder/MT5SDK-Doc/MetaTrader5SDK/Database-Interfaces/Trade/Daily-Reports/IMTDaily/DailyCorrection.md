[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyCorrection

[Previous](DailyCharge.md) | [Next](DailyBonus.md)

# IMTDaily::DailyCorrection

Get the amount of corrective balance operations for a reported day.

C++
    
    
    double  IMTDaily::DailyCorrection()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyCorrection()

### Return Value

The amount of corrective balance operations for a reported day.

# IMTDaily::DailyCorrection

Set the amount of corrective balance operations for a reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyCorrection(
       const double  correction      // Corrective operations for a day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyCorrection(
       double        correction      // Corrective operations for a day
       )

### Parameters

**correction**  
[in] The amount of corrective balance operations for a reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
