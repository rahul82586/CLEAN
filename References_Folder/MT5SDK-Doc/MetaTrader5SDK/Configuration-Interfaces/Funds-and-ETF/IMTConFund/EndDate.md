[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / EndDate

[Previous](StartDate.md) | [Next](MaxCapital.md)

# IMTConFund::EndDate

Get the fund operation end date.

C++
    
    
    INT64  IMTConFund::EndDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConFund.EndDate()

### Return Value

Fund operation end date, in seconds that have elapsed since 01.01.1970.

# IMTConFund::EndDate

Set the fund operation end date.

C++
    
    
    MTAPIRES  IMTConFund::EndDate(
       const INT64  date      // Operation end
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.EndDate(
       long         date      // Operation end
       )

### Parameters

**time**  
[in] Fund operation end date, in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
