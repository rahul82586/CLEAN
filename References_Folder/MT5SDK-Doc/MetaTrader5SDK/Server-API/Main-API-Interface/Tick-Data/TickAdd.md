[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Tick Data](../Tick-Data.md) / TickAdd

[Previous](TickUnsubscribe.md) | [Next](TickAddBatch.md)

# IMTServerAPI::TickAdd

Add a quote into the price stream.
    
    
    MTAPIRES  IMTServerAPI::TickAdd(
       MTTick&  tick        // A pointer to the quote structure
       )

### Parameters

**tick**  
[in] A pointer to theMTTickstructure that describes the quote.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method works only in plugins that run on history servers. If trying to run the command on another server, the [MT_RET_ERR_NOTSUPPORTED](../../../Return-Codes/API.md) error will be returned.
