[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickAddBatch

[Previous](TickAdd.md) | [Next](TickAddStat.md)

# IMTManagerAPI::TickAddBatch

Add multiple quotes into the price stream.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickAddBatch(
       MTTick*      ticks,   // An array of quotes
       ticks_total  tick     // The number of quotes
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickAddBatch(
       MTTick[]     ticks    // An array of quotes
       )

Python
    
    
    ManagerAPI.TickAddBatch(
       ticks        # An array of quotes
       )

### Parameters

**ticks**  
[in] An array ofMTTickobjects describing quotes.

**tick**  
[in] The number of quotes in the 'ticks' array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To execute the function, the manager must have the appropriate permission; otherwise the [MT_RET_ERR_PERMISSIONS](../../../Return-Codes/Common-errors.md) error will be returned.
