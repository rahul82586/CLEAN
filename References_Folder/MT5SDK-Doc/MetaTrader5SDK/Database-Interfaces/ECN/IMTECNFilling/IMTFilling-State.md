[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling State

[Previous](IMTFilling-ExternalID.md) | [Next](IMTFilling-Symbol.md)

# IMTECNFilling::State

Get the current state of the filling order.

C++
    
    
    UINT  IMTECNFilling::State()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNFilling.State()

### Return Value

[IMTECNMatching::ENCMatchingState (#encmatchingstate)](../IMTECNMatching/IMTMatching-Enumerations.md#encmatchingstate) enumeration value.

# IMTECNMatching::State

Set the state of the filling order.

C++
    
    
    MTAPIRES  IMTECNFilling::StateSet(
       const UINT  state     // order state
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.StateSet(
       uint        state     // order state
       )

### Parameters

**state**  
[in] Order state. The state is passed using theIMTECNMatching::ENCMatchingStateenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
