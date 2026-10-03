[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Server

[Previous](SenderName.md) | [Next](Login.md)

# IMTConEmail::Server

Get the SMTP server address in the mail server configuration.

C++
    
    
    LPCWSTR  IMTConEmail::Server()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConEmail.Server()

Python
    
    
    MTConEmail.Server

### Return Value

If successful, it returns a pointer to a string with the SMTP server address. Otherwise, NULL is returned.

### Note

The address includes a port for connection, separated by a colon.

# IMTConEmail::Server

Set the SMTP server address in the mail server configuration.

C++
    
    
    MTAPIRES  IMTConEmail::Server(
       LPCWSTR  server    // SMTP server
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.Server(
       srting   server    // SMTP server
       )

Python
    
    
    MTConEmail.Server

### Parameters

**name**  
[in] The SMTP server address and port for connection separated by a colon.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum address length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
