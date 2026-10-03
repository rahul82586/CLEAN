[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequestByGroup

[Previous](HistoryRequestByLoginsSymbol.md) | [Next](HistoryRequestByGroupSymbol.md)

# IMTAdminAPI::HistoryRequestByGroup

Request from the server closed orders (history) related to a client group.

C++
    
    
    MTAPIRES  IMTAdminAPI::HistoryRequestByGroup(
       LPCWSTR            group,         // Group
       const INT64        from,          // Beginning of the period
       const INT64        to,            // End of the period
       IMTOrderArray*     orders         // Object of the orders array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HistoryRequestByGroup(
       string             mask,          // Group
       long               from,          // Beginning of the period
       long               to,            // End of the period
       CIMTOrderArray     orders         // Object of the orders array
       )

Python
    
    
    AdminAPI.HistoryRequestByGroup(
       group,             # Group
       from,              # Beginning of the period
       to                 # End of the period
       )
    
    
    AdminAPI.HistoryRequestByGroupCSV(
       group,             # Group
       from,              # Beginning of the period
       to,                # End of the period
       fields             # Comma-separated list of required fields
       )
    
    
    AdminAPI.HistoryRequestByGroupNumPy(
       group,             # Group
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
[out] An object of the array of orders. The 'orders' object should be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all closed orders belonging to clients in the specified groups.
