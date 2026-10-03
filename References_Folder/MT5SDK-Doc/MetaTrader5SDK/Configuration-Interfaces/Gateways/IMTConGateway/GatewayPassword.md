[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / GatewayPassword

[Previous](GatewayLogin.md) | [Next](Mode.md)

# IMTConGateway::GatewayPassword

Gets a password for the authorization of the trade and history server on the gateway.

C++
    
    
    LPCWSTR  IMTConGateway::GatewayPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.GatewayPassword()

Python (Manager API)
    
    
    MTConGateway.GatewayPassword

### Return Value

If successful, it returns a pointer to a string with a password for authorization on the server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](../IMTConGateway.md) object.

# IMTConGateway::GatewayPassword

Sets a password for the authorization of the trade and history server on the gateway.

C++
    
    
    MTAPIRES  IMTConGateway::GatewayPassword(
       LPCWSTR  password      // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.GatewayPassword(
       string   password      // Password
       )

Python (Manager API)
    
    
    MTConGateway.GatewayPassword

### Parameters

**password**  
[in] A password for authorization.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The password must meet minimum security requirements (be no less than six symbols long and contain at least two of three symbols types: lower-case letters, upper-case letters or digits).
