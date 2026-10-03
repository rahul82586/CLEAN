[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnGatewayShutdown

[Previous](OnGatewayStop.md) | [Next](OnGatewayAccountSet.md)

# IMTGatewaySink::OnGatewayShutdown

A handler of the event notifying about the trading platform shutdown or gateway/data feed disconnection.

C++
    
    
    virtual void  IMTGatewaySink::OnGatewayShutdown(
       const UINT64  login      // Login
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnGatewayShutdown(
       ulong         login      // Login
       )

### Parameters

**login**  
[in] Login of the platform component from which the shutdown event has been received.

### Note

This event allows the programmer to gracefully terminate the gateway/datafeed. After receiving the event, the application must stop operation; otherwise, the process will be stopped forcibly after 5 seconds.
