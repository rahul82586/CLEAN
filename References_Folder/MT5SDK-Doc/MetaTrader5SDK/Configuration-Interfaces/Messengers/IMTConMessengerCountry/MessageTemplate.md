[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerCountry](../IMTConMessengerCountry.md) / MessageTemplate

[Previous](PhoneCode.md) | [Next](../IMTConMessengerGroup.md)

# IMTConMessengerCountry::MessageTemplate

Get a template for sending messages to users from a given country.

C++
    
    
    LPCWSTR  v::MessageTemplate()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessengerCountry.MessageTemplate()

Python
    
    
    MTConMessengerCountry.MessageTemplate

### Return Value

If successful, the method returns a pointer to a string with the template. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConMessengerCountry](../IMTConMessengerCountry.md) object.

# IMTConMessengerCountry::MessageTemplate

Set a template for sending messages to users from a given country.

C++
    
    
    MTAPIRES  IMTConMessengerCountry::MessageTemplate(
       LPCWSTR  msg_template    // Template
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerCountry.MessageTemplate(
       srting   msg_template    // Template
       )

Python
    
    
    MTConMessengerCountry.MessageTemplate

### Parameters

**msg_template**  
[in] Message template.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The name length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
