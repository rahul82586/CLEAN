[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Login

[Previous](Server.md) | [Next](Password.md)

# IMTConEmail::Login

Get the SMTP login in the mail server configuration.

C++
    
    
    LPCWSTR  IMTConEmail::Login()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConEmail.Login()

Python
    
    
    MTConEmail.Login

### Return Value

If successful, the method returns a pointer to a string with the SMTP login. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConEmail](../IMTConEmail.md) object.

# IMTConEmail::Login

Set the SMTP login in the mail server configuration.

C++
    
    
    MTAPIRES  IMTConEmail::Login(
       LPCWSTR  login     // SMTP login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.Login(
       srting   login     // SMTP login
       )

Python
    
    
    MTConEmail.Login

### Parameters

**login**  
[in] SMTP login for accessing the account on the mail server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum login length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
