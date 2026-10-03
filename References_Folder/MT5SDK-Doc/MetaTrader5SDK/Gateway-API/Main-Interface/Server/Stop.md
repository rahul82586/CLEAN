[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Server](../Server.md) / Stop

[Previous](Start.md) | [Next](IP.md)

# IMTGatewayAPI::Stop

Gateway API server port stop.

C++
    
    
    MTAPIRES  IMTGatewayAPI::Stop()

.NET
    
    
    MTRetCode CIMTGatewayAPI.Stop()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After [IMTGatewayAPI::Start](Start.md) call, the object which implements the [IMTGatewaySink](../../Event-Interface.md) interface is considered subscribed to notifications from the Gateway API. Such an object can only be deleted after calling IMTGatewayAPI::Stop. 
