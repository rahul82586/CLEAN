[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / AddressNext

[Previous](AddressTotal.md) | [Next](AddressIPv6.md)

# IMTConServer::AddressNext

Get an available IPv4 address by the index.

C++
    
    
    UINT  IMTConServer::AddressNext(
       const UINT  pos      // Position of the IP address
       )  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.AddressNext(
       uint        pos      // Position of the IP address
       )

Python (Manager API)
    
    
    MTConServer.AddressNext(
       pos         # Position of the IP address
       )

### Parameters

**pos**  
[in] Position of the address in the list of availableIPv4addresses.

### Return Value

IP address at the specified position.

### Note

The address is specified in the format address:port.
