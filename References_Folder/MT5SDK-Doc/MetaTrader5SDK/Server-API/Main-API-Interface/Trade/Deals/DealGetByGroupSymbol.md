[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealGetByGroupSymbol

[Previous](DealGetByGroup.md) | [Next](DealGetByLogins.md)

# IMTServerAPI::DealGetByGroupSymbol

Get deals by group and symbol.
    
    
    MTAPIRES  IMTServerAPI::DealGetByGroupSymbol(
       LPCWSTR       group,      // group
       LPCWSTR       symbol,     // symbol
       const INT64   from,       // beginning of period
       const INT64   to,         // end of period
       IMTDealArray* deals       // array of deals
       )

### Parameters

**group**  
[in] The groups for which deals are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group 'demoforex'.

**symbol**  
[in] The symbol for which you need to get deals. You can specify multiple symbols separated by commas as well as symbol masks. The maximum length of the string is 127 characters.

**from**  
[in] The beginning of the period for which you need to get deals. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to receive deals. The date is specified in seconds since 01.01.1970.

**deals**  
[out] An object of the deals array. The 'deals' object must first be created using theIMTAdminAPI::DealCreateArraymethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
