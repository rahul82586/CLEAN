[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / GroupDelete

[Previous](GroupShift.md) | [Next](GroupClear.md)

# IMTConGateway::GroupDelete

Delete [a group](../../Groups.md) with a specified index from the list of groups, trade operations of which are processed by the gateway.

C++
    
    
    MTAPIRES  IMTConGateway::GroupDelete(
       const UINT  pos      // Position of the group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCOde  CIMTConGateway.GroupDelete(
       uint        pos      // Position of the group
       )

Python (Manager API)
    
    
    MTConGateway.GroupDelete(
       pos         # Position of the group
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
