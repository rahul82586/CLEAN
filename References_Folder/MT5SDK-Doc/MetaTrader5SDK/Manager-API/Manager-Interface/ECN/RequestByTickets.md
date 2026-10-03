[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / RequestByTickets

[Previous](RequestByLogins.md) | [Next](RequestHistoryByGroup.md)

# IMTManagerAPI::ECNRequestByTickets

Request the [current state of matching](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history) for the specified order tickets.

C++
    
    
    MTAPIRES  IMTManagerAPI::ECNRequestByTickets(
       const UINT64*         tickets,       // tickets
       const UINT            tickets_total, // number of tickets
       IMTECNMatchingArray*  matching,      // array of matching orders
       IMTECNFillingArray*   filling,       // array of filling orders
       IMTECNProviderArray*  providers      // array of providers
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ECNRequestByTickets(
       ulong[]               tickets,       // tickets
       CIMTECNMatchingArray  matching,      // array of matching orders
       CIMTECNFillingArray   filling,       // array of filling orders
       CIMTECNProviderArray  providers      // array of providers
       )

### Parameters

**tickets**  
[in] An array of tickets the data is requested for.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**matching**  
[out] An object of thearray of matching orders. The 'matching' object must be previously created via theIMTAdminAPI::ECNCreateMatchingArraymethod.

**filling**  
[out] An object of thearray of filling orders. The 'filling' object must be previously created via theIMTAdminAPI::ECNCreateFillingArraymethod.

**providers**  
[out] An object of thearray of providers. The 'providers' object must be previously created via theIMTAdminAPI::ECNCreateProvidersArraymethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
