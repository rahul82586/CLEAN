[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerTemplate](../IMTConMessengerTemplate.md) / Id

[Previous](Type.md) | [Next](../IMTConMessengerSink.md)

# IMTConMessengerTemplate::Id

Get the message template identifier on the provider side.

C++
    
    
    LPCWSTR  IMTConMessengerTemplate::Id()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessengerTemplate.Id()

Python
    
    
    MTConMessengerTemplate.Id

### Return Value

If successful, the method returns a pointer to the string with the identifier. Otherwise, NULL is returned.

### Note

The pointer to the resulting string remains valid for the lifetime of the [IMTConMessengerTemplate](../IMTConMessengerTemplate.md) object.

# IMTConMessengerTemplate::Id

Set the message template identifier on the provider side.

C++
    
    
    MTAPIRES  IMTConMessengerTemplate::Id(
       LPCWSTR  id      // template identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerTemplate.Id(
       srting   id      // template identifier
       )

Python
    
    
    MTConMessengerTemplate.Id

### Parameters

**id**  
[in] Template identifier on the provider sied.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code is returned.
