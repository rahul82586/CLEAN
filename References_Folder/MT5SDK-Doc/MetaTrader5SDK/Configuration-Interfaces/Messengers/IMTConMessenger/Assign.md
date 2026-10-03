[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConMessenger::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConMessenger::Assign(
       const IMTConMessenger*  messenger  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.Assign(
       CIMTConMessenger        messenger  // Source object
       )

### Parameters

**messenger**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
