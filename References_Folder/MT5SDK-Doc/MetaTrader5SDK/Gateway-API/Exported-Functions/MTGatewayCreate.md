[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Exported Functions](../Exported-Functions.md) / MTGatewayCreate

[Previous](MTGatewayVersion.md) | [Next](MTGatewayCreateLocal.md)

# MTGatewayCreate

MTGatewayCreate exported function creates a new [IMTGatewayAPI](../Main-Interface.md) interface copy and returns a pointer to it.
    
    
    MTAPIRES  MTGatewayCreate(
       MTGatewayInfo&   info      // Reference to MTGatewayInfo
       IMTGatewayAPI**  gateway   // Pointer to a pointer o the interface
       )

### Parameters

**info**  
[out] A reference to theMTGatewayInfostructure.

**gateway**  
[out] A pointer to a pointer to the createdIMTGatewayAPIinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
