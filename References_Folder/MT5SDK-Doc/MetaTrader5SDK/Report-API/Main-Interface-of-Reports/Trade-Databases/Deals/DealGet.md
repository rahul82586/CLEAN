[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealGet

[Previous](DealCreateArray.md) | [Next](DealSelect.md)

# IMTReportAPI::DealGet

Get a deal by a ticket.
    
    
    MTAPIRES  IMTReportAPI::DealGet(
       const UINT64  ticket,     // The ticket of a deal
       IMTDeal*      deal        // An object of a deal
       )

### Parameters

**ticket**  
[in] The number (ticket) of a deal.

**deal**  
[out] An object of a deal. The deal object must be first created using theIMTReportAPI:DealCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the data of a deal with the specified ticket to the deal object. When calling this method Report API limits the end of the request time range by the time of the report generation ([IMTReportAPI::TimeGeneration](../../Configuration-Databases/Time/Generation.md)).

# IMTReportAPI::DealGet

Get the deals of a client in the specified date range.
    
    
    MTAPIRES  IMTReportAPI::DealGet(
       const UINT64   login,     // Login
       const INT64    from,      // Beginning of period
       const INT64    to,        // End of period
       IMTDealArray*  deals      // An object of the array of deals
       )

### Parameters

**login**  
[in] The login of the client, whose deals you need to get.

**from**  
[in] The beginning of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**deals**  
[out] An object of the array of deals. The deals object must be first created using theIMTReportAPI::DealCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

When calling this method Report API limits the end of the request time range by the time of the report generation ([IMTReportAPI::TimeGeneration](../../Configuration-Databases/Time/Generation.md)).
