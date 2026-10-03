[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestByLogins

[Previous](OrderRequestByGroupSymbol.md) | [Next](OrderRequestByLoginsSymbol.md)

# IMTManagerAPI::OrderRequestByLogins

Request from the server open orders related to the list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderRequestByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTOrderArray*     orders        // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderRequestByLogins(
       ulong[]            logins,       // Logins
       CIMTOrderArray     orders        // Object of the orders array
       )

Python
    
    
    ManagerAPI.OrderRequestByLogins(
       logins             # Logins
       )
    
    
    ManagerAPI.OrderRequestByLoginsCSV(
       logins,            # Logins
       fields             # Object of the orders array
       )
    
    
    ManagerAPI.OrderRequestByLoginsNumPy(
       logins,            # Logins
       fields             # Object of the orders array
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all open orders belonging to the specified accounts.
