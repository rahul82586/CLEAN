[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Flags

[Previous](Requests-Group.md) | [Next](Requests-Symbol.md)

# IMTExecution::Flags

Gets additional flags of a trade execution.

C++
    
    
    UINT64  IMTExecution::Flags()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.Flags()

### Return Value

Additional trade execution flags passed using the [IMTExecution::EnFlags (#enflags)](Requests-Enumerations.md#enflags) enumeration.

# IMTExecution::Flags

Sets additional flags of a trade execution.

C++
    
    
    MTAPIRES  IMTExecution::Flags(
       const UINT64  flags      // Additional trade execution flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Flags(
       ulong         flags      // Additional trade execution flags
       )

### Parameters

**flags**  
[in] Additional trade execution flags passed using theIMTExecution::EnFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
