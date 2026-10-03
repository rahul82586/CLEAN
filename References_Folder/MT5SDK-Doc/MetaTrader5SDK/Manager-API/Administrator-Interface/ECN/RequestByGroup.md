[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / RequestByGroup

[Previous](CreateHistoryDealArray.md) | [Next](RequestByLogins.md)

# IMTAdminAPI::ECNRequestByGroup

Request the [current state of matching](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history) for the specified client groups.

C++
    
    
    MTAPIRES  IMTAdminAPI::ECNRequestByGroup(
       LPCWSTR               mask,      // groups
       IMTECNMatchingArray*  matching,  // array of matching orders
       IMTECNFillingArray*   filling,   // array of filling orders
       IMTECNProviderArray*  providers  // array of providers
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ECNRequestByGroup(
       string                mask,      // groups
       CIMTECNMatchingArray  matching,  // array of matching orders
       CIMTECNFillingArray   filling,   // array of filling orders
       CIMTECNProviderArray  providers  // array of providers
       )

### Parameters

**groups**  
[in] Client group the data is requested for. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

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
