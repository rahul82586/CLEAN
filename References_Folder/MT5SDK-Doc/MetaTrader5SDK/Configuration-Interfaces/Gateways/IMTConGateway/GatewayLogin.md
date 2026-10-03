[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / GatewayLogin

[Previous](GatewayServer.md) | [Next](GatewayPassword.md)

# IMTConGateway::GatewayLogin

Gets a login for the authorization of the history and trade servers on the gateway server.

C++
    
    
    UINT64  IMTConGateway::GatewayLogin()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGateway.GatewayLogin()

Python (Manager API)
    
    
    MTConGateway.GatewayLogin

### Return Value

Login for authorization.

### Note

Parameters of connection of the history/trade server to the gateway provide operation security, as well as easy debugging of gateways by third-party developers. If you do not need debugging, you can specify any login and password, as well as any available network address, through which the interaction of the gateway with the platform servers will be implemented.

# IMTConGateway::GatewayLogin

Sets a login for the authorization of the history and trade servers on the gateway server.

C++
    
    
    MTAPIRES  IMTConGateway::GatewayLogin(
       UINT64  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.GatewayLogin(
       ulong   login      // Login
       )

Python (Manager API)
    
    
    MTConGateway.GatewayLogin

### Parameters

**login**  
[in] A login for authorization.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Only positive numbers can be used for the login.
