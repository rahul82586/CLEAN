[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealRequestByLoginsSymbol

[Previous](DealRequestByLogins.md) | [Next](DealRequestByTickets.md)

# IMTManagerAPI::DealRequestByLoginsSymbol

Get deals by a list of logins and symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealRequestByLoginsSymbol(
       const UINT64* logins,       // logins
       const UINT    logins_total, // number of logins
       LPCWSTR       symbol,       // symbol
       const INT64   from,         // beginning of period
       const INT64   to,           // end of period
       IMTDealArray* deals         // array of deals
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealRequestByLoginsSymbol(
       ulong[]       logins,       // logins
       string        symbol,       // symbol
       long          from,         // beginning of period
       long          to,           // end of period
       CIMTDealArray deals         // array of deals
       )

Python
    
    
    ManagerAPI.DealRequestByLoginsSymbol(
       logins,       # logins
       symbol,       # symbol
       from,         # beginning of period
       to            # end of period
       )
    
    
    ManagerAPI.DealRequestByLoginsSymbolCSV(
       logins,       # logins
       symbol,       # symbol
       from,         # beginning of period
       to,           # end of period
       fields        # comma-separated list of required fields
       )
    
    
    ManagerAPI.DealRequestByLoginsSymbolNumPy(
       logins,       # logins
       symbol,       # symbol
       from,         # beginning of period
       to,           # end of period
       fields        # comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

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
