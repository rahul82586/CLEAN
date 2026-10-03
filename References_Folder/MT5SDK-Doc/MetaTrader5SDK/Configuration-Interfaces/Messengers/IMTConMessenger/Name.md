[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / Name

[Previous](Clear.md) | [Next](Sender.md)

# IMTConMessenger::Name

Get the messenger configuration name.

C++
    
    
    LPCWSTR  IMTConMessenger::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.Name()

Python
    
    
    MTConMessenger.Name

### Return Value

If successful, the method returns a pointer to a string with the messenger name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConMessenger](../IMTConMessenger.md) object.

# IMTConMessenger::Name

Set the messenger configuration name.

C++
    
    
    MTAPIRES  IMTConMessenger::Name(
       LPCWSTR  name      // Messenger name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.Name(
       srting   name      // Messenger name
       )

Python
    
    
    MTConMessenger.Name

### Parameters

**name**  
[in] Messenger name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum name length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
