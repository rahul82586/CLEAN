[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Market Depth](../Market-Depth.md) / BookSubscribeBatch

[Previous](BookSubscribe.md) | [Next](BookUnsubscribe.md)

# IMTManagerAPI::BookSubscribeBatch

Subscribe to events related to a change of the Market Depth of multiple symbols.

C++
    
    
    MTAPIRES  IMTManagerAPI::BookSubscribeBatch(
       LPWSTR*       symbols,        // Array of symbols
       UINT          symbols_total,  // Number of symbols
       IMTBookSink*  sink            // A pointer to the IMTBookSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.BookSubscribeBatch(
       array<String^>^  symbols,     // Array of symbols
       CIMTBookSink     sink         // CIMTBookSink object
       )

Python
    
    
    ManagerAPI.BookSubscribeBatch(
       symbols,         # Array of symbols
       sink             # IMTBookSink object
       )

### Parameters

**symbol**  
[in] An array of symbols, to which events you want to subscribe.

**symbols_total**  
[in] The number of elements in the 'symbols' array.

**sink**  
[in] A pointer to the object that implements theIMTBookSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. The same [IMTBookSink](../../../Database-Interfaces/Depth-of-Market/IMTBookSink.md) interface cannot subscribe to an event twice: in this case the [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) response code is returned.
