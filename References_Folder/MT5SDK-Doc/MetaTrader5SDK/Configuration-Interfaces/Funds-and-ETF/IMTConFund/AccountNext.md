[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / AccountNext

[Previous](AccountTotal.md) | [Next](InvestorAdd.md)

# IMTConFund::AccountNext

Get a fund manager by index.

C++
    
    
    MTAPIRES  IMTConFund::AccountNext(
       const UINT                 pos,       // Symbol position
       IMTConFundAccount*         account    // Manager object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.AccountNext(
       uint                       pos,       // Symbol position
       CIMTConFundAccount         account    // Manager object
       )

### Parameters

**pos**  
[in] Manager position in the list, starting at 0.

**account**  
[out]IMTConFundAccountmanager object. The 'account' object must be pre-created using theIMTReportAPI::FundAccountCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
