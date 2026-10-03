[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnGatewayStart

[Previous](OnGatewayConfig.md) | [Next](OnGatewayStop.md)

# IMTGatewaySink::OnGatewayStart

A handler of the following event: Gateway API is [synchronized](../Interaction-of-the-Platform-and.md) with the platform and is ready for work.

C++
    
    
    virtual void  IMTGatewaySink::OnGatewayStart()

.NET
    
    
    virtual void  CIMTGatewaySink.OnGatewayStart()

### Note

Gateway API business logic elements methods (adding of [symbols](../Main-Interface/Configuration-Databases/Symbols.md), connection as a [dealer](../Main-Interface/Processing-Trade-Requests.md), etc.).
