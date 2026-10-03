[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Name

[Previous](Clear.md) | [Next](SenderMail.md)

# IMTConEmail::Name

Get the mail server configuration name.

C++
    
    
    LPCWSTR  IMTConEmail::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConEmail.Name()

Python
    
    
    MTConEmail.Name

### Return Value

If successful, it returns a pointer to a string with the mail server name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConEmail](../IMTConEmail.md) object.

# IMTConEmail::Name

Set the mail server configuration name.

C++
    
    
    MTAPIRES  IMTConEmail::Name(
       LPCWSTR  name      // Mail server name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.Name(
       srting   name      // Mail server name
       )

Python
    
    
    MTConEmail.Name

### Parameters

**name**  
[in] Mail server name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum name length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
