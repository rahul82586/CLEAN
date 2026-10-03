[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequestByLogins

[Previous](HistoryRequestByGroupSymbol.md) | [Next](HistoryRequestByLoginsSymbol.md)

# IMTManagerAPI::HistoryRequestByLogins

Request from the server the closed orders (history) related to the list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::HistoryRequestByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       const INT64        from,         // Beginning of the period
       const INT64        to,           // End of the period
       IMTOrderArray*     orders        // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.HistoryRequestByLogins(
       ulong[]            logins,       // Logins
       long               from,         // Beginning of the period
       long               to,           // End of the period
       CIMTOrderArray     orders        // Object of the orders array
       )

Python
    
    
    ManagerAPI.HistoryRequestByLogins(
       logins,            # Logins
       from,              # Beginning of the period
       to                 # End of the period
       )
    
    
    ManagerAPI.HistoryRequestByLoginsCSV(
       logins,            # Logins
       from,              # Beginning of the period
       to,                # End of the period
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.HistoryRequestByLoginsNumPy(
       logins,            # Logins
       from,              # Beginning of the period
       to,                # End of the period
       fields             # Comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**from**  
[in] The beginning of the period for which you need to receive orders. The date is specified in seconds which have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to receive orders. The date is specified in seconds which have elapsed since 01.01.1970.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all closed orders belonging to the specified accounts.
