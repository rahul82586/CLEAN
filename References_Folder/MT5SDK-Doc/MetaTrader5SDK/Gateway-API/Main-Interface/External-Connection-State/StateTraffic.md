[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [External Connection State](../External-Connection-State.md) / StateTraffic

[Previous](StateConnect.md) | [Next](../Client-Connection.md)

# IMTGatewayAPI::StateTraffic

Add the value to the external connection traffic counter.

C++
    
    
    MTAPIRES  IMTGatewayAPI::StateTraffic(
       const UINT  received_bytes,     // Incoming traffic
       const UINT  sent_bytes          // Outgoing traffic
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.StateTraffic(
       uint        received,           // Incoming traffic
       uint        sent                // Outgoing traffic
       )

### Parameters

**received_bytes**  
[in] Incoming traffic in bytes.

**sent_bytes**  
[in] Outgoing traffic in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Incoming and outgoing traffic values passed using this method are added to the current values.
