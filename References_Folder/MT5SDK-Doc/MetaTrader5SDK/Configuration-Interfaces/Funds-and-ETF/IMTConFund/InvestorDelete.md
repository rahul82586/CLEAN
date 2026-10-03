[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / InvestorDelete

[Previous](InvestorUpdate.md) | [Next](InvestorClear.md)

# IMTConFund::InvestorDelete

Delete an investor from the fund.

C++
    
    
    MTAPIRES  IMTConFund::InvestorDelete(
       const UINT  pos      // Investor position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.InvestorDelete(
       uint        pos      // Investor position
       )

### Parameters

**pos**  
[in] Investor position in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
