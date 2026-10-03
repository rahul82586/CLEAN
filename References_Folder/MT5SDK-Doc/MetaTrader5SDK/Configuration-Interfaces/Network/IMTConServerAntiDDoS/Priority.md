[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / Priority

[Previous](Clear.md) | [Next](AccessMask.md)

# IMTConServerAntiDDoS::Priority

Gets the basic priority of the Anti-DDoS server.

C++
    
    
    UINT  IMTConServerAntiDDoS::Priority()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAntiDDoS.Priority()

Python (Manager API)
    
    
    MTConServerAntiDDoS.Priority

### Return Value

A value from 0 (the highest priority) to 255 (the "idle" priority for creating backup Anti DDoS servers). The main priority values ​​are described in the [IMTConServerAntiDDoS::EnServerPriority (#enserverpriority)](Enumerations.md#enserverpriority) enumeration.

# IMTConServerAntiDDoS::Priority

Sets the basic priority of the Anti-DDoS server.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::Priority(
       const UINT  priority      // Priority
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.Priority(
       uint        priority      // Priority
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.Priority

### Parameters

**priority**  
[in] The basic priority of the Anti-DDoS server. Set asa value from 0 (the highest priority) to 255 (the "idle" priority for creating backup Anti DDoS servers). The main priority values ​​are described in theIMTConServerAntiDDoS::EnServerPriorityenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
