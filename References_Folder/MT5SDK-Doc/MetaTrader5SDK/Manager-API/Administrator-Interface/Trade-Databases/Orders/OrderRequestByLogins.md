[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestByLogins

[Previous](OrderRequestByGroupSymbol.md) | [Next](OrderRequestByLoginsSymbol.md)

# IMTAdminAPI::OrderRequestByLogins

Request from the server open orders related to the list of logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderRequestByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTOrderArray*     orders        // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderRequestByLogins(
       ulong[]            logins,       // Logins
       CIMTOrderArray     orders        // Object of the orders array
       )

Python
    
    
    AdminAPI.OrderRequestByLogins(
       logins             # Logins
       )
    
    
    AdminAPI.OrderRequestByLoginsCSV(
       logins,            # Logins
       fields             # Object of the orders array
       )
    
    
    AdminAPI.OrderRequestByLoginsNumPy(
       logins,            # Logins
       fields             # Object of the orders array
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all open orders belonging to the specified accounts.
