[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickAddStat

[Previous](TickAddBatch.md) | [Next](TickLast.md)

# IMTManagerAPI::TickAddStat

Add statistical information about the price.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickAddStat(
       MTTick&      tick,       // Reference to the structure of tick
       MTTickStat&  stat        // Reference to the structure of statistical information
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickAddStat(
       MTTick       tick,       // Quote structure
       MTTickStat   stat        // Statistical information structure
       )

Python
    
    
    ManagerAPI.TickAddStat(
       tick,        # Quote structure
       stat         # Statistical information structure
       )

### Parameters

**tick**  
[in] A reference to the structure that describes the tick (MTTick).

**stat**  
[in] A reference to the structure that describes statistical price information (MTTickStat).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To execute this function, a manager must have appropriate rights, otherwise the [MT_RET_ERR_PERMISSIONS](../../../Return-Codes/Common-errors.md) error is returned.
