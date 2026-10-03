[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Synchronizing Trading Data](../Synchronizing-Trading-Data.md) / GatewayAccountRequest

[Previous](GatewayAccountAnswer.md) | [Next](GatewayAccountSet.md)

# IMTGatewayAPI::GatewayAccountRequest

This method allows Gateway API to request information about a user state in MetaTrader 5 platform. Request result and the requested information are passed to [IMTGatewayAPI::OnGatewayAccountAnswer](../../Event-Interface/OnGatewayAccountAnswer.md) handler.

C++
    
    
    MTAPIRES  IMTGatewaySink::GatewayAccountRequest(
       const INT64    request_id,  // Request ID
       const IMTUser* user         // Login
       )

.NET
    
    
    MTRetCode  CIMTGatewaySink.GatewayAccountRequest(
       long           request_id,  // Request ID
       CIMTUser       user         // Login
       )

### Parameters

**request_id**  
[in] Arbitrary request ID. It is used for binding the requests executed by this method and the answers received viaIMTGatewayAPI::OnGatewayAccountAnswer.

**user**  
[in]An object of the client record.Loginfield is used in IMTUser object for identifying a user, for whom data request is performed. The client external system's account number corresponding to the gateway can also be used for identification. Account in an external system can be defined usingIMTUser::ExternalAccountAddmethod.

### Return Value

An indication of a successful placing of a request to the processing queue is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
