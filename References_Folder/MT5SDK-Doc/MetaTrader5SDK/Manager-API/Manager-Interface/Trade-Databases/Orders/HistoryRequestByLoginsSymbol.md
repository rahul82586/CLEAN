[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequestByLoginsSymbol

[Previous](HistoryRequestByLogins.md) | [Next](HistoryRequestByTickets.md)

# IMTManagerAPI::HistoryRequestByLoginsSymbol

Request closed orders (history) from the server by list of logins and symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::HistoryRequestByLoginsSymbol(
       const UINT64*      logins,       // logins
       const UINT         logins_total, // number of logins
       const INT64        from,         // beginning of period
       const INT64        to,           // end of period
       IMTOrderArray*     orders        // order array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.HistoryRequestByLoginsSymbol(
       ulong[]            logins,       // logins
       string             symbol,       // symbol
       long               from,         // beginning of period
       long               to,           // end of period
       CIMTOrderArray     orders        // order array object
       )

Python
    
    
    ManagerAPI.HistoryRequestByLoginsSymbol(
       logins,            # logins
       symbol,            # symbol
       from,              # beginning of period
       to                 # end of period
       )
    
    
    ManagerAPI.HistoryRequestByLoginsSymbolCSV(
       logins,            # logins
       symbol,            # symbol
       from,              # beginning of period
       to,                # end of period
       fields             # comma-separated list of required fields
       )
    
    
    ManagerAPI.HistoryRequestByLoginsSymbolNumPy(
       logins,            # logins
       symbol,            # symbol
       from,              # beginning of period
       to,                # end of period
       fields             # comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

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
