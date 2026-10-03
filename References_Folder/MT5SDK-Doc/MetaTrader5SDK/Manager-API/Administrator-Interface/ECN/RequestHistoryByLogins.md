[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / RequestHistoryByLogins

[Previous](RequestHistoryByGroup.md) | [Next](RequestHistoryByTickets.md)

# IMTAdminAPI::ECNRequestByLogins

Request the [matching history (#history)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#history) for the specified logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::ECNRequestByLogins(
       const UINT64*               logins,       // logins
       const UINT                  logins_total, // the number of logins
       const INT64                 from,         // period beginning
       const INT64                 to,           // period end
       IMTECNHistoryMatchingArray* matching,     // array of matching orders
       IMTECNHistoryFillingArray*  filling,      // array of filling objects
       IMTECNHistoryDealArray*     deals,        // array of deals
       IMTECNProviderArray*        providers     // array of providers
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ECNRequestByLogins(
       ulong[]                     logins,       // logins
       long                        from,         // period beginning
       long                        to,           // period end
       CIMTECNMatchingArray        matching,     // array of matching orders
       CIMTECNFillingArray         filling,      // array of filling orders
       CIMTECNHistoryDealArray     deals,        // array of deals
       CIMTECNProviderArray        providers     // array of providers
       )

### Parameters

**logins**  
[in] An array of logins the data is requested for.

**logins_total**  
[in] The number of logins in the 'logins' array.

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
