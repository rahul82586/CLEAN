[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Depth of Market](../Depth-of-Market.md) / BookUnsubscribe

[Previous](BookSubscribe.md) | [Next](BookGet.md)

# IMTServerAPI::BookUnsubscribe

Unsubscribe from events associated with changes in the symbol's DOM.
    
    
    MTAPIRES  IMTServerAPI::BookUnsubscribe(
       IMTBookSink*  sink        // A pointer to the IMTBookSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTBookSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::BookSubscribe](BookSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
