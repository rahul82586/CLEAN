[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / RequestHistoryByTickets

[Previous](RequestHistoryByLogins.md) | [Next](../Geo-Services.md)

# IMTManagerAPI::ECNRequestByTickets

Request the [matching history (#history)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#history) for the specified order tickets.

C++
    
    
    MTAPIRES  IMTManagerAPI::ECNRequestByTickets(
       const UINT64*               tickets,       // tickets
       const UINT                  tickets_total, // number of tickets
       const INT64                 from,          // period beginning
       const INT64                 to,            // period end
       IMTECNHistoryMatchingArray* matching,      // array of matching orders
       IMTECNHistoryFillingArray*  filling,       // array of filling orders
       IMTECNHistoryDealArray*     deals,         // array of deals
       IMTECNProviderArray*        providers      // array of providers
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ECNRequestByTickets(
       ulong[]                     tickets,       // tickets
       long                        from,          // period beginning
       long                        to,            // period end
       CIMTECNMatchingArray        matching,      // array of matching orders
       CIMTECNFillingArray         filling,       // array of filling orders
       CIMTECNHistoryDealArray     deals,         // array of deals
       CIMTECNProviderArray        providers      // array of providers
       )

### Parameters

**tickets**  
[in] An array of tickets the data is requested for.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**from**  
[in] The beginning of the period for which you need to get data. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get data. The date is specified in seconds since 01.01.1970.

**matching**  
[out] An object of thearray of matching orders from history. The 'matching' object must be previously created via theIMTAdminAPI::ECNCreateHistoryMatchingArraymethod.

**filling**  
[out] An object of thearray of filling orders from history. The 'filling' object must be previously created via theIMTAdminAPI::ECNCreateHistoryFillingArraymethod.

**deals**  
[out] An object of thearray of deals from history. The 'deals' object must be previously created via theIMTAdminAPI::ECNCreateHistoryDealArraymethod.

**providers**  
[out] An object of thearray of providers. The 'providers' object must be previously created via theIMTAdminAPI::ECNCreateProvidersArraymethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
