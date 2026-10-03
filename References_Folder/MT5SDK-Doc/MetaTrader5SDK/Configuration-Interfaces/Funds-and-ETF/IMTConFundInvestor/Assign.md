[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundInvestor](../IMTConFundInvestor.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConFundInvestor::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConFundInvestor::Assign(
       const IMTConFundInvestor*  investor  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFundInvestor.Assign(
       CIMTConFundInvestor        investor  // Source object
       )

### Parameters

**investor**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
