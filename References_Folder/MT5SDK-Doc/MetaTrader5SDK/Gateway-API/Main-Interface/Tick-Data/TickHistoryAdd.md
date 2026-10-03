[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Tick Data](../Tick-Data.md) / TickHistoryAdd

[Previous](TickHistoryRequestRaw.md) | [Next](TickHistoryReplace.md)

# IMTGatewayAPI::TickHistoryAdd

Add tick data of a symbol.

C++
    
    
    MTAPIRES  IMTGatewayAPI::TickHistoryAdd(
       LPCWSTR             symbol,         // Symbol
       const MTTickRate*   ticks,          // Ticks to add
       const UINT          ticks_total     // Number of ticks to add
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.TickHistoryAdd(
       string              symbol,         // Symbol
       MTTickRate[]        ticks           // Ticks to add
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update tick data.

**ticks**  
[in] Array ofMTTickRatestructures, which describe the ticks being added.

**ticks_total**  
[in] The number of ticks to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Unlike [IMTGatewayAPI::SendTicks](../Quote-and-News-Feeds/SendTicks.md), this method directly adds quotes to the price history rather than adding them to the price stream.
