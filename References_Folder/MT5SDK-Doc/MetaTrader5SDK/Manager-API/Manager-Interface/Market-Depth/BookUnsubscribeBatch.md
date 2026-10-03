[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Market Depth](../Market-Depth.md) / BookUnsubscribeBatch

[Previous](BookUnsubscribe.md) | [Next](BookGet.md)

# IMTManagerAPI::BookUnsubscribeBatch

Unsubscribe from events related to a change of the Market Depth of multiple symbols.

C++
    
    
    MTAPIRES  IMTManagerAPI::BookUnsubscribeBatch(
       LPWSTR*       symbols,        // Array of symbols
       UINT          symbols_total,  // Number of symbols
       IMTBookSink*  sink            // A pointer to the IMTBookSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.BookUnsubscribeBatch(
       array<String^>^  symbols,     // Array of symbols
       CIMTBookSink     sink         // CIMTBookSink object
       )

Python
    
    
    ManagerAPI.BookUnsubscribeBatch(
       symbols,         # Array of symbols
       sink             # IMTBookSink object
       )

### Parameters

**symbol**  
[in] An array of symbols, from which events you want to unsubscribe.

**symbols_total**  
[in] The number of elements in the 'symbols' array.

**sink**  
[in] A pointer to the object that implements theIMTBookSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTManagerAPI::BookSubscribeBatch](BookSubscribeBatch.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
