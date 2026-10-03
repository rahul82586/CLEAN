[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnGatewayAccountSet

[Previous](OnGatewayShutdown.md) | [Next](OnGatewayAccountAnswer.md)

# IMTGatewayAPI::OnGatewayAccountSet

This handler receives [IMTGatewayAPI::GatewayAccountSet](../Main-Interface/Synchronizing-Trading-Data/GatewayAccountSet.md) method execution result, as well as the final status of a client entry (after the passed changes have been applied).

C++
    
    
    MTAPIRES  IMTGatewayAPI::OnGatewayAccountSet(
       const MTAPIRES          retcode,          // Result
       const INT64             request_id        // Request ID
       const IMTUser*          user              // An object of a client record
       const IMTAccount*       account           // An object of a trading account
       const IMTOrderArray*    orders            // Array of orders
       const IMTPositionArray* positions         // Positions array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.OnGatewayAccountSet(
       MTRetCode               retcode,          // Result
       long                    request_id        // Request ID
       CIMTUser                user              // An object of a client record
       CIMTAccount             account           // An object of a trading account
       CIMTOrderArray          orders            // Array of orders
       CIMTPositionArray       positions         // Positions array
       )

### Parameters

**retcode**  
[in]IMTGatewayAPI::GatewayAccountSetexecution result code. MT_RET_OK response code is passed if a client entry has been successfully changed. Otherwise, the appropriateerror codeis returned.

**request_id**  
[in] Arbitrary request ID. It is used for binding the requests executed byIMTGatewayAPI::GatewayAccountSetmethod and the answers received via this handler.

**user**  
[in]An object of the client record.Loginfield is used in IMTUser object for identifying a user, whose data has been changed. The client external system's account number corresponding to the gateway can also be used for identification. Account in an external system can be defined usingIMTUser::ExternalAccountAddmethod.

**account**  
[in]Trading account object. OnlyBalancefield is used in IMTAccount object for passing the balance value.

**orders**  
[in]An object of the array of ordersplaced for the specified account.

**positions**  
[in]An object of the array of positionsplaced for the specified account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After a client's data is changed using [IMTGatewayAPI::GatewayAccountSet](../Main-Interface/Synchronizing-Trading-Data/GatewayAccountSet.md) method, the status of the client's trading account, orders and positions is passed to account, orders and positions parameters.
