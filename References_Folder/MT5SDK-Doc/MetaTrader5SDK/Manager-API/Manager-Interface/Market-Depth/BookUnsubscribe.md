[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Market Depth](../Market-Depth.md) / BookUnsubscribe

[Previous](BookSubscribeBatch.md) | [Next](BookUnsubscribeBatch.md)

# IMTManagerAPI::BookUnsubscribe

Unsubscribe from events associated with changes in the symbol's DOM.

C++
    
    
    MTAPIRES  IMTManagerAPI::BookUnsubscribe(
       LPCWSTR       symbol,     // Symbol
       IMTBookSink*  sink        // A pointer to the IMTBookSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.BookUnsubscribe(
       string        symbol,     // Symbol
       CIMTBookSink  sink        // CIMTBookSink object
       )

Python
    
    
    ManagerAPI.BookUnsubscribe(
       symbol,       # Symbol
       sink          # IMTBookSink object
       )

### Parameters

**symbol**  
[in] The symbol from which your unsubscribe.

**sink**  
[in] A pointer to the object that implements theIMTBookSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::BookSubscribe](BookSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
