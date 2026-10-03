[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / CountryAdd

[Previous](MessageTemplate.md) | [Next](CountryUpdate.md)

# IMTConMessenger::CountryAdd

Add a country for which the messenger will be used.

C++
    
    
    MTAPIRES  IMTConMessenger::CountryAdd(
       IMTConMessengerCountry*  country      // Country object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.CountryAdd(
       CIMTConMessengerCountry  country      // Country object
       )

Python
    
    
    MTConMessenger.CountryAdd(
       country                  # Country object
       )

### Parameters

**country**  
[in] Country objectIMTConMessengerCountry.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
