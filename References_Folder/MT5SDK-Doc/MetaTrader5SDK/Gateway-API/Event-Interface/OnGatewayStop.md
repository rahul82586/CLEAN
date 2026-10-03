[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnGatewayStop

[Previous](OnGatewayStart.md) | [Next](OnGatewayShutdown.md)

# IMTGatewaySink::OnGatewayStop

[IMTGatewaySink::OnGatewayStart](OnGatewayStart.md) inverse events handler. The notification is on the fact that Gateway API is not synchronized with the platform and not ready for work.

C++
    
    
    virtual void  IMTGatewaySink::OnGatewayStop()

.NET
    
    
    virtual void  CIMTGatewaySink.OnGatewayStop()

### Note

This notification is sent for gateways, in case of the failure of the connection to a main trading or historical server.
