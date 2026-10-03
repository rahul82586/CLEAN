[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequestPage

[Previous](HistoryRequestByGroupSymbol.md) | [Next](../Deals.md)

# IMTAdminAPI::HistoryRequestPage

Request from the server client's closed orders (history) in a paged form.

C++
    
    
    MTAPIRES  IMTAdminAPI::HistoryRequestPage(
       const UINT64    login,      // login
       const INT64     from,       // beginning of period
       const INT64     to,         // end of period
       const UINT      offset,     // order index
       const UINT      total,      // number of orders
       IMTOrderArray*  orders      // array of orders
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI::HistoryRequestPage(
       ulong           login,      // login
       long            from,       // beginning of period
       long            to,         // end of period
       uint            offset,     // order index
       uint            total,      // number of orders
       CIMTOrderArray  orders      // array of orders
       )

Python
    
    
    AdminAPI::HistoryRequestPage(
       login,          # login
       from,           # beginning of period
       to,             # end of period
       offset,         # order index
       total           # number of orders
       )
    
    
    AdminAPI::HistoryRequestPageCSV(
       login,          # login
       from,           # beginning of period
       to,             # end of period
       offset,         # order index
       total,          # number of orders
       fields          # comma-separated list of required fields
       )
    
    
    AdminAPI::HistoryRequestPageNumPy(
       login,          # login
       from,           # beginning of period
       to,             # end of period
       offset,         # order index
       total,          # number of orders
       fields          # comma-separated list of required fields
       )

### Parameters

**login**  
[in] The login of the client, whose orders you need to get.

**from**  
[in] The beginning of the period for which you need to get orders. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get orders. The date is specified in seconds since 01.01.1970.

**offset**  
[in] The index of the order starting from which you need to get orders. Numbering starts from 0.

**total**  
[in] The number of orders that should be obtained.

**orders**  
[out] An object of the array of orders. The 'orders' object must be previously created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method allows to easily arrange a paged output of resulting orders. Determine the number of orders that should be displayed on one page by setting it in the 'total' parameter. Then find the 'offset' parameter for each page, starting with 0 for the first page.
