[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PriceOrder

[Previous](Requests-OrderExternalID.md) | [Next](Requests-PriceTrigger.md)

# IMTRequest::PriceOrder

Get the price of an order in a trade request.

C++
    
    
    double  IMTRequest::PriceOrder()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.PriceOrder()

### Return Value

The price of an order in a trade request.

# IMTRequest::PriceOrder

Set the price of an order in a trade request.

C++
    
    
    MTAPIRES  IMTRequest::PriceOrder(
       const double  price      // Order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.PriceOrder(
       double        price      // Order price
       )

### Parameters

**price**  
[in] The price of an order in a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
