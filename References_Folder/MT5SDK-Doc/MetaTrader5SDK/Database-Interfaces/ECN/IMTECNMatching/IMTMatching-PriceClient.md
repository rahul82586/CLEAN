[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching PriceClient

[Previous](IMTMatching-Price.md) | [Next](IMTMatching-Digits.md)

# IMTECNMatching::PriceClient

Get the price specified in the original client order.

C++
    
    
    double  IMTECNMatching::PriceClient()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTECNMatching.PriceClient()

### Return Value

Price in the client order.

# IMTECNMatching::PriceClient

Set the price specified in the original client order.

C++
    
    
    MTAPIRES  IMTECNMatching::PriceClient(
       const double  price      // order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.PriceClient(
       double        price      // order price
       )

### Parameters

**price**  
[in] Price in the client order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
