[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Market Depth](../Market-Depth.md) / BookGet

[Previous](BookUnsubscribeBatch.md) | [Next](../Summary-Positions.md)

# IMTManagerAPI::BookGet

Get a symbol's Depth of Market.

C++
    
    
    MTAPIRES  IMTManagerAPI::BookGet(
       LPCWSTR     symbol,     // Symbol
       MTBook&     book        // An array of DOM records
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.BookGet(
       string      symbol,    // Symbol
       out MTBook  res        // An array of DOM records
       )

Python
    
    
    ManagerAPI.BookGet(
       symbol      # Symbol
       )

### Parameters

**symbol**  
[in] [in] The symbol whose DOM you need to get.

**book**  
[out] An array of DOM records of typeMTBook.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

To get information about a symbol's DOM using the IMTManagerAPI::BookGet method, it is necessary to subscribe to events of changes in the DOM of this symbol using the [IMTManagerAPI::BookSubscribe](BookSubscribe.md) method.
