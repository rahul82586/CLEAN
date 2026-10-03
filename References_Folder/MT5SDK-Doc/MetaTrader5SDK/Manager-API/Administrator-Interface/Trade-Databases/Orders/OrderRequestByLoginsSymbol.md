[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestByLoginsSymbol

[Previous](OrderRequestByLogins.md) | [Next](OrderRequestByTickets.md)

# IMTAdminAPI::OrderRequestByLoginsSymbol

Request open orders from the server by list of logins and symbol.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderRequestByLoginsSymbol(
       const UINT64*      logins,       // logins
       const UINT         logins_total, // number of logins
       LPCWSTR            symbol,       // symbol
       IMTOrderArray*     orders        // order array object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderRequestByLoginsSymbol(
       ulong[]            logins,       // logins
       string             symbol,       // symbol
       CIMTOrderArray     orders        // order array object
       )

Python
    
    
    AdminAPI.OrderRequestByLoginsSymbol(
       logins,            # logins
       symbol             # symbol
       )
    
    
    AdminAPI.OrderRequestByLoginsSymbolCSV(
       logins,            # logins
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )
    
    
    AdminAPI.OrderRequestByLoginsSymbolNumPy(
       logins,            # logins
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**symbol**  
[in] The symbol, for which you wish to get orders. You can specify multiple symbols separated by commas.

**orders**  
[out] An object of the array of orders. The 'orders' object must first be created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
