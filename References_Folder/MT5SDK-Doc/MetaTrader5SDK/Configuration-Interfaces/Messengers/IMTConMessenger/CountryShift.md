[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / CountryShift

[Previous](CountryClear.md) | [Next](CountryTotal.md)

# IMTConMessenger::CountryShift

Shift a country in the messenger settings.

C++
    
    
    MTAPIRES  IMTConMessenger::CountryShift(
       const UINT  pos,       // Country position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.CountryShift(
       uint        pos,       // Country position
       int         shift      // Shift
       )

Python
    
    
    MTConMessenger.CountryShift(
       uint        pos,       # Country position
       int         shift      # Shift
       )

### Parameters

**pos**  
[in] The position of the country in the list, starting at 0.

**shift**  
[in] The shift of the country relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
