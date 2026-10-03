[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SubscriptionsDelay

[Previous](FilterGapTicks.md) | [Next](TradeMode.md)

# IMTConSymbol::SubscriptionsDelay

Get the delay for the quotes provided by [subscription](../../Subscriptions/IMTConSubscription.md).

C++
    
    
    UINT  IMTConSymbol::SubscriptionsDelay()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.SubscriptionsDelay()

Python (Manager API)
    
    
    MTConSymbol.SubscriptionsDelay

### Return Value

Delay in minutes.

### Note

For details please see the [MetaTrader 5 Administrator Help (#delayed)](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol#delayed).

# IMTConSymbol::SubscriptionsDelay

Set the delay for the quotes provided by [subscription](../../Subscriptions/IMTConSubscription.md).

C++
    
    
    MTAPIRES  IMTConSymbol::SubscriptionsDelay(
       const UINT  delay   // Delay
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SubscriptionsDelay(
       uint        delay   // Delay
       )

Python (Manager API)
    
    
    MTConSymbol.SubscriptionsDelay

### Parameters

**delay**  
[in] Delay in minutes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A restart of the access servers is required for new delay settings to take effect.
