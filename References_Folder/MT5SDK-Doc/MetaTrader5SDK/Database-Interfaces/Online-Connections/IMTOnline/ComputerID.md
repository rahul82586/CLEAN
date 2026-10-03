[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnline](../IMTOnline.md) / ComputerID

[Previous](Time.md) | [Next](../IMTOnlineArray.md)

# IMTOnline::ComputerID

Get CID, i.e. the unique ID of the computer from which the user connected to the server.

C++
    
    
    LPCWSTR  IMTOnline::ComputerID(
       MTAPISTR&  cid     // computer ID format string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTOnline.ComputerID()

### Parameters

**cid**  
[in] Computer ID format string

### Return Value

If successful, it returns a pointer to a passed string filled with computer ID value. In case the CID is not available, an empty string is returned.
