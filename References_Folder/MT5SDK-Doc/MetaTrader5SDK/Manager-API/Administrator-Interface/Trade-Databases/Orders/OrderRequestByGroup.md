[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestByGroup

[Previous](OrderRequestOpen.md) | [Next](OrderRequestByGroupSymbol.md)

# IMTAdminAPI::OrderRequestByGroup

Request from the server open orders related to a client group.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderRequestByGroup(
       LPCWSTR            group,         // Group
       IMTOrderArray*     orders         // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderRequestByGroup(
       string             mask,          // Group
       CIMTOrderArray     orders         // Object of the orders array
       )

Python
    
    
    AdminAPI.OrderRequestByGroup(
       group              # Group
       )
    
    
    AdminAPI.OrderRequestByGroupCSV(
       group,             # Group
       fields             # Comma-separated list of required fields
       )
    
    
    AdminAPI.OrderRequestByGroupNumPy(
       group,             # Group
       fields             # Comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the orders are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data on all open orders belonging to clients in the specified groups.
