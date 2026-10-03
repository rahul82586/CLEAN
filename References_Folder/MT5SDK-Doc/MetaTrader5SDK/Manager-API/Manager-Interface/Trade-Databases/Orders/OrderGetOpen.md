[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderGetOpen

[Previous](OrderGet.md) | [Next](OrderGetByGroup.md)

# IMTManagerAPI::OrderGetOpen

Get currently unfulfilled orders of a client.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderGetOpen(
       const UINT64    login,      // Client login
       IMTOrderArray*  orders      // An object of the array of orders
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderGetOpen(
       ulong           login,      // Client login
       CIMTOrderArray  orders      // An object of the array of orders
       )

Python
    
    
    ManagerAPI.OrderGetOpen(
       login           # Client login
       )
    
    
    ManagerAPI.OrderGetOpenCSV(
       login,          # Client login
       fields          # Comma-separated list of required fields
       )
    
    
    ManagerAPI.OrderGetOpenNumPy(
       login,          # Client login
       fields          # Comma-separated list of required fields
       )

### Parameters

**login**  
[in] The login of the client, whose open orders you need to get.

**orders**  
[out] An object of the array of orders. The orders object must be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_ORDERS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
