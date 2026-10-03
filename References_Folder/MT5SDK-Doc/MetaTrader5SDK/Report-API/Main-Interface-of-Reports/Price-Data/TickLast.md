[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Price Data](../Price-Data.md) / TickLast

[Previous](TickGet.md) | [Next](TickStat.md)

# IMTReportAPI::TickLast

Get the last raw (not processed in accordance with the symbol settings) quote for the specified symbol.
    
    
    MTAPIRES  IMTReportAPI::TickLast(
       LPCWSTR       symbol,     // Symbol
       MTTickShort&  tick        // Pointer to a tick structure
       )

### Parameters

**symbol**  
[in] The symbol, for which you need to get a quote.

**tick**  
[out] A pointer to the structure describing the quote (MTTickShort).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

# IMTReportAPI::TickLast

Get the last quote for the specified symbol processed in accordance with its settings for a certain group.
    
    
    MTAPIRES  IMTReportAPI::TickLast(
       const IMTConSymbol*  symbol,     // Symbol configuration object
       MTTickShort&         tick        // Pointer to a quote structure
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration. The symbol object must be first created using theIMTReportAPI::SymbolCreatemethod.

**tick**  
[out] A pointer to the structure describing the quote (MTTickShort).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Symbol settings, in accordance with which the quotes received by this method are processed, correspond to the settings received by calling [IMTReportAPI::SymbolGet](../Configuration-Databases/Symbols/SymbolGet.md) for a specific group.

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
