[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscriptionNews](../IMTConSubscriptionNews.md) / Category

[Previous](Clear.md) | [Next](Language.md)

# IMTConSubscriptionNews::Category

Get news categories available by subscription.

C++
    
    
    LPCWSTR  IMTConSubscriptionNews::Category()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscriptionNews.Category()

### Return Value

If successful, it returns a pointer to a string with the news category. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSubscriptionNews](../IMTConSubscriptionSymbol.md) object.

# IMTConSubscriptionNews::Category

Set news categories available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscriptionNews::Category(
       LPCWSTR  category      // Categories
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscriptionNews.Category(
       string   category      // Categories
       )

### Parameters

**category**  
[in] News category.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

Categories are used for filtering news into [groups](../../Groups.md), and for easy viewing of news in terminals.
