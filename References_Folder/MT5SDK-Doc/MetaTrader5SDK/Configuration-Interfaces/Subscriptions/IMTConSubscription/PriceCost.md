[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / PriceCost

[Previous](PricePro.md) | [Next](PriceCurrency.md)

# IMTConSubscription::PriceCost

Get a subscription cost.

C++
    
    
    double  IMTConSubscription::PriceCost()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSubscription.PriceCost()

### Return Value

Subscription cost.

### Note

The currency in which the price is specified, is determined by the [IMTConSubscription::PriceCurrency](PriceCurrency.md) property.

# IMTConSubscription::PriceCost

Set a subscription cost.

C++
    
    
    MTAPIRES  IMTConSubscription::PriceCost(
       const double      price  // Price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.PriceCost(
       double            price  // Price
       )

### Parameters

**price**  
[in] Subscription cost.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The currency in which the price is specified, is determined by the [IMTConSubscription::PriceCurrency](PriceCurrency.md) property.
