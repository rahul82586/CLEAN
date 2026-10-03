[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / Server

[Previous](Group.md) | [Next](PermissionsFlags.md)

# IMTConGroup::Server

Get the ID of the trade server, to which the group is linked.

C++
    
    
    UINT64  IMTConGroup::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroup.Server()

Python (Manager API)
    
    
    MTConGroup.Server

### Return Value

The ID of the trade server, to which the group is linked.

# IMTConGroup::Server

Set the ID of the trade server, to which the group is linked.

C++
    
    
    MTAPIRES  IMTConGroup::Server(
       const UINT64  server      // Server ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.Server(
       ulong         server      // Server ID
       )

Python (Manager API)
    
    
    MTConGroup.Server

### Parameters

**server**  
[in] The ID of the server, to which the group is linked.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
