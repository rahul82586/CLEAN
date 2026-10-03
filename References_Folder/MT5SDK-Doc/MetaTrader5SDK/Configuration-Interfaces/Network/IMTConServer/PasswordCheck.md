[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / PasswordCheck

[Previous](Password.md) | [Next](ServiceTime.md)

# IMTConServer::PasswordCheck

Check the server password.

C++
    
    
    MTAPIRES  IMTConServer::PasswordCheck(
       LPCWSTR  password      // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.PasswordCheck(
       string   password      // Password
       )

Python (Manager API)
    
    
    MTConServer.PasswordCheck(
       password  # Password
       )

### Parameters

**password**  
[in] A password for checking.

### Return Value

An indication of a successful password check is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code.
