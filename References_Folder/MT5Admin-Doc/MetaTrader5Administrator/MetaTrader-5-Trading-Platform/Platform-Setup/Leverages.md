[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../Platform-Setup.md) / Leverages

[Previous](Holidays.md) | [Next](Groups.md)

<a id="leverages"></a>
# Leverages (#leverages)

In this section, you can configure a list of rules for quickly adjusting the leverage for clients. You can create several profiles and quickly switch between them in the group settings, as well as enable automatic schedule-based adjustments. In essence, this section enables the implementation of a dynamic leverage, often referred to as a floating leverage, which adjusts based on different conditions. For example, leverage values may vary depending on the volume of positions on the client account, on the day of the week or time of day, etc.

This system does not affect the [basic margin calculation principles](Symbols/Symbol-Settings/Trade/Margin-Calculation.md) set for trading instruments. It allows you to change leverage by applying an additional coefficient to the initial and maintenance margin values calculated in accordance with the symbol settings.

![Configuring leverage profiles](images/leverages.png)

Create a new configuration (profile), specify its name, and then add floating leverage rules. You can add multiple rules within one profile. For example, you can add separate rules for different types of symbols. When you enable this profile for a group, all rules will be applied.

Keep in mind that rules are checked and applied top to bottom. If the same instrument matches multiple rules, only the first applicable rule will be used.

![Leverage rule](images/leverages_rule.png)

Set general parameters for the rule:

  * Name — the name of the rule. Set descriptive names that reflect their purpose.
  * Description — an extended description of the rule.
  * Symbol — symbol or group of symbols to which the rule will apply.



You can create multi-level rules and change the leverage in different ways depending on the volume/value of the trader's positions. Select the desired condition in the Range parameter:

  * Volume — the total volume of open positions for all symbols from the Symbols field. The volume is specified in the lots number.
  * Volume per symbol — unlike the previous option, this parameter refers to the volume of open positions for each individual symbol from the Symbols field. For example, if all symbols Forex\* are specified, the volume for each instrument from this group is considered. The system calculates the volume of Forex\EURUSD positions, checks the applicable range, and applies the appropriate margin ratio. Next, it checks Forex\GBPUSD, Forex\USDJPY, and all the other symbols included in this group.
  * Notional value — the total value of open positions for all instruments from the Symbols field. The value is calculated based on the position opening price and is converted to the currency specified in the Currency field. If the Currency field is empty, the value is converted to the [deposit currency (#currency)](Groups/Group-Settings.md#currency) of the group for which the margin is calculated. The current exchange rate is used for conversions.
  * Notional value per symbol — unlike the previous option, this parameter refers to the value of open positions for each individual symbol from the Symbols field. For example, if all symbols Forex\* are specified, the system considers the notional value for each instrument from this group. The system calculates the value of Forex\EURUSD positions, checks the applicable range, and applies the appropriate margin ratio. Next, it checks Forex\GBPUSD, Forex\USDJPY, and all the other symbols included in this group.



Margin levels are configured at the bottom of the window. Specify the maximum values in the To field. The minimum value is set automatically based on the value of the previous range. Depending on the Range parameter, the field indicates the positions volume or notional value. For example, the Range field is set to "Volume". In this case, a level up to 10 means that the specified margin rates will be applicable if the total volume of the client's open positions for the specified symbols does not exceed 10 lots.

If you do not need multilevel rules, set one level covering the entire range of values for the selected condition.

Next, set the initial and maintenance margin ratios for each level. They will be applied to the margin values [calculated based on the symbol types and settings](Symbols/Symbol-Settings/Trade/Margin-Calculation.md). The initial margin Ratio applies to all open orders, including market orders. Set both margin ratios explicitly. Unlike [symbol settings](Symbols/Symbol-Settings/Margin-Rates.md), here the zero maintenance margin does not indicate that the initial margin ratio will be used instead. The zero value means that no margin will be charged.

> Floating leverage settings only work for groups with the "[for Retail Forex, CFD, Futures (#risk)](Groups/Group-Settings.md#risk)" calculation type (hedging and netting). The settings do not apply for groups with exchange calculation type.

<a id="assign"></a>
## Applying leverage configurations (#assign)

To apply a leverage configuration, open the Margin section in the [group settings (#floating-leverage)](Groups/Group-Settings.md#floating-leverage) and select the required configuration:

![Select the leverage configuration in the group settings](images/leverages_group.png)

To apply and disable settings in bulk, use the context menu in the Leverages section:

![Applying leverage settings to multiple groups](images/leverages_assign_menu.png)

If a leverage profile has been set for a specific set of groups, you can quickly replace it with another. Click Edit Groups in the profile context menu. This will open the [bulk group editing (#groupwork)](General-Information/Working-with-Instructions.md#groupwork) dialog. Update the corresponding field in this dialog. With this feature, you don't have to edit each group individually.

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



Let's calculate the account margin before applying the leverage rule: 22 * 100,000 / 100 = 22,000 USD. Since the maintenance margin rate is zero for a pending order, the initial margin rate is applied as the maintenance margin rate.

Now we apply the leverage rule, and the margin increases to 36,000. Let's look at how we got this value:

  * First, the system determines how much margin is charged for each lot. In this case, it is 22,000 / 22 = 1,000 USD.
  * Next, the margin is calculated for positions. The system determines the configured margin rule ranges in which the position lots fall. The first 10 lots fall into the first range with a margin rate of 1. For these lots, the system charges a margin of 10 * 1,000 * 1 = 10,000 USD. The remaining two lots fall into the second range with a rate of 2. For them, the system charges a margin of 2 * 1,000 * 2 = 4,000 USD.
  * Next, the system checks the orders. Since the system considers the volume of positions and orders in the aggregate, the first 8 lots of the order fall into the second range (12 lots position + 8 lots order). The charged margin is equal to 8 * 1,000 * 2 = 16,000 USD. The remaining 2 lots of the order fall into the third range with a rate of 3. The margin is equal to 2 * 1,000 * 3 = 6,000 USD.
  * The total margin: 10,000 + 4,000 + 16,000 + 6,000 = 36,000 USD



The approach based on per-lot margin calculations enables the transparent application of rates specified in the rule for any combination of positions. For example, the account has the following positions:

  * Buy 2.00 EURUSD, margin is 1,800 USD (including conversion from EUR to USD)
  * Sell 1.00 USDCHF, margin is 1,000 USD
  * Buy 15.00 USDJPY, margin is 15,000 USD



The margin per lot is (1,800 + 1,000 + 15,000)\(2 + 1 + 15) = 988.88. Next, the total volume is split into levels from the rule. The first 10 lots will be included in the first level and the remaining 8 are in the second one. Margin = (10 * 988.88) + (8 * 988.88 * 2) = 25,710.88 USD. The order in which the positions are considered does not matter.

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
  * The [hedged margin (#hedged)](Symbols/Symbol-Settings/Margin.md#hedged) for EURUSD is 50,000.



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



<a id="conversion"></a>
## Consideration of the conversion rate in margin calculation at notional value (#conversion)

If the margin currency of the instrument differs from the currency in which the notional value of the position is calculated, the floating margin will be recalculated in real-time based on the applicable exchange rate. Let's consider example:

The floating margin rule uses levels based on the notional value of positions. The currency is set to USD. The following levels and rates are set:

  * Up to 100,000 - 0.33
  * Up to 300,000 - 0.5
  * Up to 500,000 - 0.75
  * Up to 2,500,000 - 1
  * More than 2,500,000 - 1.



A user with a leverage of 1:100 opens a 100-lot AUDCHF position. Let's calculate the value of this position in the margin currency: 100 * 100,000 AUD = 10,000,000 AUD.

Let's calculate the value of this position in USD at the current rate: Ask AUDUSD = 0.63014. 10,000,000 * 0.6301400 = 6,301,400 USD.

Let's calculate the margin for the total notional value in accordance with the leverage-based rates:

  * 100,000 * 0.33 / 100 = 330 USD
  * 200,000 * 0.5 / 100 = 1,000 USD
  * 200,000 * 0.75 / 100 = 1,500 USD
  * 2,000,000 * 1 / 100 = 20,000
  * 3,801,400 * 1.1 / 100 = 41,815.40



The total margin will be 64,645.40 USD. If the currency in the rule differs from the client's deposit currency, the resulting value will be additionally converted at the "Margin Ratio" rate, which is [stored in the position (#margin-rate)](Positions.md#margin-rate). This rate does not change over time.

On the client terminal side, the margin is recalculated with each tick. Therefore, in cases as described above, you will see margin changes in real time. In manager terminals, the margin in the account properties is updated only upon request. As a result, margin changes will be visible only when reopening the corresponding dialog.  
---  
  
<a id="automation"></a>
## Automatic leverage adjustments (#automation)

You can apply leverage profiles depending on various conditions using the [Automations](Automations.md) service. For example, you can turn on a certain profile on Friday evening and then turn it off on Monday morning before the markets open.

Create a new task and select the relevant [triggers](Automations/Triggers.md) and [conditions](Automations/Conditions.md). For example, to switch a profile at a specific time, use the 'Scheduled Event' trigger. Set the action to ['Update group configuration' (#configuration)](Automations/Actions.md#configuration). To change only the leverage parameter, click 'Add Diff'. Next, select the desired group and specify the leverage profile in its settings:

![To adjust leverage values on a schedule, create an automation task](images/leverages_automation.png)

Next, create a relevant task that will disable the leverage profile in the group.
