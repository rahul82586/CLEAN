[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / PricePro

[Previous](Price.md) | [Next](PriceCost.md)

# IMTConSubscription::PricePro

Get a subscription price for professional traders.

C++
    
    
    double  IMTConSubscription::PricePro()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSubscription.PricePro()

### Return Value

Subscription price.

### Note

Professional traders include legal entities, banks, brokers, etc.

# IMTConSubscription::PricePro

Set a subscription price for professional traders.

C++
    
    
    MTAPIRES  IMTConSubscription::PricePro(
       const double      price  // Price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.PricePro(
       double            price  // Price
       )

### Parameters

**price**  
[in] Subscription price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

Professional traders include legal entities, banks, brokers, etc.
