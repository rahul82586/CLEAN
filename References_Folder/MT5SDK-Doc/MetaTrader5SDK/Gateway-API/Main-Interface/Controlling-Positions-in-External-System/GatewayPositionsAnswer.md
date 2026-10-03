[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Controlling Positions in External System](../Controlling-Positions-in-External-System.md) / GatewayPositionsAnswer

[Previous](GatewayPositionArrayCreate.md) | [Next](GatewayPositionsCheck.md)

# IMTGatewayAPI::GatewayPositionsAnswer

The method is used to display positions on the accounts in MetaTrader 5 Administrator, which are used by the gateway in an external trading system. After calling [IMTGatewaySink:HookGatewayPositionsRequest](../../Event-Interface/HookGatewayPositionsRequest.md) hook, a developer can transfer positions state to MetaTrader 5 platform using this method. Transferred positions are displayed in "Positions" tab of MetaTrader 5 Administrator.

More data on using this method can be found in [IMTGatewaySink:HookGatewayPositionsRequest](../../Event-Interface/HookGatewayPositionsRequest.md) hook description.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewayPositionsAnswer(
       const MTAPIRES          result,           // Result
       const INT64*            positions_time,  // Position state fixing time
       const IMTPositionArray* positions        // Positions array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewayPositionsAnswer(
       MTRetCode               result,           // Result
       long                    positions_time,   // Position state fixing time
       CIMTPositionArray       positions         // Positions array
       )

### Parameters

**result**  
[in] MT_RET_OK response code is used if data on positions has been successfully received from an external system. Otherwise, the appropriateerror codeis to be returned.

**positions_time**  
[in] Positions state fixing time, specified in seconds that have elapsed since 01.01.1970. The time is displayed on "Positions" tab of the gateway of the administrator terminal.

**positions**  
[in]An object of the array of positionsreceived from an external system. These positions will be displayed on "Positions" tab of the gateway of the administrator terminal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To pass information about external positions the following field of an [IMTPosition](../../../Database-Interfaces/Trade/Positions/IMTPosition.md) object can be used:

  * [Symbol](../../../Database-Interfaces/Trade/Positions/IMTPosition/Symbol.md)
  * [Action](../../../Database-Interfaces/Trade/Positions/IMTPosition/Action.md)
  * [Digits](../../../Database-Interfaces/Trade/Positions/IMTPosition/Digits.md)
  * [PriceOpen](../../../Database-Interfaces/Trade/Positions/IMTPosition/PriceOpen.md)
  * [Volume](../../../Database-Interfaces/Trade/Positions/IMTPosition/Volume.md)
  * [Comment](../../../Database-Interfaces/Trade/Positions/IMTPosition/Comment.md)


