[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConClusterState](../IMTConClusterState.md) / Clear

[Previous](Assign.md) | [Next](Id.md)

# IMTConClusterState::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConClusterState::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  IMTConClusterState.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears all fields ​​and removes nested objects.
