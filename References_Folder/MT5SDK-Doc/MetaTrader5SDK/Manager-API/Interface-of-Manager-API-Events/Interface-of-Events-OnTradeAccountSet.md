[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Interface of Manager API Events](../Interface-of-Events.md) / Interface of Events OnTradeAccountSet

[Previous](Interface-of-Events-OnDisconnect.md) | [Next](../../Gateway-API/README.md)

# IMTManagerSink::OnTradeAccountSet

This handler receives [IMTManagerAPI::TradeAccountSet](../Manager-Interface/Trade-Activity/Monitoring-Account-States/TradeAccountSet.md) method execution result, as well as the final status of a client entry (after the passed changes have been applied).

C++
    
    
    virtual void  IMTManagerSink::OnTradeAccountSet(
       const MTAPIRES          retcode,          // Result
       const INT64             request_id        // Request ID
       const IMTUser*          user              // An object of a client record
       const IMTAccount*       account           // An object of a trading account
       const IMTOrderArray*    orders            // Array of orders
       const IMTPositionArray* positions         // Positions array
       )

.NET
    
    
    virtual void  CIMTManagerSink.OnTradeAccountSet(
       MTRetCode               retcode,          // Result
       long                    request_id        // Request ID
       CIMTUser                user              // An object of a client record
       CIMTAccount             account           // An object of a trading account
       CIMTOrderArray          orders            // Array of orders
       CIMTPositionArray       positions         // Positions array
       )

### Parameters

**retcode**  
[in]IMTManagerAPI::TradeAccountSetexecution result code. MT_RET_OK response code is passed if a client entry has been successfully changed. Otherwise, the appropriateerror codeis returned.

**request_id**  
[in] Arbitrary request ID. It is used for binding the requests executed byIMTManagerAPI::TradeAccountSetmethod and the answers received via this handler.

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

After a client's data is changed using [IMTManagerAPI::TradeAccountSet](../Manager-Interface/Trade-Activity/Monitoring-Account-States/TradeAccountSet.md) method, the status of the client's trading account, orders and positions is passed to account, orders and positions parameters.
