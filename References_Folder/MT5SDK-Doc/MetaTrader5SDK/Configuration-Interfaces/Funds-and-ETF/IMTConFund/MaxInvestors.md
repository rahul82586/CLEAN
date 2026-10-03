[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / MaxInvestors

[Previous](Currency.md) | [Next](FeeMode.md)

# IMTConFund::MaxInvestors

Get the maximum allowable number of investors who can purchase shares in the fund.

C++
    
    
    UINT  IMTConFund::MaxInvestors()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.MaxInvestors()

### Return Value

The maximum allowable number of investors.

# IMTConFund::MaxInvestors

Set the maximum allowable number of investors who can purchase shares in the fund.

C++
    
    
    MTAPIRES  IMTConFund::MaxInvestors(
       const UINT  max_investors   // Number of investors
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.MaxInvestors(
       uint        max_investors   // Number of investors
       )

### Parameters

**max_investors**  
[in] The maximum allowable number of investors.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
