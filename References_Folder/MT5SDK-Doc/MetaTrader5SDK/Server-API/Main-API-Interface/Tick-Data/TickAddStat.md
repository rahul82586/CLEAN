[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Tick Data](../Tick-Data.md) / TickAddStat

[Previous](TickAddBatch.md) | [Next](TickLast.md)

# IMTServerAPI::TickAddStat

Add statistical information about the price.
    
    
    MTAPIRES  IMTServerAPI::TickAddStat(
       MTTick&      tick,       // A pointer to the quote structure
       MTTickStat&  stat        // A pointer to the structure of statistical information
       )

### Parameters

**tick**  
[in] A pointer to theMTTickstructure that describes the quote.

**stat**  
[in] A pointer to the structure that describes statistical price information (MTTickStat).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method works only in plugins that run on history servers. If trying to run the command on another server, the [MT_RET_ERR_NOTSUPPORTED](../../../Return-Codes/API.md) error will be returned.
