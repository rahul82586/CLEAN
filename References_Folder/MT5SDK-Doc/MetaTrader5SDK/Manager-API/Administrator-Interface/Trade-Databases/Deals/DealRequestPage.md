[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealRequestPage

[Previous](DealRequestByTickets.md) | [Next](DealAdd.md)

# IMTAdminAPI::DealRequestPage

Get client deals with a paged output.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealRequestPage(
       const UINT64   login,     // login
       const INT64    from,      // beginning of period
       const INT64    to,        // end of period
       const UINT     offset,    // deal index
       const UINT     total,     // number of deals
       IMTDealArray*  deals      // object of deals array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealRequestPage(
       ulong          login,     // login
       long           from,      // beginning of period
       long           to,        // end of period
       uint           offset,    // deal index
       uint           total,     // number of deals
       CIMTDealArray  deals      // object of deals array
       )

Python
    
    
    AdminAPI.DealRequestPage(
       login,         # login
       from,          # beginning of period
       to,            # end of period
       offset,        # deal index
       total          # number of deals
       )
    
    
    AdminAPI.DealRequestPageCSV(
       login,         # login
       from,          # beginning of period
       to,            # end of period
       offset,        # deal index
       total,         # number of deals
       fields         # comma-separated list of required fields
       )
    
    
    AdminAPI.DealRequestPageNumPy(
       login,         # login
       from,          # beginning of period
       to,            # end of period
       offset,        # deal index
       total,         # number of deals
       fields         # comma-separated list of required fields
       )

### Parameters

**login**  
[in] The login of the client, whose deals you wish to receive.

**from**  
[in] The beginning of the period for which you wish to receive deals. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you wish to receive deals. The date is specified in seconds that have elapsed since 01.01.1970.

**offset**  
[in] The index of the deal starting from which you wish to receive deals. Numbering starts from 0.

**total**  
[in] The number of deals that should be received.

**deals**  
[out] An object of the deals array. The 'deals' object must be previously created usingIMTManagerAPI::DealCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This request allows to easily arrange a paged output of resulting deals. Determine the number of deals that should be displayed on one page by setting it in the 'total' parameter. Then find the 'offset' parameter for each page, starting with 0 for the first page.
