[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / DigitsCurrency

[Previous](Digits.md) | [Next](ContractSize.md)

# IMTDeal::DigitsCurrency

Get the number of decimal places the deposit currency of the client who has executed the deal.

C++
    
    
    UINT  IMTDeal::DigitsCurrency()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDeal.DigitsCurrency()

### Return Value

The number of decimal places the deposit currency of the client who has executed the deal.

# IMTDeal::DigitsCurrency

Set the number of decimal places the deposit currency of the client who has executed the deal.

C++
    
    
    MTAPIRES  IMTDeal::DigitsCurrency(
       const UINT  digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.DigitsCurrency(
       uint        digits      // Decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places the deposit currency of the client who has executed the deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
