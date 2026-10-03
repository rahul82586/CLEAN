[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / InvestorClear

[Previous](InvestorDelete.md) | [Next](InvestorShift.md)

# IMTConFund::InvestorClear

Clear the list of fund investors.

C++
    
    
    MTAPIRES  IMTConFund::InvestorClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.InvestorClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method removes all investors from the fund.
