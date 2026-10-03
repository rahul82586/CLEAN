[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / SenderMail

[Previous](Name.md) | [Next](SenderName.md)

# IMTConEmail::SenderMail

Get the email address, from which emails are sent via the mail server configurations.

C++
    
    
    LPCWSTR  IMTConEmail::SenderMail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConEmail.SenderMail()

Python
    
    
    MTConEmail.SenderMail

### Return Value

If successful, the method returns a pointer to a string with the sender email. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConEmail](../IMTConEmail.md) object.

You should create a string copy if you want to use it after the object removal (call of the [IMTConEmail::Release](Release.md) method of this object).

# IMTConEmail::SenderMail

Set the email address, from which emails will be sent via the mail server configurations.

C++
    
    
    MTAPIRES  IMTConEmail::SenderMail(
       LPCWSTR  mail      // Sender email
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.SenderMail(
       srting   mail      // Sender email
       )

Python
    
    
    MTConEmail.SenderMail

### Parameters

**mail**  
[in] The email address from which emails will be sent.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum email length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
