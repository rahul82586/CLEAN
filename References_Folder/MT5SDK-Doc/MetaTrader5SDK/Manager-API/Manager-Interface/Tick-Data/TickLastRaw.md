[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickLastRaw

[Previous](TickLast.md) | [Next](TickStat.md)

# IMTManagerAPI::TickLastRaw

Get the last raw quote of a symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickLastRaw(
       LPCWSTR       symbol,     // Symbol
       MTTickShort&  tick        // Reference to the quote structure
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickLastRaw(
       string           symbol,  // Symbol
       out MTTickShort  tick     // Quote structure
       )

Python
    
    
    ManagerAPI.TickLastRaw(
       str              symbol   # Symbol
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get a quote.

**tick**  
[out] A reference to the structure describing the quote (MTTickShort).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

For this method to work, the manager account must have the [IMTConManager::RIGHT_QUOTES_RAW (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission enabled. If the permission is absent, the error [MT_RET_ERR_PERMISSIONS](../../../Return-Codes/Common-errors.md) is returned.
