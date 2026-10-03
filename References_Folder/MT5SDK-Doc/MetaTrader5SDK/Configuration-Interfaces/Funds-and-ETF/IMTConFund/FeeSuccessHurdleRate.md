[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeSuccessHurdleRate

[Previous](FeeSuccessHWM.md) | [Next](StateCurrentInvestors.md)

# IMTConFund::FeeSuccessHurdleRate

Get the hurdle rate.

C++
    
    
    double  IMTConFund::FeeSuccessHurdleRate()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConFund.FeeSuccessHurdleRate()

### Return Value

Hurdle rate as an annual percentage.

# IMTConFund::FeeSuccessHurdleRate

Set the hurdle rate.

C++
    
    
    MTAPIRES  IMTConFund::FeeSuccessHurdleRate(
       const double  rate       // Hurdle rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeSuccessHurdleRate(
       double        rate       // Hurdle rate
       )

### Parameters

**rate**  
[in] Hurdle rate as an annual percentage.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
