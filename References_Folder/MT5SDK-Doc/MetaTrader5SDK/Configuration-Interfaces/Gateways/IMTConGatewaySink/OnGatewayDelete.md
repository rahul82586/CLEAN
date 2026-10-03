[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewaySink](../IMTConGatewaySink.md) / OnGatewayDelete

[Previous](OnGatewayUpdate.md) | [Next](OnGatewaySync.md)

# IMTConGatewaySink::OnGatewayDelete

A handler of the event of removing a gateway configuration.

C++
    
    
    virtual void  IMTConGatewaySink::OnGatewayDelete(
       const IMTConGateway*  gateway      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConGatewaySink.OnGatewayDelete(
       CIMTConGateway        gateway      // Configuration object
       )

### Parameters

**gateway**  
[in] A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify that a gateway configuration has been deleted.
