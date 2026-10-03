[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Digits

[Previous](IMTFilling-Price.md) | [Next](IMTFilling-Deviation.md)

# IMTECNFilling::Digits

Get the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.

C++
    
    
    UINT  IMTECNFilling::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNFilling.Digits()

### Return Value

The number of decimal places in the symbol price

# IMTECNFilling::Digits

Set the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.

C++
    
    
    MTAPIRES  IMTECNFilling::Digits(
       const UINT    digits      // number of decimal places in the price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Digits(
       uint          digits      // number of decimal places in the price
       )

### Parameters

**digits**  
[in] The number of decimal places in the symbol price.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
