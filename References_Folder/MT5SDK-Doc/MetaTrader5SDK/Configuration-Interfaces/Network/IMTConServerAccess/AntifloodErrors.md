[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / AntifloodErrors

[Previous](AntifloodConnects.md) | [Next](PointsAdd.md)

# IMTConServerAccess::AntifloodErrors

Get the maximum number of incorrect connections, after which the IP address is temporarily blocked.

C++
    
    
    UINT  IMTConServerAccess::AntifloodErrors()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAccess.AntifloodErrors()

Python (Manager API)
    
    
    MTConServerAccess.AntifloodErrors

### Return Value

The maximum number of incorrect connections.

# IMTConServerAccess::AntifloodErrors

Set the maximum number of incorrect connections, after which the IP address is temporarily blocked.

C++
    
    
    MTAPIRES  IMTConServerAccess::AntifloodErrors(
       const UINT  errors      // The number of incorrect connections
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.AntifloodErrors(
       uint        errors      // The number of incorrect connections
       )

Python (Manager API)
    
    
    MTConServerAccess.AntifloodErrors

### Parameters

**errors**  
[in] The maximum number of incorrect connections.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
