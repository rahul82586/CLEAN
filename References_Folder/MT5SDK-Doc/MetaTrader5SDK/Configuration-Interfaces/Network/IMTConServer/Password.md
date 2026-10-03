[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Password

[Previous](Id.md) | [Next](PasswordCheck.md)

# IMTConServer::Password

Set the server password.

C++
    
    
    MTAPIRES  IMTConServer::Password(
       LPCWSTR  password      // Server password
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.Password(
       string   password      // Server password
       )

Python (Manager API)
    
    
    MTConServer.Password(
       password  # Server password
       )

### Parameters

**password**  
[in] Server password.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The must be no less than five symbols long and contain at least two of three symbols types (lower-case letters, upper-case letters or digits).
