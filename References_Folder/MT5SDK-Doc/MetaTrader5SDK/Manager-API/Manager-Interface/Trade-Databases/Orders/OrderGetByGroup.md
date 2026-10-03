[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderGetByGroup

[Previous](OrderGetOpen.md) | [Next](OrderGetByLogins.md)

# IMTManagerAPI::OrderGetByGroup

Request from the server open orders related to a client group.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderGetByGroup(
       LPCWSTR         mask,      // group mask
       IMTOrderArray*  orders     // object of the array of orders
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderGetByGroup(
       String^         mask,      // group mask
       CIMTOrderArray  orders     // object of the array of orders
       )

Python
    
    
    ManagerAPI.OrderGetByGroup(
       mask            # group mask
       )
    
    
    ManagerAPI.OrderGetByGroupCSV(
       mask,           # group mask
       fields          # comma-separated list of required fields
       )
    
    
    ManagerAPI.OrderGetByGroupNumPy(
       mask,           # group mask
       fields          # comma-separated list of required fields
       )

### Parameters

**mask**  
[in] The groups the orders are requested for. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies the data on all open orders belonging to clients in the specified groups to the 'orders' object. The method works only if the [IMTManagerAPI::PUMP_MODE_ORDERS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
