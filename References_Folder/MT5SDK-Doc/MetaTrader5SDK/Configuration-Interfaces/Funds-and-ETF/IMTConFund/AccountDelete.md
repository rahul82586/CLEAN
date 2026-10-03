[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / AccountDelete

[Previous](AccountUpdate.md) | [Next](AccountClear.md)

# IMTConFund::AccountDelete

Delete a fund manager account.

C++
    
    
    MTAPIRES  IMTConFund::AccountDelete(
       const UINT  pos      // Manager position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.AccountDelete(
       uint        pos      // Manager position
       )

### Parameters

**pos**  
[in] Manager position in the list, starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
