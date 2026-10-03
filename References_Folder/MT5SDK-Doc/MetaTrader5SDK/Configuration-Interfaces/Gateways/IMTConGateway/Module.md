[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / Module

[Previous](ID.md) | [Next](TradingServer.md)

# IMTConGateway::Module

Get the name of a gateway module.

C++
    
    
    LPCWSTR  IMTConGateway::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.Module()

Python (Manager API)
    
    
    MTConGateway.Module

### Return Value

If successful, it returns a pointer to a string with the name of the gateway module. Otherwise, it returns NULL.

### Note

It returns the name of the module (exe-file) that corresponds to the gateway.

# IMTConGateway::Module

Set the name of the gateway module.

C++
    
    
    MTAPIRES  IMTConGateway::Module(
       LPCWSTR  name      // The name of the gateway module
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.Module(
       string   name      // The name of the gateway module
       )

Python (Manager API)
    
    
    MTConGateway.Module

### Parameters

**name**  
[in] The name of the gateway module.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
