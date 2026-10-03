[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnGatewayAccountAnswer

[Previous](OnGatewayAccountSet.md) | [Next](OnDealerAnswer.md)

# IMTGatewaySink::OnGatewayAccountAnswer

This is a handler for an event of receiving a result of a request for MetaTrader 5 platform user data. This handler receives a user data requested via [IMTGatewayAPI::GatewayAccountRequest](../Main-Interface/Synchronizing-Trading-Data/GatewayAccountRequest.md) method.

C++
    
    
    virtual void  IMTGatewaySink::OnGatewayAccountAnswer(
       const MTAPIRES          retcode,          // Result
       const INT64             request_id,       // Request ID
       const IMTUser*          user              // An object of a client record
       const IMTAccount*       account           // An object of a trading account
       const IMTOrderArray*    orders            // Array of orders
       const IMTPositionArray* positions         // Positions array
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnGatewayAccountAnswer(
       MTRetCode               retcode,          // Result
       long                    request_id,       // Request ID
       CIMTUser                user              // An object of a client record
       CIMTAccount             account           // An object of a trading account
       CIMTOrderArray          orders            // Array of orders
       CIMTPositionArray       positions         // Positions array
       )

### Parameters

**retcode**  
[in] Code of the data request processing result. MT_RET_OK response code is returned if the data has been successfully received. Otherwise, the appropriateerror codeis returned.

**request_id**  
[in] Request ID. It is used for binding the requests executed byIMTGatewayAPI::GatewayAccountRequestmethod and the answers received via this handler.

***user**  
[in]An object of the client record. OnlyLoginfield and a client account number in an external trading system are passed in IMTUser objectIMTUser::ExternalAccountGetmethod should be used to receive a client account number).

***account**  
[in]Trading account object. OnlyBalancefield is used in IMTAccount object for passing the actual balance value.

***orders**  
[in]An object of the array ofclient orders.

***positions**  
[in]An object of the array ofclient positions.

### 
