[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / GroupClear

[Previous](GroupDelete.md) | [Next](GroupTotal.md)

# IMTConGateway::GroupClear

Clear the list of [groups](../../Groups.md), trade operations from which are processed by the gateway.

C++
    
    
    MTAPIRES  IMTConGateway::GroupClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.GroupClear()

Python (Manager API)
    
    
    MTConGateway.GroupClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of groups of a gateway.
