[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TradingLogin

[Previous](TradingServer.md) | [Next](TradingPassword.md)

# IMTConGateway::TradingLogin

Get a login for the authorization of a gateway on the source server.

C++
    
    
    LPCWSTR  IMTConGateway::TradingLogin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.TradingLogin()

Python (Manager API)
    
    
    MTConGateway.TradingLogin

### Return Value

If successful, it returns a pointer to a string with login for authorization on the source server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](../IMTConGateway.md) object.

To use the string after the object removal (call of the [IMTConGateway::Release](Release.md) method of this object), a copy of it should be created.

# IMTConGateway::TradingLogin

Set a login for the authorization of a gateway on the source server.

C++
    
    
    MTAPIRES  IMTConGateway::TradingLogin(
       LPCWSTR  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TradingLogin(
       string   login      // Login
       )

Python (Manager API)
    
    
    MTConGateway.TradingLogin

### Parameters

**login**  
[in] A login for authorization.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum login length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
