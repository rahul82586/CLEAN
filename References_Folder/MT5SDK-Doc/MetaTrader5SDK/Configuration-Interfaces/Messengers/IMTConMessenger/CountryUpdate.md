[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / CountryUpdate

[Previous](CountryAdd.md) | [Next](CountryDelete.md)

# IMTConMessenger::CountryUpdate

Change the country for which the messenger is used.

C++
    
    
    MTAPIRES  IMTConMessenger::CountryUpdate(
       const UINT                     pos,      // Country position
       const IMTConMessengerCountry*  country   // Country object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.CountryUpdate(
       uint                           pos,      // Country position
       CIMTConMessengerCountry        country   // Country object
       )

Python
    
    
    MTConMessenger.CountryUpdate(
       pos,                           # Country position
       country                        # Country object
       )
    
    
    MTConMessenger.CountrySet(
       country-list                   # List of countries
       )

### Parameters

**pos**  
[in] Position of the country in the list, starting with 0.

**country**  
[in] Country objectIMTConMessengerCountry.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
