[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConClusterState](../IMTConClusterState.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConClusterState::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConClusterState::Assign(
       const IMTConClusterState*    param  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  IMTConClusterState.Assign(
       CIMTConClusterState          param  // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
