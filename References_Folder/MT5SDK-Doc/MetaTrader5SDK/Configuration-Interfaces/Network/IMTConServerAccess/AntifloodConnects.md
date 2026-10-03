[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / AntifloodConnects

[Previous](AntifloodEnabled.md) | [Next](AntifloodErrors.md)

# IMTConServerAccess::AntifloodConnects

Get the maximum number of connections from one IP address for a certain period of time. When the limit is exceeded, the address is temporarily blocked.

C++
    
    
    UINT  IMTConServerAccess::AntifloodConnects()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAccess.AntifloodConnects()

Python (Manager API)
    
    
    MTConServerAccess.AntifloodConnects

### Return Value

Maximum number of connections from one IP address.

# IMTConServerAccess::AntifloodConnects

Set the maximum number of connections from one IP address for a certain period of time. When the limit is exceeded, the address is temporarily blocked.

C++
    
    
    MTAPIRES  IMTConServerAccess::AntifloodConnects(
       const UINT  connects      // Number of connections
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.AntifloodConnects(
       uint        connects      // Number of connections
       )

Python (Manager API)
    
    
    MTConServerAccess.AntifloodConnects

### Parameters

**connects**  
[in] The maximum number of connections.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
