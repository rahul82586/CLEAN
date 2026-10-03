[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / InvestorAdd

[Previous](AccountNext.md) | [Next](InvestorUpdate.md)

# IMTConFund::InvestorAdd

Add an investor for a fund.

C++
    
    
    MTAPIRES  IMTConFund::InvestorAdd(
       IMTConFundInvestor*  investor    // Investor object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.InvestorAdd(
       CIMTConFundInvestor  investor    // Investor object
       )

### Parameters

**investor**  
[in]IMTConFundInvestorinvestor object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
