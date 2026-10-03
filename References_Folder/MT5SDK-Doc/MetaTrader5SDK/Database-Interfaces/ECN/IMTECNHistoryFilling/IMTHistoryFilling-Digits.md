[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Digits

[Previous](IMTHistoryFilling-Price.md) | [Next](IMTHistoryFilling-Deviation.md)

# IMTECNHistoryFilling::Digits

Get the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.

C++
    
    
    UINT  IMTECNHistoryFilling::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryFilling.Digits()

### Return Value

The number of decimal places in the symbol price

# IMTECNHistoryFilling::Digits

Set the number of decimal places in the price of the symbol, for which an order is placed on the ECN side.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Digits(
       const UINT    digits      // number of decimal places in the price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Digits(
       uint          digits      // number of decimal places in the price
       )

### Parameters

**digits**  
[in] The number of decimal places in the symbol price.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
