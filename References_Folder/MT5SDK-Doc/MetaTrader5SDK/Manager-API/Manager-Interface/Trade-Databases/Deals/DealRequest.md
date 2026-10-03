[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealRequest

[Previous](DealUnsubscribe.md) | [Next](DealRequestByGroup.md)

# IMTManagerAPI::DealRequest

Get a deal by a ticket.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealRequest(
       const UINT64  ticket,     // The ticket of a deal
       IMTDeal*      deal        // An object of a deal
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealRequest(
       ulong         ticket,     // The ticket of a deal
       CIMTDeal      deal        // An object of a deal
       )

Python
    
    
    ManagerAPI.DealRequest(
       ticket        # The ticket of a deal
       )

### Parameters

**ticket**  
[in] The number (ticket) of a deal.

**deal**  
[out] An object of a deal. The deal object must be first created using theIMTManagerAPI::DealCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the data of a deal with the specified ticket to the deal object.

# IMTManagerAPI::DealRequest

Get the deals of a client in the specified date range.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealRequest(
       const UINT64   login,     // Login
       const INT64    from,      // Beginning of period
       const INT64    to,        // End of period
       IMTDealArray*  deals      // An object of the array of deals
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealRequest(
       ulong          login,     // Login
       long           from,      // Beginning of period
       long           to,        // End of period
       CIMTDealArray  deals      // An object of the array of deals
       )

Python
    
    
    ManagerAPI.DealRequest(
       login,         # Login
       from,          # Beginning of period
       to             # End of period
       )

### Parameters

**login**  
[in] The login of the client, whose deals you need to get.

**from**  
[in] The beginning of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**deals**  
[out] An object of the array of deals. The deals object must be first created using theIMTManagerAPI::DealCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).
