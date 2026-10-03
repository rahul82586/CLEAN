[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching State

[Previous](IMTMatching-Group.md) | [Next](IMTMatching-Flags.md)

# IMTECNMatching::State

Get the current state of the matching order.

C++
    
    
    UINT  IMTECNMatching::State()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNMatching.State()

### Return Value

[IMTECNMatching::ENCMatchingState (#encmatchingstate)](IMTMatching-Enumerations.md#encmatchingstate) enumeration value.

# IMTECNMatching::State

Set the state of the matching order.

C++
    
    
    MTAPIRES  IMTECNMatching::StateSet(
       const UINT  state     // order state
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.StateSet(
       uint        state     // order state
       )

### Parameters

**state**  
[in] Order state. The state is passed using theIMTECNMatching::ENCMatchingStateenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
