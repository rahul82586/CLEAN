[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Price

[Previous](Flags.md) | [Next](PricePro.md)

# IMTConSubscription::Price

Get a subscription price for non-professional traders.

C++
    
    
    double  IMTConSubscription::Price()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSubscription.Price()

### Return Value

Subscription price.

### Note

The currency in which the price is specified, is determined by the [IMTConSubscription::PriceCurrency](PriceCurrency.md) property.

# IMTConSubscription::Price

Set a subscription price for non-professional traders.

C++
    
    
    MTAPIRES  IMTConSubscription::Price(
       const double      price  // Price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.Price(
       double            price  // Price
       )

### Parameters

**price**  
[in] Subscription price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

The currency in which the price is specified, is determined by the [IMTConSubscription::PriceCurrency](PriceCurrency.md) property.
