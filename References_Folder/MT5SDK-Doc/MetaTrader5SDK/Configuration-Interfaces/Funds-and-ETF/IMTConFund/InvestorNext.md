[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / InvestorNext

[Previous](InvestorTotal.md) | [Next](../IMTConFundAccount.md)

# IMTConFund::InvestorNext

Get a fund investor by index.

C++
    
    
    MTAPIRES  IMTConFund::InvestorNext(
       const UINT                 pos,       // Investor position
       IMTConFundInvestor*        investor   // Investor object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.InvestorNext(
       uint                       pos,       // Investor position
       CIMTConFundInvestor        investor   // Investor object
       )

### Parameters

**pos**  
[in] Investor position in the list, starting with 0.

**investor**  
[out] Investor objectIMTConFundInvestor. The investor object must be previously created using theIMTReportAPI::FundInvestorCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
