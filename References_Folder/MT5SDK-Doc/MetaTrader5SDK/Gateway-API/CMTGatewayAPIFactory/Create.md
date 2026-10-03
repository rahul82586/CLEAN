[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [CMTGatewayAPIFactory](../CMTGatewayAPIFactory.md) / Create

[Previous](Shutdown.md) | [Next](LicenseCheck.md)

# CMTGatewayAPIFactory::Create

Create an instance of the [IMTGatewayAPI](../Main-Interface.md) interface.

C++
    
    
    MTAPIRES  CMTGatewayAPIFactory::Create(
       MTGatewayInfo&  info,          // The MTGatewayInfo structure
       IMTGatewayAPI** gateway,       // A pointer to the pointer to the API interface
       int             argc=0,        // The number of command line parameters
       wchar_t**       argv=NULL      // Command line parameters
       )

.NET
    
    
    CIMTGatewayAPI  SMTGatewayAPIFactory.CreateGateway(
       MTGatewayInfo   info,          // The MTGatewayInfo structure
       string[]        arguments,     // Command line parameters
       out MTRetCode   res            // Response code
       )

### Parameters

**info**  
[in] TheMTGatewayInfostructure that describes the parameters of the gateway/data feed module.

**gateway**  
[out] A pointer to a pointer to the created instance of theIMTGatewayAPIinterface.

**argc=0**  
[in] The number of additional parameters of a command line that is used for running the gateway/data feed. The default value is 0.

**argv=NULL**  
[in] Additional parameters of the command line that is used for running the gateway/data feed. The default value is NULL.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Gateways/data feeds support the launch with the [additional command line parameters (#param)](../Exported-Functions/MTGatewayCreateLocal.md#param). In particular, the /description command line parameter is additionally used by the history server to get the description of the gateway/data feed module. Always pass the command line parameters to the CMTGatewayAPIFactory::Create method, so that the module is correctly downloaded and managed by the history server.

  * in command line parameters passed to CMTGatewayAPIFactory::Create (/name:XXX /address:XXX), or
  * in the [configuration file (#config)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_gateways/gateway_service#config) (name=XXX, address=XXX)


