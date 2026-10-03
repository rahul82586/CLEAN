[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Routing](../Routing.md) / Actions and Conditions

[Previous](../Routing.md) | [Next](Example-of-Rules.md)

<a id="actions-and-conditions"></a>
# Actions and Conditions (#actions-and-conditions)

In the routing rules you set actions that are taken in accordance with trade requests, as well as conditions of selecting requests, meeting which these actions are taken.

<a id="action"></a>
## Actions (#action)

An action performed to a trade request, is selected in the ["Perform action" (#action)](../Routing.md#action) field of the "Common" tab:

  * Delay in milliseconds — delay request execution by the specified number of milliseconds. When selecting this action, an additional field for specifying the number of milliseconds will appear to the right of it. After this action is performed, the request execution continues in accordance with the created rules located below.
  * Delay in ticks — delay request execution by the specified number of ticks. When selecting this action, an additional field for specifying the number of ticks will appear to the right of it. After this action is performed, the request execution continues in accordance with the created rules located below. Maximum allowed delay is 60 ticks.
  * Clear TP — clear the Take Profit level set in the order.
  * Clear SL — clear the Stop Loss level set in the order.
  * Clear SLTP — clear the Stop Loss and Take Profit levels set in the order.
  * Process to dealers — enqueue the request to be processed by a dealer specified in the ["Dealers" (#dealers)](../Routing.md#dealers) tab.
  * Process to online dealers — enqueue the request to be processed by dealers who are currently online. At that, the list of dealers from the ["Dealers" (#dealers)](../Routing.md#dealers) is ignored. The request is passed to any online dealer that has a right to process it.
  * Reject — reject the request. An additional field is available for this action, allowing you to specify the reason for rejecting a request. This reason will be displayed in the trading dialog in client terminals when an operation is rejected in accordance with this rule. Providing a detailed description will help eliminate unnecessary questions from clients. The maximum message length is 31 characters.  
  
![Description of the reason for the rejection](images/routing_reject_reason.png)
  * Requote — send the current market price responding to the request.
  * Confirm by request price — confirm the order execution at the requested price.
  * Confirm by market price — confirm the order execution at the current market price. The action is applied to both client orders and orders placed by dealers.
  * Cancel order — cancel a pending order during its activation or modification. For example, if a pending order has triggered, but the client has already reached the maximum position volume and a new position cannot be opened, the routing rule will remove this order. Otherwise, the order would have continued to trigger on each new tick. When removing an order by this rule, "deleted [by dealer]" is added to the order comment. An entry about the routing rule that canceled the order is also added to the server journal:



'1813415': modify order #100103968 buy limit 1.00 EURUSD at 1.06927 sl: 0.00000 tp: 0.00000 -> 1.06552, sl: 0.00000 tp: 0.00000 (1.06996 / 1.07005 / 1.06996)   
'1813415': request rejected, order #100103968 will be canceled, rule 'Cancel on modification' (modify #100103968 buy limit 1.00 EURUSD -> price: 1.06552, sl: 0.00000, tp: 0.00000))   
'1813415': order canceled - by routing rule [#100103968 buy limit 1.00 EURUSD at 1.06927]  
---  
  
  * An additional option of "skip this rules if no dealers online" is available for actions that pass requests to dealers. If this option is enabled, the rule will be ignored, if none of dealers is online.
  * The "Cancel order" action can only be applied during pending order activation or modification (including modification buy a dealer). The rule does not affect other trade requests.

  
---  
  
<a id="request"></a>
## Conditions by the Request Type (#request)

This type of conditions is specified in the ["Where request is" (#request)](../Routing.md#request) field. Here you can specify the types of client requests, which will be proceeded due to the given rule. Any number of elements can be selected in this field.

  * Price — request price (for request execution).
  * Request execution — confirmation of order execution at the dealer's price in the request execution mode (if the option of [order confirmation (#confirm-orders)](../Symbols/Symbol-Settings/Execution.md#confirm-orders) is enabled).
  * Instant execution — placing of an order in the instant execution mode.
  * Market execution — placing of an order in the market execution mode.
  * Exchange execution — placing of an order in the exchange execution mode.
  * Pending order — placing of a pending order.
  * SL & TP modification — modification of Stop Loss and Take Profit of a position.
  * Order modification — modification of a pending order.
  * Order removal — removal of a pending order.
  * Close By — an operation of closing two oppositely directed positions at a single symbol.
  * Order activation — activation of a pending order.
  * Stop Limit activation — activation of Stop Limit.
  * SL activation — activation of a Stop Loss order.
  * TP activation — activation of a Take Profit order.
  * Stop-Out order — request to delete a pending order as a stop-out level is reached (is used, if margin requirements are set for pending orders).
  * Stop-Out position — request to forced closing of a position as the stop-out level is reached.
  * Order expiration — removing an order due to its expiration.
  * Execution by dealer — execution of a trade operation by a [dealer](../Managers.md).
  * Pending order by dealer — placing of a pending [order](../Orders.md) by a dealer.
  * Position modification by dealer — modification of a [position](../Positions.md) by a dealer.
  * Order modification by dealer — modification of an order by a dealer.
  * Order removing by dealer — deletion of an order by a dealer.
  * Pending order activation by dealer — forced activation of a pending order by a dealer.
  * Stop-Limit activation by dealer — forced activation of a Stop-Limit order by a dealer. As a result of this, the order becomes a Limit order.
  * Close By by dealer — an operation of closing two oppositely directed positions at a single symbol performed by a dealer.



<a id="order"></a>
## Conditions by the Order Type (#order)

This type of conditions is specified in the ["Where order is" (#order)](../Routing.md#order) field. Here you can specify the types of orders which will be proceeded due to the given rule. Unlimited number of elements can also be selected in this field.

  * Buy — a buy order;
  * Sell — a sell order;
  * Buy Limit — a limit order to buy;
  * Sell Limit — a limit order to sell;
  * Buy Stop — a stop order to buy;
  * Sell Stop — a stop order to sell;
  * Buy Stop Limit — Buy Stop Limit order;
  * Sell Stop Limit — Sell Stop Limit order.



> For "SL and TP modification", "SL activation", "TP activation", "Stop-Out Position" and "Position modification by dealer" operations, the condition by order type sets the direction of positions associated with these operations. For example, to route an operation closing a Buy position by Take Profit, the rule should be specified as "For orders: Buy", despite the fact that a Sell operation is actually performed to close the position.

<a id="condition"></a>
## Additional Conditions (#condition)

You can set additional conditions for a rule in the ["Where conditions are" (#condition)](../Routing.md#condition) field. In additional conditions you can set a parameter to compare, the condition (equal, not equal, etc.) and the value to which the parameter is compared. The following parameters can be set:

<a id="request"></a>
### Request (#request)

  * Date and time — using this parameter you can compare the date and time when a request was received with a date and time specified in the "Value" field;
  * Symbols — using this parameter you can specify a symbol or a group of symbols, requests by which will be processed according to the rule. Symbols can be specified using masks containing "*" and "!";
  * Request volume — deal volume requested in the order (in lots). This parameter allows setting up a rule depending on the request volume. For example, it can be the automatic processing of requests with volume less than 1 lot;
  * Deviation from market, points — this condition works for the instant and market [execution](../Symbols/Symbol-Settings/Execution.md) of orders, and for triggering of pending orders and SL/TP orders. It considers the difference between the price of a client's request and the current market price. In the market execution mode, when a client doesn't specify a price in the order, the condition considers the difference between the market price at the time of placing the order and the current market price.  
For buy trades, the deviation is calculated as ("Current Ask Price" - "Price of Client's Request"), and for sell trades it is ("Price of Client's Request" - "Current Bid Price"). For example, if a client wants to make a buy deal at 1.2000, and the current Ask price is 1.2008, then the deviation is 1.2008 - 1.2000 = 8 points.  
Thus, when setting up this condition, note the following — if deviation is positive, then opening by the request price is for benefit of the client, if deviation is negative then for benefit of the broker. Another example: if the deviation is set to < -8, then buy requests, in which the requested price is greater than the current price by more than 8 points, will fall under this condition;
  * Time — using this parameter you can compare the time when a request was received with a time specified in the "Value" field;
  * Day of week — this parameter allows to route requests depending on a day of the week;
  * Request comment — this parameter allows to compare a request comment with a specified one. If "=" condition is specified, exact match of a comment is checked. If ">" or ">=" conditions are set, a specified substring is searched in a comment string. If "<" or "<=" conditions are set, comment substring is searched in a specified string;
  * Placed by expert — this parameter allows to route requests placed by MQL5 programs.
  * Placed by signal — all trade operations copied by a client terminal according to a subscription to a [trade signal](https://www.mql5.com/en/signals "Trading Signals") are marked in a special way. This parameter allows routing trade requests created by trade signals. If it is equal to "true", the rule will trigger for all signal operations. If it is equal to false, it will trigger for all operations except for signal ones.
  * Dealer processed request — this parameter allows applying the routing rules depending on a dealer (or gateway) identifier specified in an order or position. The dealer identifier is specified in an order after it has been confirmed (processed) by the dealer/gateway. Due to it, this rule can be applied only when modifying/deleting an order, and not for newly created orders as they do not have a dealer identifier. For positions, the dealer identifier is specified according to the dealer identifier of the order, whose execution resulted in the position opening.  
This parameter can be used when processing trade operations for a symbol through several gateways simultaneously. An order or position created through a specific gateway must be further processed through the same gateway.
  * Dealer placed request — the parameter allows routing requests by a login of a dealer who set a request on a client's behalf.
  * Deviation from market, spreads — this condition works when [executing](../Symbols/Symbol-Settings/Execution.md) orders in the Instant or Market modes, as well as when pending orders and Stop Loss/Take Profit orders are triggered. It takes into account the difference between the price of a client's request and the current market price. During a market execution, when a client does not set a price in the order, the difference between the market price during the request and the current market price is taken into account.  
The deviation is set in spreads. For floating-spread symbols, the current spread valid during the request check is used. For fixed-spread symbols, a spread value from the [symbol settings (#spread)](../Symbols/Symbol-Settings/Common.md#spread) is used.  
For Buy trades the deviation is calculated as ("Current Ask price" - "Client's request price"), for Sell trades it is equal to ("Client's request price" - "Current Bid price"). For example, if a client wants to buy at 1.2000, and the current Ask is 1.2008, then the deviation is equal to 1.2008 - 1.2000 = 8 points. The deviation value is divided by the current spread value and the result is compared with the value in the rule.  
When setting the condition, keep in mind that if the deviation is positive, opening at the request price is performed in the client's favor, if the deviation is negative, opening is performed against the client. Another example: if we set < -1, the condition corresponds to the buy requests where a request price exceeds the current price by more than 1 spread.
  * Request price — order price. In the Instant and Request [execution modes](../Symbols/Symbol-Settings/Execution.md), the price which the trader has specified in the order is checked; in the Market or Exchange execution modes, the current symbol price is checked. Since prices of different symbols differ considerably, this condition should be used together with the "Symbol" condition. It can also be used to set the general price threshold. For example, you can decline all requests with a cost of less than one dollar.
  * Value — the value of the requested operation in the symbol's base currency. The value calculation depends on the symbol's [margin/profit calculation mode (#calculation)](../Symbols/Symbol-Settings/Trade.md#calculation).  
  
For symbols with the Forex calculation mode, the value is equal to the product of the contract size and the volume. For example, for EURUSD with the contract size of 100,000, the value of 1 lot is equal to EUR 100,000.  
  
For symbols with the CFD, CFD Leverage, CFD Index and Futures calculation modes, the contract size is not expressed in money, but, for example, in the number of shares. Therefore, the contract size is additionally multiplied by the symbol value to obtain the value in monetary terms. For Futures symbols, the final value is additionally multiplied by the ratio of the tick value to the tick size. For example, if a Futures symbol has USD as the base currency, the contract size is equal to 100, the cost is 33, and the tick value to tick size ratio is 1/0.1, then the value of one lot of the position will be equal to 100*33*10 = USD 33,000. For a CFD symbol with the same parameters, one lot size will be 100*33 = USD 3,300. 



<a id="account"></a>
### Account (#account)

  * Login — client's account number. Using this parameter, you can create individual rules for specific accounts;
  * Group — group to which the client is included. This parameter allows setting up rules for specific groups of accounts. For specifying groups, the mask "*" can be used. For example, if you specify "demo*" it will indicate all groups, whose name (including path) starts with "demo" (for example, demo\forex, demoforex, demoforex\usd). If you specify "*forex", it will indicate all groups, whose name ends with "forex" (for example, demo\forex, real\forex). You can also specify several groups or group masks separate by comma.
  * Country — in this parameter you can specify a country of a client. All the clients who live in it will be processed according to the given rule.
  * City — use this parameter to apply the rules to the clients who live in the specified city;
  * ZIP code — use this parameter to apply the rule for clients with the specified [zip code (#personal)](../Accounts/Editing-Account.md#personal).
  * Color — use this parameter to apply the rules to the clients marked by the specified color;
  * Leverage — use this parameter to apply the rules to the clients with the specified leverage;
  * Comment — use this parameter to apply the rules to the clients with the specified (the ["Comment" (#personal)](../Accounts/Editing-Account.md#personal) field in the client record);
  * Status — this parameter allows request routing based on the client [status (#personal)](../Accounts/Editing-Account.md#personal). For example, by combining it with the Country and Symbol parameters, you can prevent non-US clients from trading US stocks.
  * Margin — using this parameter you can set up the rule to be applied depending on the size of margin reserved at the moment (in deposit currency);
  * Margin level — this parameter allows applying the rule depending on the current margin level (in percents);
  * Free margin — this parameter allows applying the rule depending on the current size of free margin (in deposit currency);
  * Equity — use this parameter to apply the rules depending on the current size of client's equity (in deposit currency);
  * Balance — use this parameter to apply the rules depending on the current balance of the client (in deposit currency);
  * Client ID — the [unique identifier](../Clients.md) of the client with whom the trading account is associated. A client can have several trading accounts. With this condition, you can work directly with the client rather than separate accounts.



<a id="position"></a>
### Position (#position)

  * Position volume — current position volume for the symbol of the request;
  * Position profit — current profit on the position of the symbol of the request.
  * Position value — position value on the symbol's base currency. The value calculation depends on the symbol's [margin/profit calculation mode (#calculation)](../Symbols/Symbol-Settings/Trade.md#calculation).  
  
For symbols with the Forex calculation mode, the value is equal to the product of the contract size and the volume. For example, for EURUSD with the contract size of 100,000, the value of 1 lot is equal to EUR 100,000.  
  
For symbols with the CFD, CFD Leverage, CFD Index and Futures calculation modes, the contract size is not expressed in money, but, for example, in the number of shares. Therefore, the contract size is additionally multiplied by the symbol value to obtain the value in monetary terms. For Futures symbols, the final value is additionally multiplied by the ratio of the tick value to the tick size. For example, if a Futures symbol has USD as the base currency, the contract size is equal to 100, the cost is 33, and the tick value to tick size ratio is 1/0.1, then the value of one lot of the position will be equal to 100*33*10 = USD 33,000. For a CFD symbol with the same parameters, one lot size will be 100*33 = USD 3,300. 
  * Age of position — using this parameter, you can specify time in seconds that has passed since the opening of position for the symbol, the request for which is being processed. This parameter allows tracking positions by the time of holding;
  * Last change of position — using this parameter, you can specify time in seconds that has passed since the last change of position for the symbol, request for which is being processed. A change of position includes increasing its volume and partial closing. This parameter allows avoiding evasion of the previous one ("Age of position") through manipulating one position by increasing and decreasing its volume;
  * Avg lifetime of position — this parameter allows tracking the average lifetime of a position for the symbol, the request for is being processed. The Average lifetime is calculated in seconds using the following formula: current time — ((time of opening + time of changing)/2).
  * Position SL touched — condition is triggered when the market price touches the stop loss of a position (while the stop loss may not be activated yet). Possible values — true or false.
  * Position TP touched — condition is triggered when the market price touches the take profit of a position (while the take profit may not be activated yet). Possible values — true or false.
  * Positions total — this parameter allows tracking the total number of a client's open positions on all symbols. For example, you can set the platform to reject trade requests to open new positions, if the client has reached the specified limit.
  * Client positions total by symbol — the parameter allows tracking the number of positions on the symbol that is specified in the current trade request. For example, if a client has placed an order on EURUSD, this condition will check the current number of the client's open positions on EURUSD.



<a id="order"></a>
### Order (#order)

  * Order SL touched — condition is triggered when the market price touches the stop loss of a pending order. Possible values — true or false. In combination with the ["Order activation" (#request)](Actions-and-Conditions.md#request) condition, it allows you to track the simultaneous breakthrough of a pending order (trigger) and its stop loss level. This may occur during a release of important news or after a weekend when a large price gap is formed.
  * Order TP touched — condition is triggered when the market price touches the stop loss of a pending order. Possible values — true or false. In combination with the ["Order activation" (#request)](Actions-and-Conditions.md#request) condition, it allows you to track the simultaneous breakthrough of a pending order (trigger) and its take profit level. This may occur during a release of important news or after a weekend when a large price gap is formed.
  * Orders total — this parameter allows tracking the total number of a client's orders on all symbols. All orders are taken into account, including pending and history orders. Each opening and closing of a position (including partial closure), as well as placing of a pending order increases this counter.
  * Client orders total by symbol — the parameter allows tracking the number of orders on the symbol that is specified in the current trade request. For example, if a client has placed an order on EURUSD, this condition will check the current number of the client's orders (both active and history) on EURUSD.
  * Order In — orders, as a result of which the trader enters the market, increases the current position or reverses it. When a new order is received, the platform calculates the effect of the order execution on the current account state: whether a new position will be opened or existing one will be closed or reversed. The check applies to market orders (the effect of the order execution) and for pending orders (the effect of the order triggering and execution at a price specified therein).


  * On hedging accounts: any pending order is considered an entry order, since its execution can only lead to the opening of a new position.
  * On hedging accounts: triggering of Stop Loss, Take Profit and Stop Out is considered an exit order, since this always leads to closing of existing positions.
  * On netting accounts: order direction is determined relative to the current uncovered volume of the symbol, taking into account the existing open position and all pending orders for that symbol. For example, the account has a Buy 1.00 position, a Buy Limit 2.00 order and a Sell Limit 1.00 order. If both pending orders were triggered, the trader would have the resulting position Buy 2.00. This resulting position is taken into account when checking the "Order In" rule. For example, if the trader places a Buy Limit order with the volume of 1.00, the system considers it an entry order. A Sell Limit 1.00 order would be considered an exit order.
  * On netting accounts: for the rule checks performed for pending orders, a position having a Stop Loss or Take Profit level, is considered to be fully covered, so the calculated final uncovered position volume is considered to be zero. For example, the account has a Buy 1.00 position with a specified Stop Loss, a Buy Limit 2.00 order and a Sell Limit 1.00 order. If both pending orders were triggered, the trader would have the resulting position Buy 1.00. This resulting position is taken into account when checking the "Order In" rule for pending orders.
  * Order Out — orders, as a result of which the trader exits the market, partially closes the current position or reverses it. The rule is similar to the "Order In" condition.



<a id="statistics"></a>
### Statistics (#statistics)

  * Daily deals — this parameter allows applying the rules depending on the number of deals executed for the client during the previous and current day (including holidays and weekend);
  * Daily deal period — frequency of trades during the day. Calculated on the basis of 8 last deals (average time in seconds between deals);
  * Daily profit — profit of the client whose request is being processed for the previous and current day (including holidays and weekend);



<a id="symbol"></a>
### Symbol (#symbol)

  * Gap mode — this parameter allows processing trade requests in a special way under the market conditions that differ from normal ones. For example, after a gap, client requests can be rejected or requoted during a certain number of subsequent ticks. [The gap mode is defined (#gap)](../Symbols/Symbol-Settings/Quotes.md#gap) separately for each symbol according to its settings.  
The parameter may take two values — true or false (enabled/disabled). If the gap mode is active when checking a request according to the selected symbol routing rule, [actions set in this rule (#action)](Actions-and-Conditions.md#action) are applied to it.  
The gap mode is checked by an instrument's Bid and Ask prices. If a gap is detected at least on one of the prices, the rule is triggered.
  * Current spread — the parameter allows applying routing rules depending on the difference between the current Bid and Ask prices (as at the time of check) of the financial symbol from the trade request. For example, you can forward trade requests to a dealer if the spread increases a certain value.



For string type parameters (for example, City, Request comment, etc.), exact values match is checked when "=" condition is specified. If ">" or ">=" conditions are set, a specified substring is searched in the parameter. If "<" or "<=" conditions are set, parameter value substring is searched in a specified string;  
---
