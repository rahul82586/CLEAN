[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / GatewayLogin

[Previous](GatewayServer.md) | [Next](GatewayPassword.md)

# IMTConFeeder::GatewayLogin

Gets a login for the authorization of the history server on the gateway server.

C++
    
    
    UINT64  IMTConFeeder::GatewayLogin()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConFeeder.GatewayLogin()

Python (Manager API)
    
    
    MTConFeeder.GatewayLogin

### Return Value

Login for authorization.

### Note

Similar to gateways, all data feeds use Gateway API for operation. In order to connect a history server to the gateway server (developed using Gateway API), you need to specify authorization parameters. These parameters are designed for security purposes, as well as for ease of debugging of data feeds for third-party developers. If you do not need debugging, you can specify any login and password, as well as any available network address, through which the interaction of the data feed with the server will be implemented.

# IMTConFeeder::GatewayLogin

Sets a login for the authorization of the history server on the gateway server.

C++
    
    
    MTAPIRES  IMTConFeeder::GatewayLogin(
       UINT64  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.GatewayLogin(
       ulong   login      // Login
       )

Python (Manager API)
    
    
    MTConFeeder.GatewayLogin

### Parameters

**login**  
[in] A login for authorization on a data feed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Only positive numbers can be used for the login.
