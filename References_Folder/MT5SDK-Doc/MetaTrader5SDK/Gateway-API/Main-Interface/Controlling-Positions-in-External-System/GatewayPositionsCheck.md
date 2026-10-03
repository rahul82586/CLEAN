[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Controlling Positions in External System](../Controlling-Positions-in-External-System.md) / GatewayPositionsCheck

[Previous](GatewayPositionsAnswer.md) | [Next](../Controlling-Orders-in-External-System.md)

# IMTGatewayAPI::GatewayPositionsCheck

This method is intended for verification of positions with an external trading system. This method is reserved for future use.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewayPositionsCheck(
       const MTAPIRES          result,           // Result
       const INT64*            positions_time,  // Position state fixing time
       const IMTPositionArray* positions        // Positions array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewayPositionsCheck(
       MTRetCode               result,           // Result
       long                    positions_time,   // Position state fixing time
       CIMTPositionArray       positions         // Positions array
       )

### Parameters

**result**  
[in] Response code.

**positions_time**  
[in] Positions state fixing time, specified in seconds that have elapsed since 01.01.1970.

**positions**  
[in]An object of the array of positionsreceived from an external system. For a correct operation, the following fields ofIMTPositionobjects inside the array must be filled:

  * Symbol
  * Volume
  * ContractSize
  * Action
  * PriceOpen



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
