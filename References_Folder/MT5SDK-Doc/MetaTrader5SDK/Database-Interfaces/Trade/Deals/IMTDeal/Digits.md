[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Digits

[Previous](Entry.md) | [Next](DigitsCurrency.md)

# IMTDeal::Digits

Get the number of decimal places in the price of a deal.

C++
    
    
    UINT  IMTDeal::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDeal.Digits()

### Return Value

The number of decimal places in the price of a deal.

# IMTDeal::Digits

Set the number of decimal places in the price of a deal.

C++
    
    
    MTAPIRES  IMTDeal::Digits(
       const UINT  digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Digits(
       uint        digits      // Decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places in the price of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
