[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / AccountClear

[Previous](AccountDelete.md) | [Next](AccountShift.md)

# IMTConFund::AccountClear

Clear the list of fund managers.

C++
    
    
    MTAPIRES  IMTConFund::AccountClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.AccountClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method removes all managers from the fund.
