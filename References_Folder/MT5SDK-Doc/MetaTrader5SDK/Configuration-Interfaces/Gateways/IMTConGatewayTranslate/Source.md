[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayTranslate](../IMTConGatewayTranslate.md) / Source

[Previous](Clear.md) | [Next](Symbol.md)

# IMTConGatewayTranslate::Source

Get the symbol name in the data feed, to which the gateway connects.

C++
    
    
    LPCWSTR  IMTConGatewayTranslate::Source()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGatewayTranslate.Source()

Python (Manager API)
    
    
    MTConGatewayTranslate.Source

### Return Value

If successful, it returns a pointer to a string with the symbol name if the data feed. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGatewayTranslate](../IMTConGatewayTranslate.md) object.

# IMTConGatewayTranslate::Source

Set the symbol name in the data feed, to which the gateway connects.

C++
    
    
    MTAPIRES  IMTConGatewayTranslate::Source(
       LPCWSTR  source      // The name of a symbol in a data feed
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGatewayTranslate.Source(
       string   source      // The name of a symbol in a data feed
       )

Python (Manager API)
    
    
    MTConGatewayTranslate.Source

### Parameters

**source**  
[in] The name of a symbol in a data feed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the name is limited to 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
