[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Password

[Previous](Login.md) | [Next](Flags.md)

# IMTConEmail::Password

Get the SMTP password in the mail server configuration.

C++
    
    
    LPCWSTR  IMTConEmail::Password()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConEmail.Password()

Python
    
    
    MTConEmail.Password

### Return Value

If successful, the method returns a pointer to a string with the SMTP password. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConEmail](../IMTConEmail.md) object.

# IMTConEmail::Password

Set the SMTP password in the mail server configuration.

C++
    
    
    MTAPIRES  IMTConEmail::Password(
       LPCWSTR  server    // SMTP password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.Password(
       srting   server    // SMTP password
       )

Python
    
    
    MTConEmail.Password

### Parameters

**name**  
[in] SMTP password for accessing the account on the mail server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum password length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
