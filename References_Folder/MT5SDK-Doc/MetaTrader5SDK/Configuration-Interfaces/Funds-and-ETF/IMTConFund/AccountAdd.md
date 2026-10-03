[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / AccountAdd

[Previous](StateCurrentCaptital.md) | [Next](AccountUpdate.md)

# IMTConSubscription::AccountAdd

Add a fund manager account.

C++
    
    
    MTAPIRES  IMTConSubscription::AccountAdd(
       IMTConFundAccount*  account    // Manager description
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.AccountAdd(
       CIMTConFundAccount  account    // Manager description
       )

### Parameters

**account**  
[in] TheIMTConFundAccountmanager account object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
