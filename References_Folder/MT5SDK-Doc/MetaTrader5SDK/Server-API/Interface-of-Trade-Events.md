[🏠 Document Start](../README.md) / [Server API](README.md) / Interface of Trade Events

[Previous](Interface-of-Custom-Events/HookPluginCommand.md) | [Next](Interface-of-Trade-Events/OnTradeRequestAdd.md)

# Interface of Trade Events IMTTradeSink

The IMTTradeSink class contains the following methods:

Method | Description  
---|---  
[OnTradeRequestAdd](Interface-of-Trade-Events/OnTradeRequestAdd.md) | A handler of the event of adding a checked trade request in the requests queue.  
[OnTradeRequestUpdate](Interface-of-Trade-Events/OnTradeRequestUpdate.md) | A handler of the event of a changed state of a trade request.  
[OnTradeRequestDelete](Interface-of-Trade-Events/OnTradeRequestDelete.md) | A handler of the event of a trade request deletion.  
[OnTradeRequestProcess](Interface-of-Trade-Events/OnTradeRequestProcess.md) | A handler of the event of a successful execution of a trade request.  
[OnTradeRequestProcessCloseBy](Interface-of-Trade-Events/OnTradeRequestProcessCloseBy.md) | A handler of the event of a successful execution of a Close By trade request.  
[OnTradeRequestRefuse](Interface-of-Trade-Events/OnTradeRequestRefuse.md) | A handler of the event of refusal to execute a trade request before it is added to the queue.  
[OnTradeExecution](Interface-of-Trade-Events/OnTradeExecution.md) | A handler of the event of receiving a trade execution from a gateway.  
[OnTradeSplit](Interface-of-Trade-Events/OnTradeSplit.md) | A handler of the [trading position split](Main-API-Interface/Trade/Positions/PositionSplit.md) event.  
[HookTradeRequestAdd](Interface-of-Trade-Events/HookTradeRequestAdd.md) | A hook for adding a checked trade request in the requests queue.  
[HookTradeRequestRoute](Interface-of-Trade-Events/HookTradeRequestRoute.md) | A hook of trade request routing in a requests queue.  
[HookTradeRequestProcess](Interface-of-Trade-Events/HookTradeRequestProcess.md) | A hook of trade request execution.  
[HookTradeRequestProcessCloseBy](Interface-of-Trade-Events/HookTradeRequestProcessCloseBy.md) | A hook of a Close By trade request execution.  
[HookTradeRequestRuleFilter](Interface-of-Trade-Events/HookTradeRequestRuleFilter.md) | A hooks of checking of whether a trade request meets a routing rule.  
[HookTradeRequestRuleApply](Interface-of-Trade-Events/HookTradeRequestRuleApply.md) | A hook of the application of a routing rule to a trade request.  
[HookTradeRollover](Interface-of-Trade-Events/HookTradeRollover.md) | A hook of rollover charging.  
[HookTradeInterest](Interface-of-Trade-Events/HookTradeInterest.md) | A hook of calculation of annual interest.  
[HookTradeInterestCharge](Interface-of-Trade-Events/HookTradeInterestCharge.md) | A hook of adding the calculated amount of the annual interest to a client's account.  
[HookTradeInterestChargeDeal](Interface-of-Trade-Events/HookTradeInterestChargeDeal.md) | A hook of a balance deal for charging annual interest.  
[HookTradeCommissionOrder](Interface-of-Trade-Events/HookTradeCommissionOrder.md) | A hook of the calculation of commission, which is blocked on an account during the placing of an order.  
[HookTradeCommissionDeal](Interface-of-Trade-Events/HookTradeCommissionDeal.md) | A hook of the calculation of commission, which is charged during the execution of a deal. It is called before the calculation and charging/blocking commission on the account, allowing to use an individual commission calculation algorithm.  
[HookTradeCommissionCharge](Interface-of-Trade-Events/HookTradeCommissionCharge.md) | A hook for the final adding/withdrawal of commissions from an account at the end of a day/month.  
[HookTradeExecution](Interface-of-Trade-Events/HookTradeExecution.md) | A hook of applying a trade execution.  
[HookTradeSplit](Interface-of-Trade-Events/HookTradeSplit.md) | A hook for the [trading position split](Main-API-Interface/Trade/Positions/PositionSplit.md).  
  
> To be able to receive trade events, the plugin must be subscribed to these events using the [IMTServerAPI::TradeSubscribe](Main-API-Interface/Trade/Trade-Requests/Requests-Subscribe.md) method.
