[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Tick Data](../Tick-Data.md) / TickAdd

[Previous](TickRequestRaw.md) | [Next](TickReplace.md)

# IMTAdminAPI::TickAdd

Add tick data for a symbol.

C++
    
    
    MTAPIRES  IMTAdminAPI::TickAdd(
       LPCWSTR             symbol,         // Symbol
       const MTTickShort*  ticks,          // Ticks to add
       const UINT          ticks_total     // The number of ticks to add
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.TickAdd(
       string              symbol,         // Symbol
       MTTickShort[]       ticks           // Ticks to add
       )

Python
    
    
    AdminAPI.TickAdd(
       symbol,             # Symbol
       ticks               # Ticks to add
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update historical data.

**ticks**  
[in] An array ofMTTickShortstructures describing ticks to be added.

**ticks_total**  
[in] The number of ticks to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Unlike [IMTManagerAPI::TickAdd](../../Manager-Interface/Tick-Data/TickAdd.md), this method directly adds quotes to the price history rather than adding them to the price stream.
