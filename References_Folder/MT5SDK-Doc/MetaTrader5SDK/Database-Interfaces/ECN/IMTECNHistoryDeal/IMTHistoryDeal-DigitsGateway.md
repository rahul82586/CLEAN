[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal DigitsGateway

[Previous](IMTHistoryDeal-Digits.md) | [Next](IMTHistoryDeal-Commission.md)

# IMTECNHistoryDeal::DigitsGateway

Get the number of decimal places in the price of the symbol, for which the deal was executed, on the external system side.

C++
    
    
    UINT  IMTECNHistoryDeal::DigitsGateway()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryDeal.DigitsGateway()

### Return Value

The number of decimal places in the symbol price

# IMTECNHistoryDeal::DigitsGateway

Set the number of decimal places in the price of the symbol, for which the deal was executed, on the external system side.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::DigitsGateway(
       const UINT    digits      // number of decimal places in the price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.DigitsGateway(
       uint          digits      // number of decimal places in the price
       )

### Parameters

**digits**  
[in] The number of decimal places in the symbol price.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
