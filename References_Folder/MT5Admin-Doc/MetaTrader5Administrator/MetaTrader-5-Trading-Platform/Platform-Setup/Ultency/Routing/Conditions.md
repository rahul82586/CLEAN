[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../Platform-Setup.md) / [Ultency](../../Ultency.md) / [Routing](../Routing.md) / Conditions

[Previous](../Routing.md) | [Next](../Matching-Orders.md)

<a id="routing-conditions"></a>
# Routing Conditions (#routing-conditions)

The routing rule settings specify a set of conditions defining which trade requests will be processed according to this rule.

![Conditions for a routing rule](images/ultency_routing_conditions.png)

<a id="comparison-types"></a>
## Comparison Types (#comparison-types)

Standard comparison types are available for all conditions:

  * Equal (=)
  * Not equal (!=)
  * Greater than (>)
  * Greater than or equal (>=)
  * Less than (<)
  * Less than or equal (<=)



For string conditions, such as country name, symbol, or email, the Match Mask condition is also available. Here you can specify strings with the "*" mask. For example:

  * Condition "Symbol", value "Forex\USD*"  all symbols from the Forex group, where the underlying currency is USD.
  * Condition "Email", value "*@mailbox.com" applies to all email addresses on the mailbox.com domain.



For login conditions, you can specify multiple values and value ranges. For example, Account\Login = 100,102,107,120-130.

<a id="time"></a>
## Time (#time)

These parameters set date and time conditions. A rule will be triggered if a request arrives on the specified date or within the specified time range.

<a id="accounts"></a>
## Accounts (#accounts)

These settings specify conditions based on account parameters:

  * Login â the trading request was submitted from the specified account.
  * Group, Country, City, Language, Phone, Email, Color, Status, Company  the trading request was submitted from an account that belongs to the specified [group (#account)](../../Accounts/Editing-Account.md#account), [country (#personal)](../../Accounts/Editing-Account.md#personal), [city (#personal)](../../Accounts/Editing-Account.md#personal), etc. 
  * Comment â the comment added by the client to the trading request (order).
  * Registration â the condition is set relative to the account creation date in the platform. Specify the date and the comparison type: equal to, less than, or greater than. Accordingly, the condition will trigger for accounts registered on the specified date, earlier or later than this date.
  * Last visit â the condition is set relative to the last connection of the account to the platform. Specify the date and the comparison type: equal to, less than or greater than. Accordingly, the condition will trigger for account connected on the specified date, earlier or later than this date.
  * Days since registration â the condition is set relative to the number of days that have passed since the account was created. The number of days is calculated based on the number of times the clock crosses midnight (00:00) since the event. The principle of operation and purpose of this condition are similar to the "Registration" condition.
  * Days since last login â the condition is set relative to the number of days that have elapsed since the last connection to the account. The number of days is calculated based on the number of times the clock crosses midnight (00:00) since the event. The principle of operation and purpose of this condition are similar to the "Last visit" condition.
  * Days since last trade activity â condition is set relative to the number of days that have elapsed since the last operation on the account. This considers any trading operations, commission charges, etc. Balance operations are not taken into account. In addition, the system checks if the account has any open positions or active pending orders. When using this condition, please note that newly registered accounts may also fall under this condition. For example, a trader may have created an account 1-2 days ago and has not yet performed any trading operations. If you set a condition based on the absence of trading activity in the last 180 days, this trader will also be included in the automation action. To avoid such situations, use the trading activity condition in conjunction with other conditions, such as "Registration" or "Days since registration".  
The calculated number of days is rounded down. For example, if 5 days and 23 hours have passed since the event, this will be counted as 5 days.
  * Online â condition is set relative to the status of the account connection to the trade server. Possible values are "true" and "false", i.e. the account is either connected (any connection type: client terminal, mobile terminal, and so on) or not.
  * Leverage â the condition is set relative to the [account leverage (#account)](../../Accounts/Editing-Account.md#account). For example, the regulator's requirements have changed, and you need to disable trading with a leverage greater than 1:20 on accounts from the US. Set two conditions: "Country = USA", Leverage > 1:20. Assign the action "Decline" to this rule.
  * Balance â the condition is set relative to the current [account balance (#account-state)](../../Accounts/Editing-Account.md#account-state), the amount is indicated in the [deposit currency (#currency)](../../Groups/Group-Settings.md#currency).
  * Credit is similar to the "Balance" condition. In this case, the amount of [credit funds on the account (#account-state)](../../Accounts/Editing-Account.md#account-state) is checked.
  * Total positions â the condition is set by the number of open [positions](../../Positions.md) that currently exist on the account. This action allows you to control extremely active accounts. For example, set "Total positions > 100", "Group = real\*". Assign the action "Decline" to this rule.
  * Total orders â similar to the "Total positions" condition, it checks the number of active pending orders on the account.
  * Floating profit, Equity, Margin, Free margin, Margin level â these conditions are similar to the "Balance" condition. Appropriate [trading account states (#account-state)](../../Accounts/Editing-Account.md#account-state) are checked here.
  * Deposit currency â the request arrived from an account with the specified [deposit currency (#currency)](../../Groups/Group-Settings.md#currency).
  * Lead Source, Lead Campaign â [lead source and campaign (#leadsource)](../../Accounts/Editing-Account.md#leadsource) parameters specified in the account.
  * Enabled â the condition is specified relative to the "[Enable this account (#enable)](../../Accounts/Editing-Account.md#enable)" setting.
  * Trading enabled, Algo trading by Expert Advisors enabled â the conditions are set relative to the corresponding [trading settings (#limits)](../../Accounts/Editing-Account.md#limits).
  * Agent account â the condition is set relative to the [agent account (#agent-account)](../../Accounts/Editing-Account.md#agent-account) specified in the trading account settings.
  * Own funds percentage â when trading, clients are able to use their own funds they deposited in their accounts, as well as the credit and bonuses provided by a broker. Both types of funds increase their Equity parameter. The "Own funds percentage" condition allows configuring the automation task depending on the own funds share on a client's account. 100% means the account has the client's funds only with no credit or bonuses. The value of 0% indicates that only credit and bonus funds are used for trading.  
The value is calculated as (1 - (Credit / Equity)) * 100.  
The fractional part is rounded down during calculation: 1.5% becomes 1%, 0.9% becomes 0%. The parameter value cannot be greater than 100% or less than 0%. If an action is required after the client has spent all their funds, it is more efficient to use the "Own funds volume" condition.
  * Own funds volume â the parameter works similarly to the previous condition, although it applies an absolute own funds value rather than a relative one. Specified in the deposit currency. The calculation equation: Equity - Credit.



<a id="request"></a>
## Request (#request)

These settings define conditions based on the parameters of the trading request received from the client.

  * Symbol â a symbol or a group of symbols for which the rule will apply. You can use masks containing "*" and "!" to define symbols.
  * Volume â the trade volume requested in the order (in lots). This parameter allows configuring rules based on the requested volume, for example, automatically processing requests with a volume of less than 1 lot.


  * Comment â allows comparing the request comment with a specified value. When condition "=" is specified, an exact match is checked. Condition ">" or ">=" searches for the specified substring in a comment line. Condition "<" or "<=" searches for the comment substring in the specified line.


  * Reason â the [reason (#reason)](../../Orders.md#reason) for the creation of the request: whether the order was submitted by a client, Expert Advisor, dealer, etc.


  * Price â the price in the request. In the Instant and Request [execution modes](../../Symbols/Symbol-Settings/Execution.md), this is the price specified by the trader in the order. In Market and Exchange modes, this is the current market price of the instrument. Since prices vary significantly between instruments, it is recommended to use this condition in combination with the "Symbol" condition. It can also be used to set the general price threshold. For example, you can decline all requests with a cost of less than one dollar.
  * Value â the value of the requested operation in the symbol's base currency. Value calculation depends on the symbol's [margin/profit calculation mode (#calculation)](../../Symbols/Symbol-Settings/Trade.md#calculation).



<a id="position"></a>
## Position (#position)

These settings define conditions based on the [parameters of the position](../../Positions.md) affected by the received trading request.

  * Ticket â unique position ticket.
  * Volume â the current position volume for the symbol specified in the request.
  * Type â position type: buy or sell.
  * Open price â the weighted average price of the position opening: (price of deal 1 * volume of deal 1 + ... + price of deal N * volume of deal N) / (volume of deal 1 + ... + volume of deal N).


  * Current price â the price of the financial symbol for which the position has been opened, at the trigger activation time.
  * Current profit â the current floating profit from the position for which the request was received. Specified in the client's deposit currency.
  * Reason â [reason (#reason)](../../Positions.md#reason) for position opening.
  * Creation time â position opening time.
  * Days since creation â time passed since the position was opened.
  * Update time â time when the position was last modified (when its volume was changed).
  * Days since modification â the number of days passed since the last position modification (a change in its volume).
  * Expert ID â identifier (magic number) of an Expert Advisor by which a position was opened in the client terminal.
  * Comment â a text comment to the position.



<a id="order"></a>
## Order (#order)

These settings define conditions based on [order parameters](../../Orders.md).

  * Ticket â the unique order ticket.
  * ID â order identifier in the external system.
  * Setup time â time of order placing by a client.
  * Days since setup â the number of days that have elapsed since the client placed the order. The calculated number of days is rounded down. For example, if the order was placed 3 days and 22 hours ago, this will be counted as 3 days.
  * Expiration time â order expiration date, if it was set by the client.
  * Type â order type: "Buy", "Sell", "Buy Limit", "Sell Limit", "Buy Stop", "Sell Stop", "Buy Stop Limit", "Sell Stop Limit" or "Close By".
  * Order price â price specified by the trader for the order execution.
  * Trigger price â this field is used for the "Buy Stop Limit" and "Sell Stop Limit" orders. It sets the price level at which the orders trigger and the relevant limit orders are placed.


  * Current price â the price of the financial symbol for which the order has been opened, at the request arrival time.


  * Stop Loss â the Stop Loss level.
  * Take Profit â the Take Profit level.
  * Initial volume â volume requested in the order.
  * Remained volume â if the order is not filled in the volume requested by the trader this field will display the remainder volume.
  * State â current order state: Started, Placed, Partially Filled, Rejected, Filled, etc. 
  * Expert ID â identifier (magic number) of an Expert Advisor that placed the order in the client terminal.
  * Position â the ticket of the position that will be modified or closed as a result of the execution of this order.
  * Comment â a text comment to the order.
  * Contract size â the contract size of the symbol, for which an order was placed.
  * Currency â the deposit currency of the client who has placed the order.


