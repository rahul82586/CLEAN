[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / CountryNext

[Previous](CountryTotal.md) | [Next](GroupAdd.md)

# IMTConMessenger::CountryNext

Get the country for which the messenger is used, by its index in the list.

C++
    
    
    MTAPIRES  IMTConMessenger::CountryNext(
       const UINT               pos,      // Country position
       IMTConMessengerCountry*  country   // Country object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.CountryNext(
       uint                     pos,      // Country position
       CIMTConMessengerCountry  country   // Country object
       )

Python
    
    
    MTConMessenger.CountryNext(
       pos                      # Country position
       )
    
    
    MTConMessenger.CountryGet()

### Parameters

**pos**  
[in] The position of the country in the list, starting at 0.

**country**  
[out] Country object. The 'country' object must be previously created via theIMTServerAPI::MessengerCountryCreateorIMTAdminAPI::MessengerCountryCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
