[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / RequestByLogins

[Previous](RequestByGroup.md) | [Next](RequestByTickets.md)

# IMTAdminAPI::ECNRequestByLogins

Request the [current state of matching](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history) for the specified logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::ECNRequestByLogins(
       const UINT64*         logins,       // logins
       const UINT            logins_total, // number of logins
       IMTECNMatchingArray*  matching,     // array of matching orders
       IMTECNFillingArray*   filling,      // array of filling orders
       IMTECNProviderArray*  providers     // array of providers
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ECNRequestByLogins(
       ulong[]               logins,       // logins
       CIMTECNMatchingArray  matching,     // array of matching orders
       CIMTECNFillingArray   filling,      // array of filling orders
       CIMTECNProviderArray  providers     // array of providers
       )

### Parameters

**logins**  
[in] An array of logins the data is requested for.

**logins_total**  
[in] The number of logins in the 'logins' array.

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
