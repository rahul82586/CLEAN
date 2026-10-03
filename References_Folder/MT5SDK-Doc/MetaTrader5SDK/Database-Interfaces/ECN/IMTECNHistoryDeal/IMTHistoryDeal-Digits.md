[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Digits

[Previous](IMTHistoryDeal-PriceGateway.md) | [Next](IMTHistoryDeal-DigitsGateway.md)

# IMTECNHistoryDeal::Digits

Get the number of decimal places in the price of the symbol, for which the deal was executed, on the trading platform side.

C++
    
    
    UINT  IMTECNHistoryDeal::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryDeal.Digits()

### Return Value

The number of decimal places in the symbol price

# IMTECNHistoryDeal::Digits

Set the number of decimal places in the price of the symbol, for which the deal was executed, on the trading platform side.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Digits(
       const UINT    digits      // number of decimal places in the price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Digits(
       uint          digits      // number of decimal places in the price
       )

### Parameters

**digits**  
[in] The number of decimal places in the symbol price.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
