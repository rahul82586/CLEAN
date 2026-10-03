[🏠 Document Start](../README.md) / [Managing Trade Server Settings](README.md) / Margin

[Previous](Spread-Commission-and-Swap.md) | [Next](Managing-Plugins.md)

<a id="margin"></a>
# Managing margin settings (#margin)

For managers who work in the platform within a White Label and do not have full access to the platform configuration, the Manager terminal provides the ability to control their clients' margin settings. These settings are configured separately for each group. Select the ![Groups](images/groups_icon_1.png) Groups section in the Navigator and then choose a necessary group.

![Managing margin settings](images/margin.png)

The following parameters are available here:

  * Risk management — the platform provides two main risk management models for [OTC](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Retail-Forex-CFD-Futures-—-Netting.md) and [exchange market](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Stock-Exchange.md). This parameter cannot be changed.


  * for Retail Forex, CFD, Futures — margin is calculated in accordance with the parameters specified in the group settings (the margin call and stop out level, unrealized and daily returns, etc.). The [netting position accounting (#netting)](../Trading-Operations/Basic-Principles.md#netting) is used.
  * for Retail Forex, CFD, Futures with hedging — used for OTC market. Margin calculation is based on the type of instrument, as well as group settings. The [hedging position accounting (#hedging)](../Trading-Operations/Basic-Principles.md#hedging) is used.
  * for Stock Exchange, based on margin discount rates — exchange calculation. The margin is controlled in accordance with the margin rates (discount) specified in the symbol settings.
  * Margin call level — level of client's funds, reaching which the account enters the Margin Call (insufficient funds) state. Clients in this state are displayed in a [special window](../Dealing-and-Risk-Management/Accounts-with-Margin-CallStop-Out.md) of the client terminal. The manager can send a notification to such clients asking to add money to their accounts. The Margin Call state does not affect the possibility of opening new trading positions. Only used for the 'for Retail Forex*' modes.  
In the 'for Stock Exchange' mode, a Margin Call occurs when the initial margin on the client's positions becomes greater than the equity.
  * Stop out level — level of funds, at which client's orders are forcibly canceled and trading positions are closed. The stop out processing is described below. Only used for the 'for Retail Forex*' modes.  
In the 'for Stock Exchange' mode, a Stop Out occurs when the maintenance margin on the client's positions becomes greater than the equity.
  * Compensate negative balance after stop out — automatically perform on a client's account the special operation, which increases the balance and sets it to zero, if the balance has become negative after a position was closed by Stop Out. The details are available below.
  * Withdraw credit after negative balance compensation — works as an addition to the previous option. If enabled, the credit funds on the account will be set to zero after a negative balance compensation operation. Credit funds are withdrawn in a separate balance operation with the "so credit compensation" type.


  * Floating leverage — additional margin calculation rules for clients in the group. You can quickly switch between different margin profiles available under the Leverages section.



The levels of Margin Call and Stop Out can be set in % and money. In the former case, they are determined as the account's Equity value. If "In percent" is selected, the levels are defined as the account "Margin level" value (Funds/Margin*100).

  * The list of available groups is defined in the manager account configuration via the MetaTrader 5 Administrator terminal. The "Edit groups" permission defines the availability of the group settings editing option.
  * To change the settings of several groups at once, double click on the subgroup name in the tree, for example, "real", "demo", etc.

  
---  
  
<a id="compensate"></a>
## Compensation of a negative balance after a Stop Out (#compensate)

If positions are forcedly closed in the situation of a Stop Out, the balance of a client can become negative. This may happen during sharp market moves. According to the rules set out by some Regulators, for example by [the European Securities and Markets Authority](https://www.esma.europa.eu/), clients' balances may not fall below zero. Therefore, you should enable the 'Compensate negative balance after stop out' for clients from countries where such rules apply.

The server forcibly closes the client's positions upon the situation of a Stop Out. If the compensation is enabled, and the client's balance has become negative after the closing of the last position, the 'so compensation' operation is immediately performed on this account to increase the balance to zero:

![Compensating a negative balance as a separate 'so compensation' operation.](images/so_compensation.png)

The standard ["StopOuts Compensation Report"](../Server-Reports/StopOut-Compensations.md) allows controlling such compensation operations. This report includes all deals with the "so compensation" type.

<a id="symbol-margin"></a>
## Margin settings for symbols (#symbol-margin)

Margin settings are specified for symbol groups available to an account group. The list of available groups can only be changed from MetaTrader 5 Administrator. Managers can only re-define symbol settings for a certain client group.

Select the group of symbols in the Symbols tab. Settings are divided into two sections: Margin and Margin Rates:

![Margin settings for a group of symbols](images/group_symbol_margin.png)

The following parameters are available under the Margin section:

  * Use default margin settings — use the margin parameters configured for a certain symbol in the Administrator terminal (not re-define settings for a certain group).
  * Initial margin — security deposit ([margin (#futures)](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md#futures)), provided for a fixed-term contract to perform a one lot deal.
  * Maintenance margin — minimum security deposit ([margin (#futures)](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md#futures)), a trader should have on his or her account to maintain a one lot position.
  * Hedged margin — the amount of margin charged per each hedged lot of a position. If initial margin is set for an instrument, the hedged margin is specified as an absolute value (in margin currency) terms. If the initial margin is not set (equal to 0), the contract size is specified. The margin is calculated by the appropriate formula corresponding to the type of the instrument and using the specified contract size. For more details please see the [special section (#hedged)](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Retail-Forex-CFD-Futures-—-Hedging.md#hedged).
  * Calculate hedged margin using larger leg — determines the [hedged margin calculation mode (#hedged)](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Retail-Forex-CFD-Futures-—-Hedging.md#hedged): basic or using larger position leg.
  * Exclude long position PnL from free margin and margin level — the option affects the display of positions purchased with own funds, on accounts with margin trading enabled. If the option is enabled, profit/loss of positions for the symbol will be ignored when calculating free margin, margin level and account equity. Also, Stop Out will not be applies to such positions.
  * Recalculate margin exchange rate at the End of Day — if this option is enabled, at the end of the trading day, the server will update the position margin conversion rate at current market prices. For further details, please see [Basic Margin Calculation (#recalculate-margin)](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md#recalculate-margin).
  * Additional margin check — by default, the margin is checked when setting any orders and triggering any pending orders. Additional checks can be included here:


  * before an order execution — in this mode, there is an additional check: a margin is checked before an order execution, after it has been confirmed (checked) by the server (in automated execution), a dealer or a gateway.
  * when a stop loss or a take profit is triggered — enable additional margin check before closing a position by a stop loss or a take profit. If after a closing, a margin level is insufficient for maintaining open positions and orders, take profit/stop loss are not activated, and the position remains open. The verification should always be enabled if trade operations are sent to an external trading system (stock exchange).



The following parameters are available under the Margin Rates section:

  * Liquidity margin rate — in the [exchange risk management model (#assets)](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Stock-Exchange.md#assets), clients can use their own assets as collateral for open positions. The liquidity margin rate determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity). If the value is set to 0, the instrument cannot be used as collateral.
  * Currency margin rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures (#forts)](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md#forts)) traded on Moscow Exchange ([calculating variation margin and security deposit using the current USD exchange rate](https://fs.rts.micex.ru/files/644 "Variation margin and security deposit calculation using the current US Dollar exchange rate") \- in Russian). The values are sent by the Moscow Exchange when using the gateway MetaTrader 5 to MOEX Derivatives.
  * Margin rate — margin rates for various order types are specified in this table. The rates are set for the initial and maintenance margin individually. If no ratio is set for the maintenance margin (set to zero), the initial margin ratio will be used for it.


  * Market Buy Order — multiplier for calculating margin requirements for long positions relative to the [basic margin amount](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md).
  * Market Sell Order — multiplier for calculating margin requirements for short positions relative to the main amount of margin.
  * Buy Limit Order — multiplier for calculating margin requirements for Buy Limit orders relative to the main amount of margin.
  * Sell Limit Order — multiplier for calculating margin requirements for Sell Limit orders relative to the main amount of margin.
  * Buy Stop Order — multiplier for calculating margin requirements for Buy Stop orders relative to the main amount of margin.
  * Sell Stop Order — multiplier for calculating margin requirements for Sell Stop orders relative to the main amount of margin.
  * Buy Stop Limit Order — multiplier for calculating margin requirements for Buy Stop Limit orders relative to the main amount of margin.
  * Sell Stop Limit Order — multiplier for calculating margin requirements for Sell Stop Limit orders relative to the main amount of margin.



To avoid overriding the coefficient value for a group, leave the value set to "Default". In this case, the corresponding value from the symbol settings set using the administrator terminal will be used. The "Use Default Settings" command applies these default values to all parameters in this section.

  * If the initial margin is specified, there will be no margin calculations using [symbol type](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md) based formulas.
  * If the amount of the maintenance margin is not specified, the initial margin value will be used instead.
  * If the exchange risk management model is used for the client group, and a symbol has 0 margin rates, then the margin is not charged for operations by that symbol.

  
---  
  
Please find the details of margin calculation in a [separate section](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Retail-Forex-CFD-Futures-—-Netting.md).

<a id="leverage"></a>
## Floating Margin (#leverage)

Rules can be created in the Leverages section to enable quick adjustments of client leverages/margin. If several profiles are created, you can quickly switch between them in the group settings. In essence, this section enables the implementation of a dynamic leverage, often referred to as a floating leverage, which adjusts based on different conditions. For example, leverage values may vary depending on the volume of positions on the client account, on the day of the week or time of day, etc.

This system does not affect the [basic margin calculation principles](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md) set for trading instruments. It allows you to change leverage by applying an additional coefficient to the initial and maintenance margin values calculated in accordance with the symbol settings.

![Configuring leverage profiles](images/leverages.png)

Through the Manager terminal, you can only apply existing leverage profiles to groups. To create or change profiles, use the Administrator terminal.

Each profile consists of a set of leverage rules. Multiple rules can be added within one profile. For example, you can add separate rules for different types of symbols. When you enable this profile for a group, all rules will be applied.

![Leverage rule](images/leverages_rule.png)

Set general parameters for the rule:

  * Name — the name of the rule. Set descriptive names which reflect their purpose.
  * Description — an extended description of the rule.
  * Symbol — symbol or group of symbols to which the rule will apply.



You can create multi-level rules and change the leverage in different ways depending on the volume/value of the trader's positions. Select the desired condition in the Range parameter:

  * Volume — the total volume of open positions for all symbols from the Symbols field. The volume is specified in the lots number.
  * Volume by symbol — unlike the previous option, this parameter refers to the volume of open positions for each individual symbol from the Symbols field. For example, if all symbols Forex\* are specified, the volume for each instrument from this group is considered. The system calculates the volume of Forex\EURUSD positions, checks the applicable range, and applies the appropriate margin ratio. Next, it checks Forex\GBPUSD, Forex\USDJPY, and all the other symbols included in this group.
  * Notional value — the total value of open positions for all instruments from the Symbols field. The value is calculated based on the position opening price and is converted to the currency specified in the Currency field. If the Currency field is empty, the value is converted to the deposit currency of the group for which the margin is calculated. The current exchange rate is used for conversions.
  * Notional value by symbol — unlike the previous option, this parameter refers to the value of open positions for each individual symbol from the Symbols field. For example, if all symbols Forex\* are specified, the system considers the notional value for each instrument from this group. The system calculates the value of Forex\EURUSD positions, checks the applicable range, and applies the appropriate margin ratio. Next, it checks Forex\GBPUSD, Forex\USDJPY, and all the other symbols included in this group.



Margin levels are configured at the bottom of the window. Specify the maximum values in the To field. The minimum value is set automatically based on the value of the previous range. Depending on the Range parameter, the field indicates the volume or notional value of positions. For example, the Range field is set to 'Volume'. In this case, a level up to 10 means that the specified margin rates will be applicable if the total volume of the client's open positions for the specified symbols does not exceed 10 lots.

If you do not need multilevel rules, set one level covering the entire range of values for the selected condition.

Next, set the initial and maintenance margin ratios for each level. They will be applied to the margin values [calculated based on the symbol types and settings](../Trading-Operations/For-Advanced-Users/Margin-Calculation-Basic.md). The initial margin Ratio applies to all open orders, including  market orders. Set both margin ratios explicitly. Unlike symbol settings, here the zero maintenance margin does not indicate that the initial margin ratio will be used instead. The zero value means that no margin will be charged.

> Floating leverage settings only work for groups with the "for Retail Forex, CFD, Futures" calculation type (hedging and netting). The settings do not apply for groups with exchange calculation type.

<a id="assign"></a>
## Applying leverage configurations (#assign)

To apply a leverage configuration, open the Margin section in the group settings and select the required configuration:

![Select the leverage configuration in the group settings](images/leverages_group.png)

To apply and disable settings in bulk, use the context menu in the Leverages section:

![Applying leverage settings to multiple groups](images/leverages_assign_menu.png)

If a leverage profile has been previously set for specific groups, you can quickly replace it with another profile. Select 'Edit Groups' in the profile context menu. This will open the bulk group editing dialog. Update the corresponding field in this dialog. With this feature, you don't have to edit each group individually.

Select 'Groups' in the context menu to go to a list of groups for which the selected leverage profile is applied. From this list, you can quickly select groups and update their settings in a bulk operation.

![List of groups for which the leverage profile is applied](images/leverages_group_list.png)

<a id="example"></a>
## Margin calculation example based on volume (#example)

Let's look at the calculation procedure using an example. The following leverage levels are specified:

![Leverage configuration example](images/leverages_example.png)

The calculation is performed in the following environment:

  * The account is in the group with the "for Retail Forex, CFD, Futures with hedging" type and with the deposit currency USD.
  * The group has a leverage of 1:100.
  * The initial and maintenance margin rates for market orders are set to 1. For pending orders, the initial margin rates are set to 1 and the maintenance margin rates are 0.
  * The USDCHF contract size is 100,000; the instrument type is Forex.



The account has:

  * Position 'Buy 12.00 lot USDCHF'
  * Pending order 'Buy Limit 10.00 USDCHF'



Let's calculate the account margin before applying the leverage rule: 12 * 100,000 / 100 = USD 12,000. Since the maintenance margin rate is zero for a pending order, no margin is charged for it.

Now we apply the leverage rule, and the margin increases to 36,000. Let's look at how we got this value:

  * First, the system determines how much margin is charged for each lot of the position. In this case it is 12,000 / 12 = USD 1,000.
  * Next the margin is calculated for positions. The system determines the configured margin rule ranges in which the position lots fall. The first 10 lots fall into the first range with a margin rate of 1. For these lots, the system charges a margin of 10 * 1,000 * 1 = USD 10,000. The remaining two lots fall into the second range with a rate of 2. For them, the system charges a margin of 2 * 1,000 * 2 = USD 4,000.
  * Next, the system checks the orders. Since the system considers the volume of positions and orders in aggregate, the first 8 lots of the order fall into the second range (12 lots position + 8 lots order). The charged margin is equal to 8 * 1,000 * 2 = USD 16,000. The remaining 2 lots of the order fall into the third range with a rate of 3. The margin is equal to 2 * 1,000 * 3 = USD 6,000.
  * Resulting margin: 10,000 + 4,000 + 16,000 + 6,000 = USD 36,000



The approach based on per-lot margin calculations enables transparent application of rates specified in the rule for any combination of positions. For example, the account has the following positions:

  * Buy 2.00 EURUSD, margin is USD 1,800 (including conversion from EUR to USD)
  * Sell 1.00 USDCHF, margin is USD 1,000
  * Buy 15.00 USDJPY, margin is USD 15,000



The margin per lot is (1,800 + 1,000 + 15,000)\(2 + 1 + 15) = 988.88. Next, the total volume is split into levels from the rule. The first 10 lots will be included in the first level and the remaining 8 are in the second one. Margin = (10 * 988.88) + (8 * 988.88 * 2) = USD 25,710.88. The order in which the positions are considered does not matter.

> When opening positions, the initial margin is checked. For open positions, the maintenance margin is checked. For pending orders, the initial margin is always checked.

<a id="example-nominal"></a>
## An example of calculating margin based on the notional value (#example-nominal)

Let's look at an example of calculating margin on the basis of the notional value with hedged positions present on the account. The following leverage levels are specified:

![Leverage configuration example](images/leverages_example_notional.png)

The calculation is performed in the following environment:

  * The account is in the group with the "for Retail Forex, CFD, Futures with hedging" type and with the deposit currency USD.
  * The group has a leverage of 1:500.
  * The initial and maintenance margin rates for market orders are set to 1. For pending orders, the initial margin rates are set to 1 and the maintenance margin rates are 0.
  * The EURUSD contract size is 100,000; the instrument type is Forex.
  * The hedged margin for EURUSD is 50,000.



The account has the following positions:

  * Buy 20.00 EURUSD at 1.08095
  * Buy 10.00 EURUSD at 1.08095
  * Buy 10.00 EURUSD at 1.08095
  * Sell 15.00 EURUSD at 1.08095



For simplicity, we use the same opening price. Let's calculate the margin before the application of leverage rules. We have 40 lots of buy positions and 15 lots of sell positions. Consequently, the uncovered volume is 25 lots, and the covered volume is 15:

  * 25 * 100,000 / 500 = EUR 5,000
  * 15 * 50,000 / 500 = EUR 1,500



Let's convert the margin into the deposit currency (USD) at the position opening rate: 6,500 * 1.08095 = USD 7,026.175.

Now we apply the margin rule:

  * First we calculated the total volume. The margin is charged in full for 25 non-covered lots. For 15 hedged lots, the margin is charged at half the amount, since the hedged margin is specified as half the size of the standard contract (50,000). Thus, this volume can be reduced to the standard 7.5 lots. The total calculated volume is 32.5 lots.
  * Next, we convert the volume into money, since margin levels are set as notional values. 32.5 * EUR 100,000 * 1.08095 = USD 3,513,087.5
  * Then we calculate what share of the total margin (USD 7,026.175) falls on each level, and then apply the relevant rate:
    * 7,026.175 * (200,000 / 3,513,087.5) * 0.1 = USD 40. Unaccounted remainder: 3,513,087.5 - 200,000 = 3,313,087.5
    * 7,026.175 * (800,000 / 3,513,087.5) * 0.2 = USD 320. Unaccounted remainder: 3,313,087.5 - 800,000 = 2,513,087.5
    * 7,026.175 * (1,000,000 / 3,513,087.5) * 0.5 = USD 1,000. Unaccounted remainder: 2,513,087.5 - 1,000,000 = 1,513,087.5
    * 7.026.175 * (1,513,087.5 / 3,513,087.5) * 1 = 3,026.175
  * Next, we sum up the values for each level and get the final margin value: 40 + 320 + 1,000 + 3,026.175 = 4,386.175 USD



<a id="automation"></a>
## Automatic leverage adjustments (#automation)

You can apply leverage profiles depending on various conditions using the [Automations](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation) service. For example, you can turn on a certain profile on Friday evening before trading closes and then turn it off on Monday morning before the markets open. To configure the leverages, please contact the platform administrator.
