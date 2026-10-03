[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderGetByGroup

[Previous](OrderGet.md) | [Next](OrderGetByGroupSymbol.md)

# IMTServerAPI::OrderGetByGroup

Get open orders for a client group.
    
    
    MTAPIRES  IMTServerAPI::OrderGetByGroup(
       LPCWSTR            group,         // Group
       IMTOrderArray*     orders         // The object of the orders array
       )

### Parameters

**group**  
[in] The groups for which the orders are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTServerAPI::OrderCreateArraymethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all open orders belonging to clients from the specified groups.
