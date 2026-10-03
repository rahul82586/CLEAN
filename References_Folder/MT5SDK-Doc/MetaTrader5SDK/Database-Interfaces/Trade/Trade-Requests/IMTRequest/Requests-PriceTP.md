[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PriceTP

[Previous](Requests-PriceSL.md) | [Next](Requests-PriceDeviation.md)

# IMTRequest::PriceTP

Gets the Take Profit level in a trade request.

C++
    
    
    double  IMTRequest::PriceTP()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.PriceTP()

### Return Value

The Take Profit level in a trade request. The zero value means that the level is not set.

# IMTRequest::PriceTP

Sets the Take Profit level in a trade request.

C++
    
    
    MTAPIRES  IMTRequest::PriceTP(
       const double  price      // Take Profit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.PriceTP(
       double        price      // Take Profit
       )

### Parameters

**price**  
[in] The Take Profit level in a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The zero value means that the level is not set.
