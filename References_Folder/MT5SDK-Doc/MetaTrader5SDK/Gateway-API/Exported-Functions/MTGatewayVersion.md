[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Exported Functions](../Exported-Functions.md) / MTGatewayVersion

[Previous](../Exported-Functions.md) | [Next](MTGatewayCreate.md)

# MTGatewayVersion

MTGatewayVersion exported function returns Gateway API library version.
    
    
    MTAPIRES  MTGatewayVersion(
       UINT&  version      // Reference to a Gateway API version
       )

### Parameters

**version**  
[in] A reference to a Gateway API version.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
