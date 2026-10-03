[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Trade Activity](../Trade-Activity.md) / Auxiliary Functions

[Previous](Trade-Requests/RequestGetAll.md) | [Next](Auxiliary-Functions/TradeProfit.md)

# Auxiliary Functions

Functions described in this section are auxiliary. They allow calculating profit and margin requirements for positions as well as calculating conversion rates for currencies.

Functions | Purpose  
---|---  
[TradeProfit](Auxiliary-Functions/TradeProfit.md) | Calculates profit for the specified trading conditions.  
[TradeProfitExt](Auxiliary-Functions/TradeProfitExt.md) | Calculates profit for the specified trading conditions using extended volume accuracy.  
[TradeRateBuy](Auxiliary-Functions/TradeRateBuy.md) | Calculates the conversion rate for a Buy trade.  
[TradeRateSell](Auxiliary-Functions/TradeRateSell.md) | Calculates the conversion rate for a Sell trade.  
[TradeMarginCheck](Auxiliary-Functions/TradeMarginCheck.md) | Checks the availability of the margin required for the execution of this order.  
[TradeMarginCheckExt](Auxiliary-Functions/TradeMarginCheckExt.md) | Checks the availability of the margin required for the execution of this order with the indication of increased accuracy volume.  
  
To ensure proper operation of these functions, the Manager API needs to have access to actual quotes of financial instruments used in calculations. To receive quotes of an instrument, add it to the list of selected symbols using the [IMTManagerAPI::SelectedAdd](../Selected-Symbols/SelectedAdd.md) or [IMTManagerAPI::SelectedAddAll](../Selected-Symbols/SelectedAddAll.md) method. Please note that these methods work asynchronously, i.e. they only send a request for a subscription to the symbols. The prices do not become available to the application immediately after the call. To make sure that the application uses actual prices, call auxiliary functions after receiving the [IMTTickSink::OnTick](../../../Database-Interfaces/Price-Data/IMTTickSink/OnTick.md) event for the corresponding symbol. To receive such events, you need to subscribe to them using the [IMTManagerAPI::TickSubscribe](../Tick-Data/TickSubscribe.md) method.
