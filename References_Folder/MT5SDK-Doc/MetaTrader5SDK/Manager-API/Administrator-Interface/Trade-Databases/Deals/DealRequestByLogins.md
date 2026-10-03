[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealRequestByLogins

[Previous](DealRequestByGroupSymbol.md) | [Next](DealRequestByLoginsSymbol.md)

# IMTAdminAPI::DealRequestByLogins

Receive deals by the list of logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealRequestByLogins(
       const UINT64* logins,       // Logins
       const UINT    logins_total, // Number of logins
       const INT64   from,         // Beginning of the period
       const INT64   to,           // End of the period
       IMTDealArray* deals         // Array of deals
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealRequestByLogins(
       ulong[]       logins,       // Logins
       long          from,         // Beginning of the period
       long          to,           // End of the period
       CIMTDealArray deals         // Array of deals
       )

Python
    
    
    AdminAPI.DealRequestByLogins(
       logins,       # Logins
       from,         # Beginning of the period
       to            # End of the period
       )
    
    
    AdminAPI.DealRequestByLoginsCSV(
       logins,       # Logins
       from,         # Beginning of the period
       to,           # End of the period
       fields        # Comma-separated list of required fields
       )
    
    
    AdminAPI.DealRequestByLoginsNumPy(
       logins,       # Logins
       from,         # Beginning of the period
       to,           # End of the period
       fields        # Comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**from**  
[in] The beginning of the period for which you need to receive deals. The date is specified in seconds which have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to receive deals. The date is specified in seconds which have elapsed since 01.01.1970.

**deals**  
[out] An object of the deals array. The 'deals' object must be first created usingIMTAdminAPI::DealCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method copies to the 'deals' object data of all deals, which belong to the specified accounts and which were executed in the specified time range.
