[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / AccountUpdate

[Previous](AccountAdd.md) | [Next](AccountDelete.md)

# IMTConFund::AccountUpdate

Update a fund manager account.

C++
    
    
    MTAPIRES  IMTConFund::AccountUpdate(
       const UINT                pos,       // Manager position
       const IMTConFundAccount*  symbol     // Manager description
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.AccountUpdate(
       uint                      pos,       // Manager position
       CIMTConFundAccount        symbol     // Manager description
       )

### Parameters

**pos**  
[in] Position of a manager account in the list, starting at 0.

**news**  
[in] Symbol objectIMTConSubscriptionSymbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
