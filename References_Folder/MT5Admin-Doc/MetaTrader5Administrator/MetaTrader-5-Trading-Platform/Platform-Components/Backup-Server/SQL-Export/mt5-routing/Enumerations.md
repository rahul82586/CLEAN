[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../../Platform-Components.md) / [Backup Server](../../../Backup-Server.md) / [SQL Export](../../SQL-Export.md) / [mt5_routing](../mt5-routing.md) / Enumerations

[Previous](../mt5-routing.md) | [Next](../mt5-routing-dealers.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The following enumerations are used for passing information about trade routing rules:

  * [EnRouteFlags (#enrouteflags)](Enumerations.md#enrouteflags)
  * [EnTypeFlags (#entypeflags)](Enumerations.md#entypeflags)
  * [EnRouteAction (#enrouteaction)](Enumerations.md#enrouteaction)
  * [EnRouteCondition (#enroutecondition)](Enumerations.md#enroutecondition)
  * [EnConditionRule (#enconditionrule)](Enumerations.md#enconditionrule)



<a id="enrouteflags"></a>
## EnRouteFlags (#enrouteflags)

Conditions for applying a rule based on the request type are enumerate in EnRouteFlags.

ID | Value | Description  
REQUEST_NONE | 0x00000000 | Conditions by the request type are not specified.  
REQUEST_PRICE | 0x00000001 | Price request (for request execution).  
REQUEST_REQUEST | 0x00000002 | Confirmation of order execution ar a dealer's type in the request execution mode (with the order confirmation option enabled).  
REQUEST_INSTANT | 0x00000004 | Placing an order in the instant execution mode.  
REQUEST_MARKET | 0x00000008 | Placing an order in the market execution mode.  
REQUEST_EXCHANGE | 0x00000010 | Placing an order in the exchange execution mode.  
REQUEST_PENDING | 0x00000020 | Placing a pending order.  
REQUEST_SLTP | 0x00000040 | Modification of Stop Loss and Take Profit of a position.  
REQUEST_MODIFY | 0x00000080 | Modification of a pending order.  
REQUEST_REMOVE | 0x00000100 | Deleting a pending order.  
REQUEST_ACTIVATE | 0x00000200 | Activation (triggering) of a pending order.  
REQUEST_STOPLIMIT | 0x00000400 | Activation of a Stop Limit order.  
REQUEST_SL | 0x00000800 | Triggering of a Stop Loss order.  
REQUEST_TP | 0x00001000 | Triggering of a Take Profit order.  
REQUEST_STOPOUT_ORDER | 0x00002000 | A request to delete a pending order in case of reaching the stop-out level (if margin requirements are set for pending orders)  
REQUEST_STOPOUT_POSITION | 0x00004000 | A request to close a position when reaching stop-out.  
REQUEST_EXPIRATION | 0x00008000 | Cancellation of an order upon expiration.  
REQUEST_DEALER_POS_EXECUTE | 0x00010000 | Position opening and closing by a dealer.  
REQUEST_DEALER_ORD_PENDING | 0x00020000 | Placing of a pending order by a dealer.  
REQUEST_DEALER_POS_MODIFY | 0x00040000 | Position modification by a dealer.  
REQUEST_DEALER_ORD_MODIFY | 0x00080000 | Order modification by a dealer.  
REQUEST_DEALER_ORD_REMOVE | 0x00100000 | Order deletion by a dealer.  
REQUEST_DEALER_ORD_ACTIVATE | 0x00200000 | Order activation by a dealer.  
REQUEST_DEALER_ORD_SLIMIT | 0x00400000 | Activation of a Stop Limit order by a dealer. After this action is performed, the order turns into a limit order.  
REQUEST_DEALER_CLOSE_BY | 0x00800000 | Close By. An operation of closing two oppositely directed positions at a single symbol performed by a dealer.  
REQUEST_CLOSE_BY | 0x01000000 | Close By. An operation of closing two oppositely directed positions at a single symbol performed by a client.  
  
<a id="entypeflags"></a>
## EnTypeFlags (#entypeflags)

Conditions for applying a rule based on the order type are enumerate in EnTypeFlags.

ID | Value | Description  
TYPE_NONE | 0x0000 | No conditions by the order type.  
TYPE_BUY | 0x0001 | A Buy order.  
TYPE_SELL | 0x0002 | A Sell order.  
TYPE_BUY_LIMIT | 0x0004 | A limit Buy order.  
TYPE_SELL_LIMIT | 0x0008 | A limit Sell order.  
TYPE_BUY_STOP | 0x0010 | A stop Buy order.  
TYPE_SELL_STOP | 0x0020 | A stop Sell order.  
TYPE_BUY_STOP_LIMIT | 0x0040 | A limit Buy Stop order.  
TYPE_SELL_STOP_LIMIT | 0x0080 | A limit Sell Stop order.  
  
<a id="enrouteaction"></a>
## EnRouteAction (#enrouteaction)

Types of actions that are applied to requests are listed in EnRouteAction.

ID | Value | Description  
ACTION_DELAY_TIME | 0 | Delay request execution by the specified number of milliseconds. After applying this action to a request, its execution continues in accordance with the created rules located below in the list. The delay is indicated in a separate parameter.  
ACTION_DELAY_TICK | 1 | Delay request execution by the specified number of ticks. After applying this action to a request, its execution continues in accordance with the created rules located below in the list. The delay is indicated in a separate parameter.  
ACTION_CLEAR_TP | 2 | Clear the Take Profit level set in the order.  
ACTION_CLEAR_SL | 3 | Clear the Stop Loss level set in the order.  
ACTION_CLEAR_SLTP | 4  | Clear the Stop Loss and Take Profit levels set in the order.  
ACTION_DEALER | 1001 | Enqueue the request to be processed by the specified dealer. The flag of action omission in case there are no dealers online, is specified by an additional parameter.  
ACTION_DEALER_ONLINE | 1002 | Pass the request to dealers that are currently online. The flag of action omission in case there are no dealers online, is specified by an additional parameter.  
ACTION_REJECT | 1003 | Reject a request.  
ACTION_REQUOTE | 1004 | Send current market prices in response to the request.  
ACTION_CONFIRM_CLIENT | 1005 | Confirm the execution of an order at a price requested in it.  
ACTION_CONFIRM_MARKET | 1006 | Confirm the execution of an order at the current market price.  
ACTION_CANCEL_ORDER | 1007 | Cancel a pending order during its activation or modification. For example, if a pending order has triggered, but the client has already reached the maximum position volume and a new position cannot be opened, the routing rule will remove this order. Otherwise, the order would have continued to trigger on each new tick. When removing an order by this rule, "deleted [by dealer]" is added to the order comment. An entry about the routing rule that canceled the order is also added to the server journal. The server returns error code MT_RET_REQUEST_REJECT_CANCEL. The action can only be applied during pending order activation or modification (including modification buy a dealer). The rule does not affect other trade requests.  
  
<a id="enroutecondition"></a>
## EnRouteCondition (#enroutecondition)

Additional conditions for activation of a routing rule are listed in IMTConCondition::EnRouteCondition.

ID | Value | Description  
CONDITION_DATETIME | 0 | Using this parameter you can compare date and time of a request with that specified in the "Value" field.  
CONDITION_SYMBOL | 1 | This parameter is used for specifying a symbol or a group of symbols requests for which will be subject to the routing rule.  
CONDITION_VOLUME | 2 | Deal volume requested in an order (in lots). This parameter is used for configuring a rule depending on the request volume, e.g. automatic processing of requests less than 1 lot.  
CONDITION_MARKET_DEVIATION | 3 | This condition is applicable only with the instant execution mode. It takes into account the difference between the price of a client's request and the current market price. For Buy trades the deviation is calculated as ("Current Ask price" - "Client's request price"), for Sell trades it is equal to ("Client's request price" - "Current Bid price"). For example, if a client wants to buy at 1.2000, and the current Ask is 1.2008, then the deviation is equal to 1.2008 - 1.2000 = 8 points.  
CONDITION_TIME | 4  | This parameter can be used for comparing the time or a request arrival (in minutes since 00:00) with the value specified in the "Value" field.  
CONDITION_WEEKDAY | 5 | This parameter allows to route requests depending on a day of the week.  
CONDITION_COMMENT | 6 | This parameter allows to compare a request comment with a specified one. If "=" condition is specified, exact match of a comment is checked. If ">" or ">=" conditions are set, a specified substring is searched in a comment string. If "<" or "<=" conditions are set, comment substring is searched in a specified string.  
CONDITION_EXPERT | 7 | This parameter allows to route requests placed by MQL5 programs.  
CONDITION_SIGNAL | 8 | All operations copied by the client terminal in accordance with the subscription to a [trading signal](https://www.mql5.com/en/signals "Trading Signals") are marked with a special flag. This parameter allows routing trade requests created by trade signals. If this condition is enabled, the rule will trigger for all signal operations.  
CONDITION_DEALER_LOGIN | 9 | This parameter allows applying the routing rules depending on a dealer (or gateway) identifier specified in an order or position. The dealer identifier is specified in an order after it has been confirmed (processed) by the dealer/gateway. Due to it, this rule can be applied only when modifying/deleting an order, and not for newly created orders as they do not have a dealer identifier.. For positions, the dealer identifier is specified according to the dealer identifier of the order, whose execution resulted in the position opening.  
This parameter can be used when processing trade operations for a symbol through several gateways simultaneously. An order or position created through a specific gateway must be further processed through the same gateway.  
CONDITION_SOURCE_LOGIN | 10 | The parameter allows routing requests by a login of a dealer who set a request on a client's behalf.  
CONDITION_MARKET_DEVIATION_SPR | 11 | This condition works when executing orders in the Instant or Market modes, as well as when pending orders and Stop Loss/Take Profit orders are triggered. It takes into account the difference between the price of a client's request and the current market price. During a market execution, when a client does not set a price in the order, the difference between the market price during the request and the current market price is taken into account. The deviation is set in spreads. For floating-spread symbols, the current spread valid during the request check is used. For fixed-spread symbols, a spread value from the symbol settings is used. For Buy trades the deviation is calculated as ("Current Ask price" - "Client's request price"), for Sell trades it is equal to ("Client's request price" - "Current Bid price"). For example, if a client wants to buy at 1.2000, and the current Ask is 1.2008, then the deviation is equal to 1.2008 - 1.2000 = 8 points. The current spread is divided by this value and the result is compared with the value in the rule. When setting the condition, keep in mind that if the deviation is positive, opening at the request price is performed in the client's favor, if the deviation is negative, opening is performed against the client. Another example: if we set < -1, the condition corresponds to the buy requests where a request price exceeds the current price by more than 1 spread.  
CONDITION_GAP | 12 | This parameter allows processing trade requests in a special way under the market conditions that differ from normal ones. For example, after a gap, client requests can be rejected or requoted during a certain number of subsequent ticks. The gap mode is defined separately for each symbol according to its settings. The parameter may take two values — true or false (enabled/disabled). If the gap mode is active when checking a request according to the selected symbol routing rule, actions set in this rule are applied to it. The gap mode is checked by an instrument's Bid and Ask prices. If a gap is detected at least on one of the prices, the rule is triggered.  
CONDITION_LOGIN | 1000 | The number of a client's account. This parameter allows creating individual rules for accounts.  
CONDITION_GROUP | 1001 | The group to which the client's account is included. This parameter is used for configuring rules for separate account groups.  
CONDITION_COUNTRY | 1002 | In this parameter a client's country can be specified. The specified rule will be applied to all clients living in this country.  
CONDITION_CITY | 1003 | Use this parameter to apply the rule to all clients living in a specified city.  
CONDITION_COLOR | 1004 | Use this parameter to apply the rule for clients that are marked with the specified color.  
CONDITION_LEVERAGE | 1005 | Use this parameter to apply the rule for clients with the specified leverage.  
CONDITION_COMMENT_CLIENT | 1006 | Use this parameter to apply the rule for clients with the specified comment.  
CONDITION_MARGIN | 2000 | Use this parameter to set up rule application depending on the margin volume that is currently reserved (in the deposit currency).  
CONDITION_MARGIN_LEVEL | 2001 | This parameter allows using rules depending on the current margin level (in percents).  
CONDITION_MARGIN_FREE | 2002 | This parameter allows using rules depending on the current amount of free margin (in the deposit currency).  
CONDITION_EQUITY | 2003 | This parameter allows using rules depending on the current equity on a client's account (in the deposit currency).  
CONDITION_BALANCE | 2004 | This parameter allows using rules depending on the current balance of a client (in the deposit currency).  
CONDITION_PROFIT | 2005 | This parameter allows using rules depending on the current floating profit of a client.  
CONDITION_DAILY_DEALS | 3000 | This parameter allows using rules depending on the number of deals of a client for the current and previous days (including weekends and holidays).  
CONDITION_DAILY_DEALS_PERIOD | 3001 | The frequency of deals for a day. Calculated on the basis of the last 8 deals (the average time between deals).  
CONDITION_DAILY_PROFIT | 3002 | The profit of the client, whose request is being handled, for the current and previous days (including weekends and holidays).  
CONDITION_POSITION_VOLUME | 4000 | The current volume of a position for the symbol, for which a request has arrived.  
CONDITION_POSITION_PROFIT | 4001 | The current profit of a position for the symbol, for which a request has arrived.  
CONDITION_POSITION_AGE | 4002 | Using this parameter you can specify time in seconds elapsed since position opening for the symbol a request for which is currently being handled. This parameter allows to track positions based on the time they have been held.  
CONDITION_POSITION_MODIFY_TIME | 4003 | Using this parameter you can specify time in seconds elapsed since the last modification of a position for the symbol a request for which is currently being handled. Position modification means increase of its volume, partial closure, and modification of Stop Loss and Take Profit levels. This parameter allows to prevent evasion of the previous rule through manipulating one position, increasing or reducing its volume.  
CONDITION_POSITION_AVERAGE_TIME | 4004 | This parameter allows to track positions based on the time the average age of the position for the symbol for which a request is being handled. The average position age is calculated as follows: Current time — ((Open time + Modification time)/2).  
CONDITION_POSITION_TOTAL | 4005 | This parameter allows tracking the total number of a client's open positions on all symbols. For example, you can set the platform to reject trade requests to open new positions, if the client has reached the specified limit.  
CONDITION_POSITION_TOTAL_SYMBOL | 4006 | The parameter allows tracking the number of positions on the symbol that is specified in the current trade request. For example, if a client has placed an order on EURUSD, this condition will check the current number of the client's open positions on EURUSD.  
CONDITION_ORDER_TOTAL | 4007 | This parameter allows tracking the total number of a client's orders on all symbols. All orders are taken into account, including pending and history orders. Each opening and closing of a position (including partial closure), as well as placing of a pending order increases this counter.  
CONDITION_ORDER_TOTAL_SYMBOL | 4008 | The parameter allows tracking the number of orders on the symbol that is specified in the current trade request. For example, if a client has placed an order on EURUSD, this condition will check the current number of the client's orders (both active and history) on EURUSD.  
CONDITION_POSITION_SL_TOUCHED | 4009 | The condition is triggered when the market price touches the stop loss of a position (while the stop loss may not be activated yet). Possible values — true or false.  
CONDITION_POSITION_TP_TOUCHED | 4010 | The condition is triggered when the market price touches the take profit of a position (while the take profit may not be activated yet). Possible values — true or false.  
CONDITION_ORDER_SL_TOUCHED | 4011 | The condition is triggered when the market price touches the stop loss of a pending order. Possible values — true or false. In combination with the REQUEST_ACTIVATE condition, it allows you to track the simultaneous breakthrough of a pending order (trigger) and its stop loss level. This may occur during a release of important news or after a weekend when a large price gap is formed.  
CONDITION_ORDER_TP_TOUCHED | 4012 | The condition is triggered when the market price touches the stop loss of a pending order. Possible values — true or false. In combination with the REQUEST_ACTIVATE condition, it allows you to track the simultaneous breakthrough of a pending order (trigger) and its take profit level. This may occur during a release of important news or after a weekend when a large price gap is formed.  
  
<a id="enconditionrule"></a>
## EnConditionRule (#enconditionrule)

Types of parameter and value comparison are enumerated in IMTConCondition::EnConditionRule.

ID | Value | Description  
RULE_EQ | 0 | Condition of equality.  
RULE_NOT_EQ | 1 | Condition of inequality.  
RULE_GREATER | 2 | Condition of "greater than".  
RULE_NOT_LESS | 3 | Condition of "not less than".  
RULE_LESS | 4  | Condition of "less than".  
RULE_NOT_GREATER | 5 | Condition of "not greater than".
