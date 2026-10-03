[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderGetByLogins

[Previous](OrderGetByGroup.md) | [Next](OrderGetByTickets.md)

# IMTManagerAPI::OrderGetByLogins

Receive currently open orders by the list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderGetByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTOrderArray*     orders        // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderGetByLogins(
       ulong[]            logins,       // Logins
       CIMTOrderArray     orders        // Object of the orders array
       )

Python
    
    
    ManagerAPI.OrderGetByLogins(
       logins             # Logins
       )
    
    
    ManagerAPI.OrderGetByLoginsCSV(
       logins,            # Logins
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.OrderGetByLoginsNumPy(
       logins,            # Logins
       fields             # Comma-separated list of required fields
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

The method copies to the 'orders' object the data of all open orders belonging to the specified accounts. The method works only if the [IMTManagerAPI::PUMP_MODE_ORDERS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
