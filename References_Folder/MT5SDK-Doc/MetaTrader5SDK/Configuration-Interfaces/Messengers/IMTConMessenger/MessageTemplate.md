[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / MessageTemplate

[Previous](Flags.md) | [Next](CountryAdd.md)

# IMTConMessenger::MessageTemplate

Get a basic template for sending messages via this provider.

C++
    
    
    LPCWSTR  IMTConMessenger::MessageTemplate()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessenger.MessageTemplate()

Python
    
    
    MTConMessenger.MessageTemplate

### Return Value

If successful, the method returns a pointer to a string with the template. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConMessenger](../IMTConMessenger.md) object.

# IMTConMessenger::MessageTemplate

Set a basic template for sending messages via this provider.

C++
    
    
    MTAPIRES  IMTConMessenger::MessageTemplate(
       LPCWSTR  msg_template    // Template
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.MessageTemplate(
       srting   msg_template    // Template
       )

Python
    
    
    MTConMessenger.MessageTemplate

### Parameters

**msg_template**  
[in] Message template.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The name length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
