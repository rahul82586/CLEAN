[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryGetByGroupSymbol

[Previous](HistoryGetByGroup.md) | [Next](HistoryGetByLogins.md)

# IMTServerAPI::HistoryGetByGroupSymbol

Get closed orders (history) from the server by group and symbol.
    
    
    MTAPIRES  IMTServerAPI::HistoryGetByGroupSymbol(
       LPCWSTR            group,         // group
       LPCWSTR            symbol,        // symbol
       const INT64        from,          // beginning of period
       const INT64        to,            // end of period
       IMTOrderArray*     orders         // order array object
       )

### Parameters

**group**  
[in] The groups for which the orders are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group 'demoforex'.

**symbol**  
[in] The symbol, for which you are requesting orders. You can specify multiple symbols separated by commas as well as symbol masks. The maximum length of the string is 127 characters.

**from**  
[in] The beginning of the period for which you need to get orders. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get orders. The date is specified in seconds since 01.01.1970.

**orders**  
[out] Orders array object. The 'orders' object must first be created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
