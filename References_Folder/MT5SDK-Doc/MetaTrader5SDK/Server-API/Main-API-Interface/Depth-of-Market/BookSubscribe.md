[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Depth of Market](../Depth-of-Market.md) / BookSubscribe

[Previous](../Depth-of-Market.md) | [Next](BookUnsubscribe.md)

# IMTServerAPI::BookSubscribe

Subscribe to events associated with changes in the symbol's DOM.
    
    
    MTAPIRES  IMTServerAPI::BookSubscribe(
       IMTBookSink*  sink        // A pointer to the IMTBookSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTBookSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTBookSink](../../../Database-Interfaces/Depth-of-Market/IMTBookSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
