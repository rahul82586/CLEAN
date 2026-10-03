[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / InvestorUpdate

[Previous](InvestorAdd.md) | [Next](InvestorDelete.md)

# IMTConFund::InvestorUpdate

Edit a fund investor.

C++
    
    
    MTAPIRES  IMTConFund::InvestorUpdate(
       const UINT                 pos,       // Symbol position
       const IMTConFundInvestor*  investor   // Investor object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.InvestorUpdate(
       uint                       pos,       // Symbol position
       CIMTConFundInvestor        investor   // Investor object
       )

### Parameters

**pos**  
[in] Investor position in the list, starting with 0.

**news**  
[in]IMTConFundInvestorinvestor object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
