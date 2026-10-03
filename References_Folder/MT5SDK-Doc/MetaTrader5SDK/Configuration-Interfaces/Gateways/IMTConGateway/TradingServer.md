[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TradingServer

[Previous](Module.md) | [Next](TradingLogin.md)

# IMTConGateway::TradingServer

Get the address of the server to which the gateway connects.

C++
    
    
    LPCWSTR  IMTConGateway::TradingServer()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.TradingServer()

Python (Manager API)
    
    
    MTConGateway.TradingServer

### Return Value

If successful, it returns a pointer to a string with the address of the server to which the gateway connects. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](../IMTConGateway.md) object.

# IMTConGateway::TradingServer

Set the address of the server to which the gateway will connect.

C++
    
    
    MTAPIRES  IMTConGateway::TradingServer(
       LPCWSTR  server      // Server address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TradingServer(
       string   server      // Server address
       )

Python (Manager API)
    
    
    MTConGateway.TradingServer

### Parameters

**server**  
[in] Server address.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the address is 128 characters (including the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
