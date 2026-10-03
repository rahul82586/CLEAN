[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / Enumerations

[Previous](../IMTConCondition.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConCondition](../IMTConCondition.md) class contains the following enumerations:

  * [IMTConCondition::EnRouteCondition (#enroutecondition)](Enumerations.md#enroutecondition)
  * [IMTConCondition::EnConditionRule (#enconditionrule)](Enumerations.md#enconditionrule)
  * [IMTConCondition::EnConditionType (#enconditiontype)](Enumerations.md#enconditiontype)



<a id="enroutecondition"></a>
## IMTConCondition::EnRouteCondition (#enroutecondition)

Additional conditions for activation of a routing rule are listed in IMTConCondition::EnRouteCondition.

ID | Value | Description  
CONDITION_DATETIME | 0 | Using this parameter you can compare date and time of a request with that specified in the "Value" field.  
CONDITION_SYMBOL | 1 | This parameter is used for specifying a symbol or a group of symbols requests for which will be subject to the routing rule.  
CONDITION_VOLUME | 2 | Deal volume requested in an order (in lots). This parameter is used for configuring a rule depending on the request volume, e.g. automatic processing of requests less than 1 lot.  
CONDITION_MARKET_DEVIATION | 3 | This condition is applicable only with the instant execution mode. It takes into account the difference between the price of a client's request and the current market price. For Buy trades the deviation is calculated as ("Current Ask price" - "Client's request price"), for Sell trades it is equal to ("Client's request price" - "Current Bid price"). For example, if a client wants to buy at 1.2000, and the current Ask is 1.2008, then the deviation is equal to 1.2008 - 1.2000 = 8 points.  
CONDITION_TIME | 4  | This parameter can be used for comparing the time or a request arrival (in minutes since 00:00) with the value specified in the "Value" field.  
CONDITION_WEEKDAY | 5 | This parameter allows to route requests depending on a day of the week.  
CONDITION_COMMENT | 6 | This parameter allows to compare a request comment with a specified one. If "=" condition is specified, exact match of a comment is checked. If ">" or ">=" conditions are set, a specified substring is searched in a comment string. If "<" or "<=" conditions are set, comment substring is searched in a specified string.  
CONDITION_EXPERT | 7 | This parameter allows to route requests placed by MQL5 programs. Requests placed by MQL5 programs have the flag [IMTRequest::TA_FLAG_EXPERT (#entradeactionflags)](../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Enumerations.md#entradeactionflags).  
CONDITION_SIGNAL | 8 | All operations copied by the client terminal in accordance with the subscription to a [trading signal](https://www.mql5.com/ru/signals "Trading Signals") are marked with a special flag. This parameter allows routing trade requests created by trade signals. If this condition is enabled, the rule will trigger for all signal operations.  
CONDITION_DEALER_LOGIN | 9 | This parameter allows applying the routing rules depending on a dealer (or gateway) identifier specified in an order or position. The dealer identifier is specified in an order after it has been confirmed (processed) by the dealer/gateway. Due to it, this rule can be applied only when modifying/deleting an order, and not for newly created orders as they do not have a dealer identifier.. For positions, the dealer identifier is specified according to the dealer identifier of the order, whose execution resulted in the position opening.  
This parameter can be used when processing trade operations for a symbol through several gateways simultaneously. An order or position created through a specific gateway must be further processed through the same gateway.  
CONDITION_SOURCE_LOGIN | 10 | The parameter allows routing requests by a login of a dealer who set a request on a client's behalf.  
CONDITION_MARKET_DEVIATION_SPR | 11 | This condition works when executing orders in the Instant or Market modes, as well as when pending orders and Stop Loss/Take Profit orders are triggered. It takes into account the difference between the price of a client's request and the current market price. During a market execution, when a client does not set a price in the order, the difference between the market price during the request and the current market price is taken into account. The deviation is set in spreads. For floating-spread symbols, the current spread valid during the request check is used. For fixed-spread symbols, a spread value from the symbol settings is used. For Buy trades the deviation is calculated as ("Current Ask price" - "Client's request price"), for Sell trades it is equal to ("Client's request price" - "Current Bid price"). For example, if a client wants to buy at 1.2000, and the current Ask is 1.2008, then the deviation is equal to 1.2008 - 1.2000 = 8 points. The current spread is divided by this value and the result is compared with the value in the rule. When setting the condition, keep in mind that if the deviation is positive, opening at the request price is performed in the client's favor, if the deviation is negative, opening is performed against the client. Another example: if we set < -1, the condition corresponds to the buy requests where a request price exceeds the current price by more than 1 spread.  
CONDITION_GAP | 12 | This parameter allows processing trade requests in a special way under the market conditions that differ from normal ones. For example, after a gap, client requests can be rejected or requoted during a certain number of subsequent ticks. The [gap mode is defined](../../Symbols/IMTConSymbol/FilterGap.md) separately for each symbol according to its settings. The parameter may take two values — true or false (enabled/disabled). If the gap mode is active when checking a request according to the selected symbol routing rule, actions set in this rule are applied to it. The gap mode is checked by an instrument's Bid and Ask prices. If a gap is detected at least on one of the prices, the rule is triggered.  
CONDITION_PRICE | 13 | Order price. In the Instant and Request execution modes, the price which the trader has specified in the order is checked; in the Market or Exchange execution modes, the current symbol price is checked ([IMTConSymbol::EnExecutionMode (#enexecutionmode)](../../Symbols/IMTConSymbol/Enumerations.md#enexecutionmode)). Since prices of different symbols differ considerably, this condition should be used together with the CONDITION_SYMBOL condition. It can also be used to set the general price threshold. For example, you can decline all requests with a cost of less than one dollar.  
CONDITION_VALUE | 14 | The value of the requested operation in the symbol base currency. The value calculation depends on the symbol's margin/profit calculation mode ([IMTConSymbol::CalcMode](../../Symbols/IMTConSymbol/CalcMode.md)). For symbols with the Forex calculation mode, the value is equal to the product of the contract size and the volume. For example, for EURUSD with the contract size of 100,000, the value of 1 lot is equal to EUR 100,000. For symbols with the CFD, CFD Leverage, CFD Index and Futures calculation modes, the contract size is not expressed in money, but, for example, in the number of shares. Therefore, the contract size is additionally multiplied by the symbol value to obtain the value in monetary terms. For Futures symbols, the final value is additionally multiplied by the ratio of the tick price to the tick size. For example, if a Futures symbol has USD as the base currency, the contract size is equal to 100, the cost is 33, and the tick price to tick size ratio is 1/0.1, then the value of one lot of the position will be equal to 100*33*10 = USD 33,000. For a CFD symbol with the same parameters, one lot size will be 100*33 = USD 3,300.  
CONDITION_LOGIN | 1000 | The number of a client's account. This parameter allows creating individual rules for accounts.  
CONDITION_GROUP | 1001 | The group to which the client's account is included. This parameter is used for configuring rules for separate account groups.  
CONDITION_COUNTRY | 1002 | In this parameter a client's country can be specified. The specified rule will be applied to all clients living in this country.  
CONDITION_CITY | 1003 | Use this parameter to apply the rule to all clients living in a specified city.  
CONDITION_COLOR | 1004 | Use this parameter to apply the rule for clients that are marked with the specified color.  
CONDITION_LEVERAGE | 1005 | Use this parameter to apply the rule for clients with the specified leverage.  
CONDITION_COMMENT_CLIENT | 1006 | Use this parameter to apply the rule for clients with the specified comment ([IMTUser::Comment](../../../Database-Interfaces/Users/IMTUser/Comment.md) field in the client record).  
CONDITION_ZIPCODE | 1007 | Use this parameter to apply the rule for clients with the specified zip code ([IMTUser::Zipcode](../../../Database-Interfaces/Users/IMTUser/ZipCode.md)).  
CONDITION_STATUS | 1008 | Use this parameter to route requests based on the client status ([IMTUser::Status](../../../Database-Interfaces/Users/IMTUser/Status.md)). For example, by combining it with the CONDITION_COUNTRY and CONDITION_SYMBOL parameters, you can prevent non-US clients from trading US stocks.  
CONDITION_MARGIN | 2000 | Use this parameter to set up rule application depending on the margin volume that is currently reserved (in the deposit currency).  
CONDITION_MARGIN_LEVEL | 2001 | This parameter allows using rules depending on the current margin level (in percents).  
CONDITION_MARGIN_FREE | 2002 | This parameter allows using rules depending on the current amount of free margin (in the deposit currency).  
CONDITION_EQUITY | 2003 | This parameter allows using rules depending on the current equity on a client's account (in the deposit currency).  
CONDITION_BALANCE | 2004 | This parameter allows using rules depending on the current balance of a client (in the deposit currency).  
CONDITION_PROFIT | 2005 | This parameter allows using rules depending on the current floating profit of a client.  
CONDITION_DAILY_DEALS | 3000 | This parameter allows using rules depending on the number of deals of a client for the current and previous days (including weekends and holidays).  
CONDITION_DAILY_DEALS_PERIOD | 3001 | The frequency of deals for a day. Calculated on the basis of the last 8 deals (the average time in seconds between deals).  
CONDITION_DAILY_PROFIT | 3002 | The profit of the client, whose request is being handled, for the current and previous days (including weekends and holidays).  
CONDITION_POSITION_VOLUME | 4000 | The current volume of a position for the symbol, for which a request has arrived.  
CONDITION_POSITION_PROFIT | 4001 | The current profit of a position for the symbol, for which a request has arrived.  
CONDITION_POSITION_AGE | 4002 | Using this parameter you can specify time in seconds elapsed since position opening for the symbol a request for which is currently being handled. This parameter allows to track positions based on the time they have been held.  
CONDITION_POSITION_MODIFY_TIME | 4003 | Using this parameter you can specify time in seconds elapsed since the last modification of a position for the symbol a request for which is currently being handled. Position modification means increase of its volume and partial closure. This parameter allows to prevent evasion of the previous rule (CONDITION_POSITION_AGE) through manipulating one position, increasing or reducing its volume.  
CONDITION_POSITION_AVERAGE_TIME | 4004 | This parameter allows to track positions based on the time the average age of the position for the symbol for which a request is being handled. The average position age is calculated as follows: Current time — ((Open time + Modification time)/2).  
CONDITION_POSITION_TOTAL | 4005 | This parameter allows tracking the total number of a client's open positions on all symbols. For example, you can set the platform to reject trade requests to open new positions, if the client has reached the specified limit.  
CONDITION_POSITION_TOTAL_SYMBOL | 4006 | The parameter allows tracking the number of positions on the symbol that is specified in the current trade request. For example, if a client has placed an order on EURUSD, this condition will check the current number of the client's open positions on EURUSD.  
CONDITION_ORDER_TOTAL | 4007 | This parameter allows tracking the total number of a client's orders on all symbols. All orders are taken into account, including pending and history orders. Each opening and closing of a position (including partial closure), as well as placing of a pending order increases this counter.  
CONDITION_ORDER_TOTAL_SYMBOL | 4008 | The parameter allows tracking the number of orders on the symbol that is specified in the current trade request. For example, if a client has placed an order on EURUSD, this condition will check the current number of the client's orders (both active and history) on EURUSD.  
CONDITION_POSITION_SL_TOUCHED | 4009 | The condition is triggered when the market price touches the stop loss of a position (while the stop loss may not be activated yet). Possible values — true or false.  
CONDITION_POSITION_TP_TOUCHED | 4010 | The condition is triggered when the market price touches the take profit of a position (while the take profit may not be activated yet). Possible values — true or false.  
CONDITION_ORDER_SL_TOUCHED | 4011 | The condition is triggered when the market price touches the stop loss of a pending order. Possible values — true or false. In combination with the [IMTConRoute::REQUEST_ACTIVATE (#enrouteflags)](../IMTConRoute/Enumerations.md#enrouteflags) condition, it allows you to track the simultaneous breakthrough of a pending order (trigger) and its stop loss level. This may occur during a release of important news or after a weekend when a large price gap is formed.  
CONDITION_ORDER_TP_TOUCHED | 4012 | The condition is triggered when the market price touches the stop loss of a pending order. Possible values — true or false. In combination with the [IMTConRoute::REQUEST_ACTIVATE (#enrouteflags)](../IMTConRoute/Enumerations.md#enrouteflags) condition, it allows you to track the simultaneous breakthrough of a pending order (trigger) and its take profit level. This may occur during a release of important news or after a weekend when a large price gap is formed.  
CONDITION_ORDER_ENTRY_IN | 4013 | Orders, as a result of which the trader enters the market, increases the current position or reverses it. When a new order is received, the platform calculates the effect of the order execution on the current account state: whether a new position will be opened or existing one will be closed or reversed. The check applies to market orders (the effect of the order execution) and for pending orders (the effect of the order triggering and execution at a price specified therein).

  * On hedging accounts: any pending order is considered an entry order, since its execution can only lead to the opening of a new position.
  * On hedging accounts: triggering of Stop Loss, Take Profit and Stop Out is considered an exit order, since this always leads to closing of existing positions.
  * On netting accounts: order direction is determined relative to the current uncovered volume of the symbol, taking into account the existing open position and all pending orders for that symbol. For example, the account has a Buy 1.00 position, a Buy Limit 2.00 order and a Sell Limit 1.00 order. If both pending orders were triggered, the trader would have the resulting position Buy 2.00. This resulting position is taken into account when checking the "Order In" rule. For example, if the trader places a Buy Limit order with the volume of 1.00, the system considers it an entry order. A Sell Limit 1.00 order would be considered an exit order.
  * On netting accounts: for the rule checks performed for pending orders, a position having a Stop Loss or Take Profit level, is considered to be fully covered, so the calculated final uncovered position volume is considered to be zero. For example, the account has a Buy 1.00 position with a specified Stop Loss, a Buy Limit 2.00 order and a Sell Limit 1.00 order. If both pending orders were triggered, the trader would have the resulting position Buy 1.00. This resulting position is taken into account when checking the "Order In" rule for pending orders.

  
CONDITION_ORDER_ENTRY_OUT | 4014 | Orders, as a result of which the trader exits the market, partially closes the current position or reverses it. The rule is similar to CONDITION_ORDER_ENTRY_IN.  
CONDITION_POSITION_VALUE | 4015 | Position value in the symbol's base currency. The value calculation depends on the symbol's margin/profit calculation mode ([IMTConSymbol::CalcMode](../../Symbols/IMTConSymbol/CalcMode.md)). For symbols with the Forex calculation mode, the value is equal to the product of the contract size and the volume. For example, for EURUSD with the contract size of 100,000, the value of 1 lot is equal to EUR 100,000. For symbols with the CFD, CFD Leverage, CFD Index and Futures calculation modes, the contract size is not expressed in money, but, for example, in the number of shares. Therefore, the contract size is additionally multiplied by the symbol value to obtain the value in monetary terms. For Futures symbols, the final value is additionally multiplied by the ratio of the tick price to the tick size. For example, if a Futures symbol has USD as the base currency, the contract size is equal to 100, the cost is 33, and the tick price to tick size ratio is 1/0.1, then the value of one lot of the position will be equal to 100*33*10 = USD 33,000. For a CFD symbol with the same parameters, one lot size will be 100*33 = USD 3,300.  
CONDITION_SYMBOL_SPREAD | 5000 | Current spread. The parameter allows applying routing rules depending on the difference between the current Bid and Ask prices (as at the time of check) of the financial symbol from the trade request. For example, you can forward trade requests to a dealer if the spread increases a certain value.  
CONDITION_FIRST |  | Beginning of enumeration. Corresponds to CONDITION_DATETIME.  
CONDITION_LAST |  | End of enumeration. Corresponds to CONDITION_SYMBOL_SPREAD.  
  
This enumeration is used in the [IMTConCondition::Condition](Condition.md) method.

<a id="enconditionrule"></a>
## IMTConCondition::EnConditionRule (#enconditionrule)

Types of parameter and value comparison are enumerated in IMTConCondition::EnConditionRule.

ID | Value | Description  
RULE_EQ | 0 | Condition of equality.  
RULE_NOT_EQ | 1 | Condition of inequality.  
RULE_GREATER | 2 | Condition of "greater than".  
RULE_NOT_LESS | 3 | Condition of "not less than".  
RULE_LESS | 4  | Condition of "less than".  
RULE_NOT_GREATER | 5 | Condition of "not greater than".  
RULE_FIRST |  | Beginning of enumeration. Corresponds to RULE_EQ.  
RULE_LAST |  | End of enumeration. Corresponds to RULE_NOT_EQ.  
  
This enumeration is used in the [IMTConCondition::Rule](Rule.md) method.

<a id="enconditiontype"></a>
## IMTConCondition::EnConditionType (#enconditiontype)

Types of parameters are listed in IMTConCondition::EnConditionType.

ID | Value | Description  
TYPE_NONE | 0 | Parameter is not specified.  
TYPE_STRING | 1 | The parameter is of the string type.  
TYPE_INT | 2 | The parameter is of the int type.  
TYPE_UINT | 3 | The parameter is of the uint type.  
TYPE_DOUBLE | 4  | The parameter is of the double type.  
TYPE_COLOR | 5 | The parameter is of the color type.  
TYPE_MONEY | 6 | The parameter expresses the amount of money.  
TYPE_VOLUME | 7 | The parameter expresses volume.  
TYPE_DATETIME | 8 | The parameter expresses date and time (in seconds that have elapsed since 01.01.1970).  
TYPE_LEVERAGE | 9 | The parameter expresses a leverage.  
TYPE_BOOL | 10 | The parameter is of the bool type.  
TYPE_TIME | 11 | The parameter expresses time (in minutes since 00:00).  
TYPE_WEEKDAY | 12 | The parameter expresses a weekday (0 - Sunday, 6 - Saturday).  
TYPE_FIRST |  | Beginning of enumeration. Corresponds to TYPE_NONE.  
TYPE_LAST |  | End of enumeration. Corresponds to TYPE_WEEKDAY.  
  
This enumeration is used in the following methods:

  * [IMTConCondition::ValueType](ValueType.md)
  * [IMTConRoute::ParamType](../IMTConRoute/ParamType.md)


