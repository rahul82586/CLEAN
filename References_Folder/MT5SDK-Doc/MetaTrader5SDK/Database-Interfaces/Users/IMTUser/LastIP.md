[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LastIP

[Previous](LastAccess.md) | [Next](Name.md)

# IMTUser::LastIP

Get the IP address from which the user last connected to the server.

C++
    
    
    LPCWSTR  IMTUser::LastIP(
       MTAPISTR&  ip      // IP address format string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.LastIP()

### Parameters

**ip**  
[in][out] The string in which the IP address is formatted.

### Return Value

If successful, it returns a pointer to a passed string filled with the formatted IP address. In case the IP address is not available, an empty string is returned.
