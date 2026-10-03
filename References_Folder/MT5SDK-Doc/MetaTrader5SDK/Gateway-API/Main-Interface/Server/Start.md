[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Server](../Server.md) / Start

[Previous](../Server.md) | [Next](Stop.md)

# IMTGatewayAPI::Start

Gateway API server port launch.

C++
    
    
    MTAPIRES  IMTGatewayAPI::Start(
       IMTGatewaySink  *sink,            // IMTGatewaySink interface object
       LPCWSTR         address=NULL      // Address
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.Start(
       CIMTGatewaySink sink,             // CIMTGatewaySink interface object
       string[]        address=NULL      // Address
       )

### Parameters

***sink**  
[in]IMTGatewaySinkinterface object for notifications on the platform and Gateway API events.

**address=NULL**  
[in] Address at which the client connections will be accepted. Defined as address:port. Several addresses separated with a comma can be specified here. For example, address1:port1,address2:port2. In case parameter value is not defined, default value is used. Address specified as the command line parameter during the launch of the executed gateway/data feed file is used as the default address. This address is passed in the argc and argv parameters of theCMTGatewayAPIFactory::Createmethod. In case the address is not specified neither in the IMTGatewayAPI::Start method, nor in the command line, the server port will not be launched.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method is called by the server during the gateway/data feed launch.
