[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryGetByLogins

[Previous](HistoryGetByGroupSymbol.md) | [Next](HistoryGetByLoginsSymbol.md)

# IMTServerAPI::HistoryGetByLogins

Receive closed orders (history) related to the list of logins.
    
    
    MTAPIRES  IMTServerAPI::HistoryGetByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       const INT64        from,          // Period from
       const INT64        to,            // Period to
       IMTOrderArray*     orders        // The object of the orders array
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**from**  
[in] The beginning of the period you want to receive orders for. The date is specified in seconds which have elapsed since 01.01.1970.

**to**  
[in] The end of the period you want to receive orders for. The date is specified in seconds which have elapsed since 01.01.1970.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTServerAPI::OrderCreateArraymethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all closed orders belonging to the specified accounts.
