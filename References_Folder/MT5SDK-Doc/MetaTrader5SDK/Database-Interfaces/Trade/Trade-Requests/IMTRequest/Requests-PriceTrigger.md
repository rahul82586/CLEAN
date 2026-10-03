[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PriceTrigger

[Previous](Requests-PriceOrder.md) | [Next](Requests-PriceSL.md)

# IMTRequest::PriceTrigger

Get the price, at which a Limit order is placed when the Stop Limit order triggers.

C++
    
    
    double  IMTRequest::PriceTrigger()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTRequest.PriceTrigger()

### Return Value

The price, at which a Limit order is placed when the Stop Limit order triggers.

### Note

This method is used only when working with Stop Limit orders. The Stop Limit order trigger price is specified in [IMTRequest::PriceOrder](Requests-PriceOrder.md).

# IMTRequest::PriceTrigger

Set the price, at which a Limit order is placed when the Stop Limit order triggers.

C++
    
    
    MTAPIRES  IMTRequest::PriceTrigger(
       const double  price      // Triggering price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.PriceTrigger(
       double        price      // Triggering price
       )

### Parameters

**price**  
[in] Order triggering price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is used only when working with Stop Limit orders. The Stop Limit order trigger price is specified in [IMTRequest::PriceOrder](Requests-PriceOrder.md).
