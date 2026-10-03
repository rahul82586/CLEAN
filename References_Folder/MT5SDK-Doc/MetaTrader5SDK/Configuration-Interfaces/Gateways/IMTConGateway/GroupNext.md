[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / GroupNext

[Previous](GroupTotal.md) | [Next](TranslateAdd.md)

# IMTConGateway::GroupNext

Get [a group](../../Groups.md) from the list of groups processed by the gateway by the index.

C++
    
    
    LPCWSTR  IMTConGateway::GroupNext(
       const UINT  pos      // Position of the group
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.GroupNext(
       uint        pos      // Position of the group
       )

Python (Manager API)
    
    
    MTConGateway.GroupNext(
       pos         # Position of the group
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the group at the specified position. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](../IMTConGateway.md) object.
