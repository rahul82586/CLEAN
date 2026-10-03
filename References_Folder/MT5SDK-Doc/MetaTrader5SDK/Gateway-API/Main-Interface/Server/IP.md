[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Server](../Server.md) / IP

[Previous](Stop.md) | [Next](Port.md)

# IMTGatewayAPI::ServerIP

Get the IP address on which the Gateway API server port is running.

C++
    
    
    MTAPIRES  IMTGatewayAPI::ServerIP(
       MTAPISTR&  ip      // IP address
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.ServerIP(
       out string ip      // IP address
       )

### Parameters

**ip**  
[out] IP address on which the server port is running. In case several addresses have been specified viaIMTGatewayAPI::Startmethod, ServerIP method will return them in the same format - separated with a comma. For example, address1:port1,address2:port2.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IP address on which the Gateway API server port is running is determined by the [IMTGatewayAPI::Start](Start.md) method.
