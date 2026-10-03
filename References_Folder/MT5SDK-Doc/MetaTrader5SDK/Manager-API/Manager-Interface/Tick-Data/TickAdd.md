[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickAdd

[Previous](TickUnsubscribe.md) | [Next](TickAddBatch.md)

# IMTManagerAPI::TickAdd

Add a quote into the price stream.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickAdd(
       LPCWSTR  symbol,     // Symbol
       MTTick&  tick        // Reference to the quote structure
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickAdd(
       srting   symbol,     // Symbol
       MTTick   tick        // Quote structure
       )

Python
    
    
    ManagerAPI.TickAdd(
       symbol,  # Symbol
       tick     # Quote structure
       )

### Parameters

**symbol**  
[in] The symbol, for which a quote is added. Obsolete parameter, its value is ignored. Can be filled with NULL.

**tick**  
[in] A reference to the structure that describes the tick (MTTick).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To execute this function, a manager must have appropriate rights, otherwise the [MT_RET_ERR_PERMISSIONS](../../../Return-Codes/Common-errors.md) error is returned.
