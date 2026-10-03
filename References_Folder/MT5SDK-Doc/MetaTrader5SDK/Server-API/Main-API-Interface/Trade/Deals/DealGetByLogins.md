[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealGetByLogins

[Previous](DealGetByGroupSymbol.md) | [Next](DealGetByLoginsSymbol.md)

# IMTServerAPI::DealGetByLogins

Receive deals by the list of logins.
    
    
    MTAPIRES  IMTServerAPI::DealGetByLogins(
       const UINT64* logins,       // Logins
       const UINT    logins_total, // Number of logins
       const INT64   from,         // Period from
       const INT64   to,           // Period to
       IMTDealArray* deals         // Array of deals
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
[out] An object of the deals array. The 'deals' object must be first created usingIMTServerAPI::DealCreateArray.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method copies to the 'deals' object data of all deals, which belong to the specified accounts and which were executed in the specified time range.
