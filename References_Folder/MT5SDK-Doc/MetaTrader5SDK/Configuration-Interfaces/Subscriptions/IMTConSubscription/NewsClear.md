[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / NewsClear

[Previous](NewsDelete.md) | [Next](NewsShift.md)

# IMTConSubscription::NewsClear

Clear the list of news categories available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::NewsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.NewsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method deletes all news categories from the news list available by subscription.
