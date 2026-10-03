[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching PriceClient

[Previous](IMTHistoryMatching-Price.md) | [Next](IMTHistoryMatching-Digits.md)

# IMTECNHistoryMatching::PriceClient

Get the price specified in the original client order.

C++
    
    
    double  IMTECNHistoryMatching::PriceClient()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTECNHistoryMatching.PriceClient()

### Return Value

Price in the client order.

# IMTECNHistoryMatching::PriceClient

Set the price specified in the original client order.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::PriceClient(
       const double  price      // order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.PriceClient(
       double        price      // order price
       )

### Parameters

**price**  
[in] Price in the client order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
