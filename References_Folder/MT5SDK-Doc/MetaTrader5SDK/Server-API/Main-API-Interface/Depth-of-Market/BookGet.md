[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Depth of Market](../Depth-of-Market.md) / BookGet

[Previous](BookUnsubscribe.md) | [Next](../Mail-Database.md)

# IMTServerAPI::BookGet

Get a symbol's Depth of Market.
    
    
    MTAPIRES  IMTServerAPI::BookGet(
       LPCWSTR  symbol,     // Symbol
       MTBook&  book        // An array of DOM records
       )

### Parameters

**symbol**  
[in] [in] The symbol whose DOM you need to get.

**book**  
[out] An array of DOM records of typeMTBook.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

To get information about a symbol's DOM using the IMTServerAPI::BookGet method, it is necessary to subscribe to events of changes in the DOM of this symbol using the [IMTServerAPI::BookSubscribe](BookSubscribe.md) method.

This method can be used only on history servers.
