[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Digits

[Previous](IMTMatching-PriceClient.md) | [Next](IMTMatching-DigitsClient.md)

# IMTECNMatching::Digits

Get the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.

C++
    
    
    UINT  IMTECNMatching::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNMatching.Digits()

### Return Value

The number of decimal places in the symbol price

# IMTECNMatching::Digits

Set the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.

C++
    
    
    MTAPIRES  IMTECNMatching::Digits(
       const UINT    digits      // number of decimal places in the price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Digits(
       uint          digits      // number of decimal places in the price
       )

### Parameters

**digits**  
[in] The number of decimal places in the symbol price.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
