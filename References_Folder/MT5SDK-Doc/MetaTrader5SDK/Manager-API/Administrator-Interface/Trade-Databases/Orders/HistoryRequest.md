[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequest

[Previous](OrderReopen.md) | [Next](HistoryRequestByTickets.md)

# IMTAdminAPI::HistoryRequest

Request from the server the client's closed orders (history) in the specified date range.

C++
    
    
    MTAPIRES  IMTAdminAPI::HistoryRequest(
       const UINT64    login,      // Client login
       const INT64     from,       // Beginning of period
       const INT64     to,         // End of period
       IMTOrderArray*  orders      // An object of the array of orders
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HistoryRequest(
       ulong           login,      // Client login
       long            from,       // Beginning of period
       long            to,         // End of period
       CIMTOrderArray  orders      // An object of the array of orders
       )

Python
    
    
    AdminAPI.HistoryRequest(
       login,          # Client login
       from,           # Beginning of period
       to              # End of period
       )

### Parameters

**login**  
[in] The login of the client, whose open orders you need to get.

**from**  
[in] The beginning of the period you want to receive orders for. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get orders. The date is specified in seconds that have elapsed since 01.01.1970.

**orders**  
[out] An object of the array of orders. The orders object must be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).
