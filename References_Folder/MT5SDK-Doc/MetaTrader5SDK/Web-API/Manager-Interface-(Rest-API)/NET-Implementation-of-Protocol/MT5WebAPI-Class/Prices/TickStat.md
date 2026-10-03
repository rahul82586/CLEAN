[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Prices](../Prices.md) / TickStat

[Previous](TickLastGroup.md) | [Next](../Custom-Commands.md)

# MT5WebAPI.TickStat

Get the current prices of symbols taking into account conversion for the specified group.
    
    
    MTRetCode  MT5WebAPI.TickStat(
       string                symbol,    // Symbols
       out List<MTTickStat>  tickStat  // An array of statistical data
       )

### Parameters

**symbol**  
[in] Comma separated symbols, for which you need to receive statistical data. You may use the mask "*" and the negation sign "!" to specify groups of symbols. For example:

**tickStat**  
[out] An array of MTickStat objects that describe the statistical data of symbol prices. Description of statistical data is available in the"Data Structure"section.

  * SYMBOL=EURUSD,USDJPY — get quotes for symbols EURUSD and USDJPY.
  * SYMBOL=Forex\Major*, GOLD — get quotes of all symbols from the Major subgroup and quotes of GOLD.
  * SYMBOL=Forex\Crosses*,!AUDUSD — get quotes of all symbols of the Crosses subgroup except AUDUSD.
  * SYMBOL=Forex\Major\EUR* — get quotes of all symbols with the basic currency EUR from the Major subgroup.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A mask can be used only when specifying the full path to a symbol or group. For example, you can't specify "USD*", the correct variant is "Forex\Major\USD*".
