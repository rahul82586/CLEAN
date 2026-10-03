[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / StartDate

[Previous](Recalculation.md) | [Next](EndDate.md)

# IMTConFund::StartDate

Get the fund operation start date.

C++
    
    
    INT64  IMTConFund::StartDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConFund.StartDate()

### Return Value

Fund operation start date, in seconds that have elapsed since 01.01.1970.

# IMTConFund::StartDate

Set the fund operation start date.

C++
    
    
    MTAPIRES  IMTConFund::StartDate(
       const INT64  date      // Operation start
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.StartDate(
       long         date      // Operation start
       )

### Parameters

**time**  
[in] Fund operation start date, in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
