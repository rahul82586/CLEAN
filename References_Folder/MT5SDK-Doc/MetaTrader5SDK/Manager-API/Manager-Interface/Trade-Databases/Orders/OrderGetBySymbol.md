[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderGetBySymbol

[Previous](OrderGetByTickets.md) | [Next](OrderRequest.md)

# IMTManagerAPI::OrderGetBySymbol

Get currently open orders by group and symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderGetBySymbol(
       LPCWSTR         groups,    // Group mask
       LPCWSTR         symbol,    // Symbol
       IMTOrderArray*  orders     // Orders array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderGetBySymbol(
       String^         groups,    // Group mask
       String^         symbol,    // Symbol
       CIMTOrderArray  orders     // Orders array object
       )

Python
    
    
    ManagerAPI.OrderGetBySymbol(
       groups,         # Group mask
       symbol,         # Symbol
       )
    
    
    ManagerAPI.OrderGetBySymbolCSV(
       groups,         # Group mask
       symbol,         # Symbol
       fields          # Comma-separated list of required fields
       )
    
    
    ManagerAPI.OrderGetBySymbolNumPy(
       groups,         # Group mask
       symbol,         # символ
       fields          # Comma-separated list of required fields
       )

### Parameters

**groups**  
[in] The groups the orders are requested for. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex. The 'nullptr' value means "all groups".

**news**  
[in] The symbol, for which you wish to obtain orders.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method only works if the [IMTManagerAPI::PUMP_MODE_ORDERS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during connection.
