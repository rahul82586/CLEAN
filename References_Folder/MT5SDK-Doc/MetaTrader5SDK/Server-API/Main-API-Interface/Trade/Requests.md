[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Trade](../Trade.md) / Requests

[Previous](Positions/PositionSplit.md) | [Next](Trade-Requests/Requests-RequestCreate.md)

# Trade Requests

Trade request functions provide access to conducting trading operations on the server through the plugin. They also allow subscribing to events associated with changes in the queue of requests.

Functions | Purpose  
---|---  
[TradeRequestCreate](Trade-Requests/Requests-RequestCreate.md) | Creates an object of a trade request.  
[TradeRequestCreateArray](Trade-Requests/Requests-RequestCreateArray.md) | Creates an object of the array of trade requests.  
[TradeConfirmCreate](Trade-Requests/Requests-ConfirmCreate.md) | Creates an object of a trade request confirmation.  
[TradeExecutionCreate](Trade-Requests/Requests-ExecutionCreate.md) | Creates an object of a trade request.  
[TradeSubscribe](Trade-Requests/Requests-Subscribe.md) | Subscribes to events and hooks associated with trade requests.  
[TradeUnsubscribe](Trade-Requests/Requests-Unsubscribe.md) | Unsubscribes from events and hooks associated with trade requests.  
[TradeRequest](Trade-Requests/Requests-Request.md) | Adds a trade request to the queue of requests.  
[TradeProfit](Trade-Requests/Requests-Profit.md) | Calculates profit for the specified trading conditions.  
[TradeProfitExt](Trade-Requests/Requests-ProfitExt.md) | Calculates profit for the specified trading conditions using extended volume accuracy.  
[TradeRateBuy](Trade-Requests/Requests-RateBuy.md) | Calculates the conversion rate for a Buy trade.  
[TradeRateSell](Trade-Requests/Requests-RateSell.md) | Calculates the conversion rate for a Sell trade.  
[TradeMarginCheck](Trade-Requests/Requests-MarginCheck.md) | Checks the availability of the margin required for the execution of this order.  
[TradeMarginCheckExt](Trade-Requests/Requests-MarginCheckExt.md) | Checks the availability of the margin required for the execution of this order with the indication of increased accuracy volume.  
[TradeBalanceCheck](Trade-Requests/Requests-BalanceCheck.md) | Check and correction of a client's balance and credit assets.  
[TradeSubscribeEOD](Trade-Requests/Requests-SubscribeEOD.md) | Subscribes to events associated with operations performed at the end of a trading day/month.  
[TradeUnsubscribeEOD](Trade-Requests/Requests-UnsubscribeEOD.md) | Unsubscribes from events associated with operations performed at the end of a trading day/month.  
[TradeAccountSet](Trade-Requests/Requests-AccountSet.md) | Synchronizes an account's trade state with an external system.
