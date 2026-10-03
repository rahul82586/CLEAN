[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestByGroup

[Previous](OrderRequestOpen.md) | [Next](OrderRequestByGroupSymbol.md)

# IMTManagerAPI::OrderRequestByGroup

Request from the server open orders related to a client group.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderRequestByGroup(
       LPCWSTR            group,         // Group
       IMTOrderArray*     orders         // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderRequestByGroup(
       string             mask,          // Group
       CIMTOrderArray     orders         // Object of the orders array
       )

Python
    
    
    ManagerAPI.OrderRequestByGroup(
       mask               # Group
       )
    
    
    ManagerAPI.OrderRequestByGroupCSV(
       mask,              # Group
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.OrderRequestByGroupNumPy(
       mask,              # Group
       fields             # Comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the orders are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data on all open orders belonging to clients in the specified groups.
