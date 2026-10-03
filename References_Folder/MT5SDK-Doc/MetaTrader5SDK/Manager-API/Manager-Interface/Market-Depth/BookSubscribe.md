[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Market Depth](../Market-Depth.md) / BookSubscribe

[Previous](../Market-Depth.md) | [Next](BookSubscribeBatch.md)

# IMTManagerAPI::BookSubscribe

Subscribe to events associated with changes in the symbol's DOM.

C++
    
    
    MTAPIRES  IMTManagerAPI::BookSubscribe(
       LPCWSTR       symbol,     // Symbol
       IMTBookSink*  sink        // A pointer to the IMTBookSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.BookSubscribe(
       string        symbol,     // Symbol
       CIMTBookSink  sink        // CIMTBookSink object
       )

Python
    
    
    ManagerAPI.BookSubscribe(
       symbol,       # Symbol
       sink          # IMTBookSink object
       )

### Parameters

**news**  
[in] The symbol for which your subscribe.

**sink**  
[in] A pointer to the object that implements theIMTBookSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTBookSink](../../../Database-Interfaces/Depth-of-Market/IMTBookSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
