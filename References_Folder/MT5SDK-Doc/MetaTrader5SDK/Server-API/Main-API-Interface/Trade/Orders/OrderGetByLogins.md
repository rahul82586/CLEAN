[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderGetByLogins

[Previous](OrderGetByGroupSymbol.md) | [Next](OrderGetByLoginsSymbol.md)

# IMTServerAPI::OrderRequestByLogins

Receive open orders by the list of logins.
    
    
    MTAPIRES  IMTServerAPI::OrderRequestByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTOrderArray*     orders        // The object of the orders array
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTServerAPI::OrderCreateArraymethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all open orders belonging to the specified accounts.
