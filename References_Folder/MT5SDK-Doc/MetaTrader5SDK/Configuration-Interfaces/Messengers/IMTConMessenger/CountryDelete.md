[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / CountryDelete

[Previous](CountryUpdate.md) | [Next](CountryClear.md)

# IMTConMessenger::CountryDelete

Delete the country for which the messenger is used.

C++
    
    
    MTAPIRES  IMTConMessenger::CountryDelete(
       const UINT  pos      // Position of the country
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.CountryDelete(
       uint        pos      // Position of the country
       )

Python
    
    
    MTConMessenger.CountryDelete(
       pos         # Position of the country
       )

### Parameters

**pos**  
[in] The position of the country in the list, starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
