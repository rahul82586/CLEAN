[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealRequestByGroupSymbol

[Previous](DealRequestByGroup.md) | [Next](DealRequestByLogins.md)

# IMTManagerAPI::DealRequestByGroupSymbol

Get deals by group and symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealRequestByGroupSymbol(
       LPCWSTR       group,      // group
       LPCWSTR       symbol,     // symbol
       const INT64   from,       // beginning of period
       const INT64   to,         // end of period
       IMTDealArray* deals       // array of deals
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealRequestByGroupSymbol(
       string        mask,       // group
       string        symbol,     // symbol
       long          from,       // beginning of period
       long          to,         // end of period
       CIMTDealArray deals       // array of deals
       )

Python
    
    
    ManagerAPI.DealRequestByGroupSymbol(
       mask,         # group
       symbol,       # symbol
       from,         # beginning of period
       to            # end of period
       )
    
    
    ManagerAPI.DealRequestByGroupSymbolCSV(
       mask,         # group
       symbol,       # symbol
       from,         # beginning of period
       to,           # end of period
       fields        # comma-separated list of required fields
       )
    
    
    ManagerAPI.DealRequestByGroupSymbolNumPy(
       mask,         # group
       symbol,       # symbol
       from,         # beginning of period
       to,           # end of period
       fields        # comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which deals are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**symbol**  
[in] The symbol for which you need to get deals.

**from**  
[in] The beginning of the period for which you need to get deals. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to receive deals. The date is specified in seconds since 01.01.1970.

**deals**  
[out] An object of the deals array. The 'deals' object must be first created usingIMTManagerAPI::DealCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
