[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequestByGroupSymbol

[Previous](HistoryRequestByGroup.md) | [Next](HistoryRequestByLogins.md)

# IMTManagerAPI::HistoryRequestByGroupSymbol

Request closed orders (history) from the server by group and symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::HistoryRequestByGroupSymbol(
       LPCWSTR            group,         // group
       LPCWSTR            symbol,        // symbol
       const INT64        from,          // beginning of period
       const INT64        to,            // end of period
       IMTOrderArray*     orders         // order array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.HistoryRequestByGroupSymbol(
       string             mask,          // group
       string             symbol,        // symbol
       long               from,          // beginning of period
       long               to,            // end of period
       CIMTOrderArray     orders         // order array object
       )

Python
    
    
    ManagerAPI.HistoryRequestByGroupSymbol(
       mask,              # group
       symbol,            # symbol
       from,              # beginning of period
       to                 # end of period
       )
    
    
    ManagerAPI.HistoryRequestByGroupSymbolCSV(
       mask,              # group
       symbol,            # symbol
       from,              # beginning of period
       to,                # end of period
       fields             # comma-separated list of required fields
       )
    
    
    ManagerAPI.HistoryRequestByGroupSymbolNumPy(
       mask,              # group
       symbol,            # symbol
       from,              # beginning of period
       to,                # end of period
       fields             # comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the orders are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**symbol**  
[in] The symbol, for which you wish to get orders.

**from**  
[in] The beginning of the period for which you need to get orders. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get orders. The date is specified in seconds since 01.01.1970.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
