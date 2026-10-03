[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [General Principles](../General-Principles.md) / Types of Orders

[Previous](../General-Principles.md) | [Next](Types-of-Execution.md)

<a id="types-of-orders"></a>
# Types of Orders (#types-of-orders)

Several types of trade orders are used for sending trade requests. An order is a trader's instruction to brokerage company to perform a trade operation. Orders are divided into two main types: market and pending. In addition, there are special [Stop Loss (#stop-loss)](Types-of-Orders.md#stop-loss) and [Take Profit (#take-profit)](Types-of-Orders.md#take-profit) orders.

> All types of orders are listed in [IMTOrder::EnOrderType (#enordertype)](../Orders/IMTOrder/Enumerations.md#enordertype).

<a id="market-order"></a>
## Market Order (#market-order)

A market order is an instruction to buy or sell a financial instrument. Execution of such an order will result in a deal. The price at which the deal is executed is determined by the [type of execution](Types-of-Execution.md) that depends on the symbol type. Generally, a security is bought at the Ask price and sold at the Bid price.

<a id="pending-order"></a>
## Pending order (#pending-order)

A pending order is an order to buy or sell a financial instrument in future, with the specified terms. The following types of pending orders are available:

  * Buy Limit — a trade request to buy at the Ask price that is equal to or less than that specified in the order. The current price level is higher than the value specified in the order. Usually this order is placed in anticipation of that the security price, having fallen to a certain level, will increase;


  * Buy Stop — a trade order to buy at the "Ask" price equal to or greater than the one specified in the order. The current price level is lower than the value specified in the order. Usually this order is placed in anticipation of that the security price, having reached a certain level, will keep on increasing.
  * Sell Limit — a trade order to sell at the "Bid" price equal to or greater than the one specified in the order. The current price level is lower than the value specified in the order. Usually this order is placed in anticipation of that the security price will increase to a certain level and will fall then;
  * Sell Stop — a trade order to sell at the "Bid" price equal to or less than the one specified in the order. The current price level is higher than the value in the order. Usually this order is placed in anticipation of that the security price will reached a certain level and will keep on falling.
  * Buy Stop Limit — this type is the combination of the first two types, being a stop order to place a Buy Limit order. As soon as the future Ask price reaches the stop level specified in the order (Price field), a Buy Limit order will be placed at the level specified in Stop Limit Price field. A stop level is set above the current Ask price, while Stop Limit price is set below the stop level.
  * Sell Stop Limit — this order is a stop order to place a Sell Limit order. As soon as the future Bid price reaches the stop level specified in the order (Price field), a Sell Limit order will be placed at the level specified in Stop Limit Price field. A stop level is set below the current Bid price, while Stop Limit price is set above the stop level.



  * For symbols with Exchange Stocks, Exchange Futures and Futures Forts [calculation modes (#encalcmode)](../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#encalcmode), all the types of pending orders trigger according to the Last price (price of a last executed deal). In other words, an order triggers when the Last price touches the price specified in the order. But note that buying or selling as a result of triggering of an order is always performed by the Bid and Ask prices.
  * In the "Exchange execution" mode, the price specified when placing limit orders is not verified. It can be specified above the current Ask price (for the Buy Limit orders) and below the current Bid price (for the Sell Limit orders). When placing an order with such a price, it triggers almost immediately and turns into a market one. However, unlike market orders where a trader agrees to perform a deal by a non-specified current market price, a pending order will be executed at a price no worse than the one specified.
  * If during pending order activation the corresponding market operation cannot be executed (for example, the free margin on the account is not enough), the pending order will be canceled and moved to history with the "Rejected" status.

  
---  
  
![Pending Order Types](images/order_types.png)

![Current market state](images/order_type_red_bar.png) | — current market state | ![Forecast](images/order_type_gray_bar.png) | — forecast  
---|---|---|---  
![Current price](images/order_type_current.png) | — current price | ![Order price](images/order_type_order.png) | — order price  
![Price, reaching which a pending order will be placed](images/order_type_trigger.png) | — price, reaching which a pending order will be placed  
![Expected growth](images/order_type_arrow_up.png) | — expected growth | ![Expected fall](images/order_type_arrow_down.png) | — Expected fall  
  
<a id="take-profit"></a>
## Take Profit (#take-profit)

The Take Profit order is intended for gaining the profit when the security price has reached a certain level. Execution of this order results in complete closing of the whole position. It is always associated with an open [position](../Positions.md) or a pending order. The order can be requested only together with a market or a pending order. Terminal checks long positions with Bid price for meeting of this order provisions (the order is always set above the current Bid price), and it does with Ask price for short positions (the order is always set below the current Ask price).

<a id="stop-loss"></a>
## Stop Loss (#stop-loss)

This order is used for minimizing of losses if the security price has started to move in an unprofitable direction. If the security price reaches this level, the entire position is closed automatically. It is always associated with an open [position](../Positions.md) or a pending order. The order can be placed only together with a market or a pending order. Terminal checks long positions with Bid price for meeting of this order provisions (the order is always set below the current Bid price), and it does with Ask price for short positions (the order is always set above the current Ask price).

  * Levels of Take Profit and Stop Loss are set for the position by the last order (market or triggered pending order). In other words, stop levels in each subsequent order of the same position replace previous ones.
  * Activation of Take Profit and Stop Loss leads to complete closing of the position.


  * For symbols with Exchange Stocks, Exchange Futures and Futures Forts [calculation modes (#encalcmode)](../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#encalcmode), Stop Loss and Take Profit orders trigger according to the Last price (price of a last executed deal). In other words, a stop-order triggers when the Last price touches the specified price. However note that buying or selling as a result of activation of a stop-order is always performed by the Bid and Ask prices.
  * If during Take Profit or Stop Loss activation the corresponding market operation cannot be executed (for example, it is rejected by the exchange), the order will not be deleted. It will trigger again at the next tick corresponding to the order activation conditions.

  
---
