[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnline](../IMTOnline.md) / Address

[Previous](Group.md) | [Next](Type.md)

# IMTOnline::Address

Get the IP address from which the user connected to the server.

C++
    
    
    LPCWSTR  IMTOnline::Address(
       MTAPISTR&  ip      // IP address format string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTOnline.Address()

### Parameters

**ip**  
[in] The string in which the IP address is formatted.

### Return Value

If successful, it returns a pointer to a passed string filled with the formatted IP address. In case the IP address is not available, an empty string is returned.
