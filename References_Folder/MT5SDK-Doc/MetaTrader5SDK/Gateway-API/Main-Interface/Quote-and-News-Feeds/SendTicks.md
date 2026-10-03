[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Quote and News Feeds](../Quote-and-News-Feeds.md) / SendTicks

[Previous](SendTickStats.md) | [Next](SendBookDiffs.md)

# IMTGatewayAPI::SendTicks

Sending current prices.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SendTicks(
       MTTick*     ticks,          // Prices array
       const UINT  ticks_total     // Number of the elements in the array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendTicks(
       MTTick[]    ticks           // Prices array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendTick(
       MTTick      ticks           // A single description of prices
       )

### Parameters

***ticks**  
[in] A pointer to the array of prices described by theMTTickstructure.

**ticks_total**  
[in] Number of the elements in the ticks array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method sends the filled [MTTick](../../../Structures/MTTick.md) structures array to the trading platform.
