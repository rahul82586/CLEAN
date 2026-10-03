[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerCountry](../IMTConMessengerCountry.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConMessengerCountry::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConMessengerCountry::Assign(
       const IMTConMessengerCountry*  country  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.Assign(
       CIMTConMessengerCountry        country  // Source object
       )

### Parameters

**country**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
