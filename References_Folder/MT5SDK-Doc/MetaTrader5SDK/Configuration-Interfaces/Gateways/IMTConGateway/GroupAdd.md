[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / GroupAdd

[Previous](SymbolNext.md) | [Next](GroupUpdate.md)

# IMTConGateway::GroupAdd

Add [a group](../../Groups.md), trade operations from which will be processed by the gateway.

C++
    
    
    MTAPIRES  IMTConGateway::GroupAdd(
       LPCWSTR  path      // Path to the group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.GroupAdd(
       string   path      // Path to the group
       )

Python (Manager API)
    
    
    MTConGateway.GroupAdd(
       path     # Path to the group
       )

### Parameters

**path**  
[in] Path to a group in accordance with the hierarchy of groups in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGroup::Group](../../Groups/IMTConGroup/Group.md) value is used as the path to the group.
