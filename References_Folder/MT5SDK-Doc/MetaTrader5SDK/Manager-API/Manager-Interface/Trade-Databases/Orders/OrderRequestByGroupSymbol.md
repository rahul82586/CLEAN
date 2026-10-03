[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestByGroupSymbol

[Previous](OrderRequestByGroup.md) | [Next](OrderRequestByLogins.md)

# IMTManagerAPI::OrderRequestByGroupSymbol

Request open orders from the server by group and symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderRequestByGroupSymbol(
       LPCWSTR            group,         // group
       LPCWSTR            symbol,        // symbol
       IMTOrderArray*     orders         // order array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderRequestByGroupSymbol(
       string             mask,          // group
       string             symbol,        // symbol
       CIMTOrderArray     orders         // order array object
       )

Python
    
    
    ManagerAPI.OrderRequestByGroupSymbol(
       mask,              # group
       symbol             # symbol
       )
    
    
    ManagerAPI.OrderRequestByGroupSymbolCSV(
       mask,              # group
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )
    
    
    ManagerAPI.OrderRequestByGroupSymbolNumPy(
       mask,              # group
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the orders are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**symbol**  
[in] The symbol, for which you wish to get orders. You can specify multiple symbols separated by commas as well as symbol masks. The maximum length of the string is 127 characters.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data on all open orders belonging to clients in the specified groups.
