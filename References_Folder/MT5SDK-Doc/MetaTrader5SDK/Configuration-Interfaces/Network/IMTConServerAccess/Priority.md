[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / Priority

[Previous](Clear.md) | [Next](PriorityCurrent.md)

# IMTConServerAccess::Priority

Get the base priority of the Access Server.

C++
    
    
    UINT  IMTConServerAccess::Priority()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerAccess.Priority()

Python (Manager API)
    
    
    MTConServerAccess.Priority

### Return Value

A value from 0 (the highest priority) to 255 (the "idle" priority for creating backup access servers). The main priority values ​​are described in the [IMTConServerAccess::EnServerPriority (#enserverpriority)](Enumerations.md#enserverpriority) enumeration.

# IMTConServerAccess::Priority

Set the base priority of the Access Server.

C++
    
    
    MTAPIRES  IMTConServerAccess::Priority(
       const UINT  priority      // Priority
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.Priority(
       uint        priority      // Priority
       )

Python (Manager API)
    
    
    MTConServerAccess.Priority

### Parameters

**priority**  
[in] Base priority of the Access Server. Is set by a valuefrom 0 (the highest priority) to 255 (the "idle" priority for creating backup access servers). The main priority values ​​are described in theIMTConServerAccess::EnServerPriorityenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
