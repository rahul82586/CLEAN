[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Group

[Previous](IMTMatching-Server.md) | [Next](IMTMatching-State.md)

# IMTECNMatching::Group

Get the group of the client who has placed the matching order.

C++
    
    
    UINT64  IMTECNMatching::Group()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNMatching.Group()

### Return Value

The group of the client who has placed the matching order.

# IMTECNMatching::Group

Set the group of the client who has placed the matching order.

C++
    
    
    MTAPIRES  IMTECNMatching::Group(
       const UINT64  group     // group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Group(
       ulong         group     // group
       )

### Parameters

**group**  
[in] The group of the client who has placed the matching order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
