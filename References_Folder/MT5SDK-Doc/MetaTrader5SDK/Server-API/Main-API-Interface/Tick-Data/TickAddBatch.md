[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Tick Data](../Tick-Data.md) / TickAddBatch

[Previous](TickAdd.md) | [Next](TickAddStat.md)

# IMTServerAPI::TickAddBatch

Add multiple quotes into the price stream.
    
    
    MTAPIRES  IMTServerAPI::TickAddBatch(
       MTTick*      ticks,   // An array of quotes
       ticks_total  tick     // The number of quotes
       )

### Parameters

**ticks**  
[in] An array ofMTTickobjects describing quotes.

**tick**  
[in] The number of quotes in the 'ticks' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method works only in plugins running on history servers. An attempt to run the command on another server will cause the [MT_RET_ERR_NOTSUPPORTED](../../../Return-Codes/API.md) error to be returned.
