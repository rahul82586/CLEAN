[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewaySink](../IMTConGatewaySink.md) / OnGatewayUpdate

[Previous](OnGatewayAdd.md) | [Next](OnGatewayDelete.md)

# IMTConGatewaySink::OnGatewayUpdate

A handler of the event of updating a gateway configuration.

C++
    
    
    virtual void  IMTConGatewaySink::OnGatewayUpdate(
       const IMTConGateway*  gateway      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConGatewaySink.OnGatewayUpdate(
       CIMTConGateway        gateway      // Configuration object
       )

### Parameters

**gateway**  
[in] A pointer to the updated configuration object.

### Note

This method is called by the API to notify that a gateway configuration has changed.
