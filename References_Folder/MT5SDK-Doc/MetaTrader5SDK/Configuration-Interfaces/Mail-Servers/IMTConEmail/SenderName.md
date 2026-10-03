[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / SenderName

[Previous](SenderMail.md) | [Next](Server.md)

# IMTConEmail::SenderName

Get the email sender's name in the mail server configuration.

C++
    
    
    LPCWSTR  IMTConEmail::SenderName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConEmail.SenderName()

Python
    
    
    MTConEmail.SenderName

### Return Value

If successful, the method returns a pointer to a string with the sender's name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConEmail](../IMTConEmail.md) object.

# IMTConEmail::SenderName

Set the email sender's name in the mail server configuration.

C++
    
    
    MTAPIRES  IMTConEmail::SenderName(
       LPCWSTR  name      // Sender's name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.SenderName(
       srting   name      // Sender's name
       )

Python
    
    
    MTConEmail.SenderName

### Parameters

**name**  
[in] Email sender name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum name length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
