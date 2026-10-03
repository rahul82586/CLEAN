[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching DigitsClient

[Previous](IMTMatching-Digits.md) | [Next](IMTMatching-VolumeInitialExt.md)

# IMTECNMatching::DigitsClient

Get the number of decimal places in the price of the symbol, for which an order is placed on the client side.

C++
    
    
    UINT  IMTECNMatching::DigitsClient()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNMatching.DigitsClient()

### Return Value

The number of decimal places in the symbol price

# IMTECNMatching::DigitsClient

Set the number of decimal places in the price of the symbol, for which an order is placed on the client side.

C++
    
    
    MTAPIRES  IMTECNMatching::DigitsClient(
       const UINT    digits      // number of decimal places in the price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.DigitsClient(
       uint          digits      // number of decimal places in the price
       )

### Parameters

**digits**  
[in] The number of decimal places in the symbol price.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
