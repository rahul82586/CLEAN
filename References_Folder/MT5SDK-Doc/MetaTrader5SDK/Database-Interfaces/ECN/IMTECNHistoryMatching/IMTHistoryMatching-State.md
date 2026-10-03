[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching State

[Previous](IMTHistoryMatching-Server.md) | [Next](IMTHistoryMatching-TimeSetupMsc.md)

# IMTECNHistoryMatching::State

Get the current state of the matching order.

C++
    
    
    UINT  IMTECNHistoryMatching::State()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryMatching.State()

### Return Value

[IMTECNMatching::ENCMatchingState (#encmatchingstate)](../IMTECNMatching/IMTMatching-Enumerations.md#encmatchingstate) enumeration value.

# IMTECNHistoryMatching::State

Set the state of the matching order.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::StateSet(
       const UINT  state     // order state
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.StateSet(
       uint        state     // order state
       )

### Parameters

**state**  
[in] Order state. The state is passed using theIMTECNMatching::ENCMatchingStateenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
