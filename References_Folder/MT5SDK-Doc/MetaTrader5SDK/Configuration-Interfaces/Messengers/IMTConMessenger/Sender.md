[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / Sender

[Previous](Name.md) | [Next](ProviderType.md)

# IMTConMessenger::Sender

Get the sender name in the messenger configuration.

C++
    
    
    LPCWSTR  IMTConMessenger::Sender()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.Sender()

Python
    
    
    MTConMessenger.Sender

### Return Value

If successful, the method returns a pointer to a string with the sender's name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConMessenger](../IMTConMessenger.md) object.

You should create a string copy if you want to use it after the object removal (call of the [IMTConMessenger::Release](Release.md) method of this object).

# IMTConMessenger::Sender

Set the sender name in the messenger configuration.

C++
    
    
    MTAPIRES  IMTConMessenger::Sender(
       LPCWSTR  sender    // Sender name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.Sender(
       srting   sender    // Sender name
       )

Python
    
    
    MTConMessenger.Sender

### Parameters

**name**  
[in] Email sender name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum name length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
