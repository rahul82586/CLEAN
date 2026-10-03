[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / Name

[Previous](Clear.md) | [Next](ID.md)

# IMTConGateway::Name

Get the gateway name.

C++
    
    
    LPCWSTR  IMTConGateway::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.Name()

Python (Manager API)
    
    
    MTConGateway.Name

### Return Value

If successful, it returns a pointer to a string with the name of the gateway. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](../IMTConGateway.md) object.

# IMTConGateway::Name

Set the gateway name.

C++
    
    
    MTAPIRES  IMTConGateway::Name(
       LPCWSTR  name      // The gateway name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.Name(
       string   name      // The gateway name
       )

Python (Manager API)
    
    
    MTConGateway.Name

### Parameters

**name**  
[in] The gateway name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
