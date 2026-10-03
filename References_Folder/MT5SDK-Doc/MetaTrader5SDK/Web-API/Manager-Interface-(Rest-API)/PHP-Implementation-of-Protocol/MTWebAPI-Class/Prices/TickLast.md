[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Prices](../Prices.md) / TickLast

[Previous](../Prices.md) | [Next](TickLastGroup.md)

# MTWebAPI::TickLast

Get the current prices of symbols.
    
    
    MTAPIRES  MTWebAPI::TickLast(
       string          $symbol,          // Symbols
       MTTick          $&ticks           // Array of quotes
       )

### Parameters

**$symbol**  
[in] Comma separated symbols, the prices of which should be received. You may use the mask "*" and the negation sign "!" to specify groups of symbols. For example:

**$ &ticks**  
[out] An array of MTick objects that describe ticks. Tick parameters are described in section"Data Structure".

  * EURUSD,USDJPY — get quotes for symbols EURUSD and USDJPY.
  * Forex\Major*, GOLD — get quotes of all symbols from the Major subgroup and quotes of GOLD.
  * Forex\Crosses*,!AUDUSD — get quotes of all symbols of the Crosses subgroup except AUDUSD.
  * Forex\Major\EUR* — get quotes of all symbols with the basic currency EUR from the Major subgroup.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A mask can be used only when specifying the full path to a symbol or group. For example, you can't specify "USD*", the correct variant is "Forex\Major\USD*".
