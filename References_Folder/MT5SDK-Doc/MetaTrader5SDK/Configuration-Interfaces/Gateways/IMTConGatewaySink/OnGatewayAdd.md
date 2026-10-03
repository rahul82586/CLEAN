[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewaySink](../IMTConGatewaySink.md) / OnGatewayAdd

[Previous](../IMTConGatewaySink.md) | [Next](OnGatewayUpdate.md)

# IMTConGatewaySink::OnGatewayAdd

A handler of the event of adding a new gateway configuration.

C++
    
    
    virtual void  IMTConGatewaySink::OnGatewayAdd(
       const IMTConGateway*  gateway      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConGatewaySink.OnGatewayAdd(
       CIMTConGateway*       gateway      // Configuration object
       )

### Parameters

**gateway**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by the API to notify of the fact that a new gateway configuration has been added.
