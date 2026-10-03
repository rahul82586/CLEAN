[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Tick Data](../Tick-Data.md) / TickReplace

[Previous](TickAdd.md) | [Next](../Settings-Files.md)

# IMTAdminAPI::TickReplace

Full replacement of tick data in the specified period with the passed data.

C++
    
    
    MTAPIRES  IMTAdminAPI::TickReplace(
       LPCWSTR             symbol,        // Symbol
       const INT64         from_msc,      // Beginning of the period
       const INT64         to_msc,        // End of the period
       const MTTickShort*  ticks,         // New ticks
       const UINT          ticks_total    // Number of new ticks
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.TickReplace(
       string              symbol,        // Symbol
       long                from_msc,      // Beginning of the period
       long                to_msc,        // End of the period
       MTTickShort[]       ticks          // New ticks
       )

Python
    
    
    AdminAPI.TickReplace(
       symbol,             # Symbol
       from_msc,           # Beginning of the period
       to_msc,             # End of the period
       ticks               # New ticks
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update historical data.

**from_msc**  
[in] The beginning of the period for which you need to replace data. The date is specified in milliseconds that have elapsed since 01.01.1970.

**to_msc**  
[in] The date is specified in seconds that have elapsed since 01.01.1970. The date is specified in milliseconds that have elapsed since 01.01.1970.

**ticks**  
[in] An array ofMTTickShortstructures describing new ticks.

**ticks_total**  
[in] The number of ticks passed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method totally replaces the tick data in the specified time period with the data passed in the 'ticks' parameter.
