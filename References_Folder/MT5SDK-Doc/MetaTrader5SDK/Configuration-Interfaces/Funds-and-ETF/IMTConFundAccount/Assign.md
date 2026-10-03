[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundAccount](../IMTConFundAccount.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConFundAccount::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConFundAccount::Assign(
       const IMTConFundAccount*  account  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Assign(
       CIMTConFundAccount        account  // Source object
       )

### Parameters

**account**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
