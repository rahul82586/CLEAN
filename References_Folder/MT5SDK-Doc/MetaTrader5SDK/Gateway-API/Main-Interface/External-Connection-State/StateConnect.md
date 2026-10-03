[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [External Connection State](../External-Connection-State.md) / StateConnect

[Previous](../External-Connection-State.md) | [Next](StateTraffic.md)

# IMTGatewayAPI::StateConnect

Set the state of the gateway/data feed external connection.

C++
    
    
    MTAPIRES  IMTGatewayAPI::StateConnect(
       const UINT  state      // Connection state
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.StateConnect(
       bool        state      // Connection state
       )

### Parameters

**state**  
[in] Any value other than 0 means that external connection was established successfully. The 0 value means that connection is absent.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
