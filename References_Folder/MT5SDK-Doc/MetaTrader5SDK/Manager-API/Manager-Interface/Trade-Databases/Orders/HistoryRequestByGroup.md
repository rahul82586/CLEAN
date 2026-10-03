[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequestByGroup

[Previous](HistoryRequest.md) | [Next](HistoryRequestByGroupSymbol.md)

# IMTManagerAPI::HistoryRequestByGroup

Request from the server closed orders (history) related to a client group.

C++
    
    
    MTAPIRES  IMTManagerAPI::HistoryRequestByGroup(
       LPCWSTR            group,         // Group
       const INT64        from,          // Beginning of the period
       const INT64        to,            // End of the period
       IMTOrderArray*     orders         // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.HistoryRequestByGroup(
       string             mask,          // Group
       long               from,          // Beginning of the period
       long               to,            // End of the period
       CIMTOrderArray     orders         // Object of the orders array
       )

Python
    
    
    ManagerAPI.HistoryRequestByGroup(
       mask,              # Group
       from,              # Beginning of the period
       to                 # End of the period
       )
    
    
    ManagerAPI.HistoryRequestByGroupCSV(
       mask,              # Group
       from,              # Beginning of the period
       to,                # End of the period
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.HistoryRequestByGroupNumPy(
       mask,              # Group
       from,              # Beginning of the period
       to,                # End of the period
       fields             # Comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the orders are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex.

**from**  
[in] The beginning of the period for which you need to receive orders. The date is specified in seconds which have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to receive orders. The date is specified in seconds which have elapsed since 01.01.1970.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all closed orders belonging to clients in the specified groups.
