[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / CountryClear

[Previous](CountryDelete.md) | [Next](CountryShift.md)

# IMTConMessenger::CountryClear

Clear the list of countries for which the messenger is used.

C++
    
    
    MTAPIRES  IMTConMessenger::CountryClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.CountryClear()

Python
    
    
    MTConMessenger.CountryClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method deletes from the list all countries for which the messenger is used.
