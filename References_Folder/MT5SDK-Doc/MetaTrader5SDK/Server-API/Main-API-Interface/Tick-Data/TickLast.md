[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Tick Data](../Tick-Data.md) / TickLast

[Previous](TickAddStat.md) | [Next](TickStat.md)

# IMTServerAPI::TickLast

For the last raw (not processed in accordance with the symbol settings) quote for the specified symbol.
    
    
    MTAPIRES  IMTServerAPI::TickLast(
       LPCWSTR       symbol,     // Symbol
       MTTickShort&  tick        // A pointer to the quote structure
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get a quote.

**tick**  
[out] A pointer to the structure describing the quote (MTTickShort).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# IMTServerAPI::TickLast

Get the last quote for the specified symbol processed in accordance with its settings for a certain group.
    
    
    MTAPIRES  IMTServerAPI::TickLast(
       const IMTConSymbol*  symbol,     // An object of the symbol configuration
       MTTickShort&         tick        // A pointer to the quote structure
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration. The symbol object must be first created using theIMTServerAPPI::SymbolCreatemethod.

**tick**  
[out] A pointer to the structure describing the quote (MTTickShort).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method does not work on history servers, because they do not have access to the user [group](../../../Configuration-Interfaces/Groups.md) settings. If you try to run it on a history server, the [MT_RET_ERR_NOTSUPPORTED](../../../Return-Codes/API.md) error will be returned.

### Example
    
    
    void GetCurrentTicks(LPCWSTR group_name,LPCWSTR symbol_name,MTTickShort& tick)
      {
       IMTConGroup *group=api->GroupCreate();
       api->GroupGet(group_name);
    //---  
       IMTConSymbol *symbol=api->SymbolCreate();
       api->SymbolGet(symbol_name,group,symbol);
    //---
       api->TickLast(symbol,tick);
      }
