[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests GatewayID

[Previous](Requests-PriceGateway.md) | [Next](Requests-ExternalRetcode.md)

# IMTExecution::GatewayID

Gets the ID of the gateway from which a trade execution has been received. It corresponds to the value of [IMTConGateway::ID](../../../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md).

C++
    
    
    UINT64  IMTExecution::GatewayID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.GatewayID()

### Return Value

The ID of the gateway from which a trade execution has been received.

# IMTExecution::GatewayID

Sets the ID of the gateway from which a trade execution has been received. It corresponds to the value of [IMTConGateway::ID](../../../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md).

C++
    
    
    MTAPIRES  IMTExecution::GatewayID(
       const UINT64  id      // Gateway ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.GatewayID(
       ulong         id      // Gateway ID
       )

### Parameters

**id**  
[in] The ID of the gateway from which a trade execution has been received.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
