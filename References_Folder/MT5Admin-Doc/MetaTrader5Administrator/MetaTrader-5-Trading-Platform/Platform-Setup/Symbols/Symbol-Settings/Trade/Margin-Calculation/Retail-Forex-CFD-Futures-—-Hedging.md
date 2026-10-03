[🏠 Document Start](../../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../../../Platform-Setup.md) / [Symbols](../../../../Symbols.md) / [Symbol Settings](../../../Symbol-Settings.md) / [Trade](../../Trade.md) / [Margin Calculation](../Margin-Calculation.md) / Retail Forex, CFD, Futures — Hedging

[Previous](Retail-Forex-CFD-Futures-—-Netting.md) | [Next](Stock-Exchange.md)

<a id="retail-forex-cfd-futures-hedging"></a>
# Retail Forex, CFD, Futures — Hedging (#retail-forex-cfd-futures-hedging)

This margin calculation model is used for Retail Forex, CFD and Futures with the [hedging position accounting system (#hedging)](../../../../Groups/Position-Accounting-Systems.md#hedging). Unlike to the same model for netting accounts, the presence of [multiple positions/orders of one symbols (#hedged)](Retail-Forex-CFD-Futures-—-Hedging.md#hedged) is additionally taken into account in this calculation method.

The margin amount is calculated in several stages:

  * Basic calculation for a certain symbol
  * [Conversion of margin currency into deposit currency (#conversion)](Retail-Forex-CFD-Futures-—-Netting.md#conversion)
  * [Multiplication by rate (#rate)](Retail-Forex-CFD-Futures-—-Netting.md#rate)
  * [Accounting multiple positions/orders of the same symbol (#hedged)](Retail-Forex-CFD-Futures-—-Hedging.md#hedged)



<a id="main"></a>
## Basic Calculation for a Symbol (#main)

[The basic margin value](Basic.md) in accordance with the symbol type is calculated first. The type is defined by symbol settings in the [Calculation (#calculation)](../../Trade.md#calculation) field.

<a id="conversion"></a>
## Converting into Deposit Currency (#conversion)

The main calculations by formulas is performed in the [symbol margin currency (#margin-currency)](../../Currency.md#margin-currency). Conversion is applied if it differs from the client's deposit currency. For example, the basic calculation for the EURUSD pair with the EUR margin currency will produce the margin value in EUR. If the user's deposit currency is USD, the calculated value will be converted from EUR to USD.

The current exchange rate of margin currency to deposit currency is used for conversion. The Ask price is used for buy deals, and the Bid price is used for sell deals.

Suppose that the basic size of the margin previously calculated for buying one lot of EURUSD is 1000 EUR. If the account deposit currency is USD, the current Ask price of EURUSD pair is used for conversion. For example, if the current rate is 1.2790, the total margin size is 1279 USD.

The margin to deposit currency conversion rate is shown in the "Margin rate" field in [orders](../../../../Orders.md) and [positions](../../../../Positions.md).

For details, please visit the [Conversion](../Conversion.md) section.

<a id="rate"></a>
## Margin rate (#rate)

You can specify in symbol settings additional multipliers (rates) for the margin requirements depending on the position/order type. This can be done in the [Margin rates](../../Margin-Rates.md) tab. The final size of the margin requirements previously calculated regarding conversion into the deposit currency is additionally multiplied by the appropriate rate. In addition, you can completely disable margin charging for any desired types of trading operations. To do this, set the zero margin ratio.

For example, the previously calculated margin for buying one lot of EURUSD is 1279 USD. This sum is additionally multiplied by long margin rate. For example, if it is equal to 1.15, the final margin is 1279 * 1.15 = 1470.85 USD.

<a id="hedging"></a>
## Accounting multiple positions/orders of the same symbol (#hedging)

The hedging system allows having simultaneously multiple open positions of the same financial instrument. This is reflected in margin calculation.

<a id="positionsorders-opened-in-the-same-direction"></a>
### Positions/orders opened in the same direction (#positionsorders-opened-in-the-same-direction)

Their volumes are summed up and the weighted average open price is calculated for them. The resulting values are used for calculating margin by the formula corresponding to the [symbol type (#main)](Retail-Forex-CFD-Futures-—-Hedging.md#main). Margin is calculated separately for pending orders (if the margin rate is non-zero).

For example, the following positions and orders exist on the account:

  * Buy 1 lot at 15.436
  * Buy 2 lot at 15.432
  * Buy Limit 1 lot at 15.412



The CFD Leverage calculation type is used for the instrument, its contract size is 5,000, and the account leverage is 1:100. The margin rate for all types of operations is 1.

  * Calculating the average weighted Open price of Buys positions: (1 * 15.436 + 2 * 15.432)/(1 + 2) = 15.433333333
  * Calculating margin using the [CFD Leverage formula](Basic.md) for the aggregate volume: 3 * 5 000 * 15.433333333 / 100 = 2 315.00
  * Taking into account the margin rate: 2 315.00 * 1 = 2 315.00
  * Calculating margin using the CFD Leverage formula separately for the pending order: 1 * 5 000 * 15.412 / 100 = 770.60
  * Taking into account the margin rate: 770.60 * 1 = 770.60
  * Calculating the final value as the sum of position and order margin values: 2 315.00 + 770.60 = 3 085.60



Further, this value can be converted to the account deposit currency, if necessary.

<a id="opposite-positionsorders"></a>
### Opposite Positions/Orders (#opposite-positionsorders)

Oppositely directed open positions of the same symbol are considered hedged or covered. Two margin calculation methods are possible for such positions. The calculation method is determined by the symbol settings.

Basic calculation | Using the larger leg  
---|---  
Used if the "Calculate hedged margin using larger leg" option is disabled in the [symbol settings](../../Margin.md). The calculation consists of several steps:

  * For uncovered volume
  * For covered volume (if hedged margin size is specified)
  * For pending orders

The resulting margin value is calculated as the sum of margins calculated at each step. Calculation for uncovered volume

  * Calculation of the total volume of all positions and market orders for each of the legs — buy and sell.


  * Calculation of the weighted average position and market order open price for each leg: (open price of position or order 1 * volume of position or order 1 + ... + open price of position or order N * volume of position or order N) / (volume of position or order 1 + ... + volume of position or order N).
  * Calculation of uncovered volume (smaller leg volume is subtracted from the larger one).


  * The calculated volume and weighted average price are used then to calculate margin by the appropriate formula corresponding to the [symbol type](Retail-Forex-CFD-Futures-—-Hedging.md).
  * When considering a [margin rate (#rate)](Retail-Forex-CFD-Futures-—-Hedging.md#rate), the larger leg rate (buy or sell) is used.
  * The weighted average rate value is used when [converting from a margin currency to a deposit one (#conversion)](Retail-Forex-CFD-Futures-—-Hedging.md#conversion).

Calculation for covered volume Used if the "Hedged margin" value is specified in the [symbol settings](../../Margin.md). In this case margin is charged for hedged, as well as uncovered volume. If the initial margin is specified for a symbol, the hedged margin is specified as an absolute value (in monetary terms). If the initial margin is not specified (equal to 0), the contract size is specified in the "Hedged" field. The margin is calculated by the appropriate formula in accordance with the type of the financial instrument, using the specified contract size. For example, we have two positions Buy EURUSD 1 lot and Sell EURUSD 1 lot, the contract size is 100,000. If the value of 100,000 is specified in the "Hedged field", the margin for the two positions will be calculated as per 1 lot. If you specify 0, no margin is charged for the hedged (covered) volume.

> If you migrate margin calculation settings from MetaTrader 4, you should multiply the value of the "Hedged" field by 2. Thus you will receive the same margin value during calculations. For example, if the hedged margin in MetaTrader 4 was 50,000, it should be set to 100,000 in MetaTrader 5.

Per each hedged lot of a position, the margin is charged in accordance with the value specified in the "Hedged Margin" field in the [symbol settings](../../Margin.md):

  * Calculation of hedged volume for all open positions and market orders (uncovered volume is subtracted from the larger leg).
  * Calculation of the weighted average Open price of all positions and market orders: (open price of position or order 1 * volume of position or order 1 + ... + open price of position or order N * volume of position or order N) / (volume of position or order 1 + ... + volume of position or order N).
  * The calculated volume, weighted average price and the hedged margin value are used then to calculate margin by the appropriate formula corresponding to the [symbol type](Retail-Forex-CFD-Futures-—-Hedging.md).
  * When considering a [margin rate (#rate)](Retail-Forex-CFD-Futures-—-Hedging.md#rate), the average value of the buy and sell order rate is used: (Buy rate + Sell rate)/2
  * The weighted average rate value is used when [converting from a margin currency to a deposit one (#conversion)](Retail-Forex-CFD-Futures-—-Hedging.md#conversion).

Calculation for pending orders

  * Calculation of margin for each pending order type separately (Buy Limit, Sell Limit, etc.).


  * The weighted average rate value and the conversion rate for each pending order type is used when taking into account the [margin rate (#rate)](Retail-Forex-CFD-Futures-—-Hedging.md#rate) and the [margin to deposit currency conversion rate (#conversion)](Retail-Forex-CFD-Futures-—-Hedging.md#conversion).

Calculation specifics for hedging orders when using fixed margin When an order opposite to an existing position is placed, the margin on the hedged volume is always calculated using the "Hedge margin" value. For the non-hedged volume, the "Initial margin" value is used when placing an order, and "Maintenance margin" is applied after the appropriate position is opened. These specifics are only valid for symbols with the specified initial and maintenance margin ([Fixed Margin (#fixed)](Basic.md#fixed) or [Futures (#futures)](Basic.md#futures) calculation type). For example, the following parameters are used for EURUSD:

  * Initial margin = 1000
  * Maintenance margin = 500
  * Hedge margin = 500

A trader has a position Buy 1.00 BR-12.18 on a USD account. A margin of 500 USD (as per the "Maintenance margin") is reserved on the trader's account for this position.

  * To open Sell 2.00 BR-12.18, the trader needs the margin of 2000 USD: 500 USD for the existing position, 500 for 1 hedged lot of the new position (in accordance with the "Hedged margin" parameter) and 1000 for 1 non-hedged lot of the new position (as set in the "Initial margin" parameter).
  * Once the position is opened, a margin of 1000 USD will remain reserved on the trader's account: 500 USD for 1 hedged lot (in accordance with "Hedged margin") and 500 USD for 1 non-hedged lot (as specified in the "Maintenance margin").

| Used if the "Calculate hedged margin using larger leg" option is enabled in the [symbol settings](../../Margin.md).

  * Calculation of margin for shorter and longer legs for all open positions and market orders.
  * Calculation of margin for each pending order type separately (Buy Limit, Sell Limit, etc.).
  * Summing up a longer leg margin: long positions and market orders + long pending orders.
  * Summing up a shorter leg margin: short positions and market orders + short pending orders.


  * The largest one of all calculated values is used as the final margin value.

Long side calculation

  * The total volume of long positions and market orders is calculated
  * Calculation of the weighted average Open price of long positions and market orders: (open price of position or order 1 * volume of position or order 1 + ... + open price of position or order N * volume of position or order N) / (volume of position or order 1 + ... + volume of position or order N).
  * The calculated volume and weighted average price are used then to calculate margin by the appropriate formula corresponding to the [symbol type](Retail-Forex-CFD-Futures-—-Hedging.md).


  * The [margin rate (#rate)](Retail-Forex-CFD-Futures-—-Hedging.md#rate) for long positions is taken into account.
  * The weighted average rate value is used when [converting from a margin currency to a deposit one (#conversion)](Retail-Forex-CFD-Futures-—-Hedging.md#conversion).

  
A similar calculation is performed for each type of pending Buy orders: separately for Buy Limit, Buy Stop and Buy Stop Limit orders. All calculated values ​​are summed. Short side calculation

  * The total volume of short positions and market orders is calculated
  * Calculation of the weighted average Open price of short positions and market orders: (open price of position or order 1 * volume of position or order 1 + ... + open price of position or order N * volume of position or order N) / (volume of position or order 1 + ... + volume of position or order N).
  * The calculated volume and weighted average price are used then to calculate margin by the appropriate formula corresponding to the [symbol type](Retail-Forex-CFD-Futures-—-Hedging.md).


  * The [margin rate (#rate)](Retail-Forex-CFD-Futures-—-Hedging.md#rate) for short positions is taken into account.
  * The weighted average rate value is used when [converting from a margin currency to a deposit one (#conversion)](Retail-Forex-CFD-Futures-—-Hedging.md#conversion).

  
A similar calculation is performed for each type of pending Sell orders: separately for Sell Limit, Sell Stop and Sell Stop Limit orders. All calculated values ​​are summed. Total value The largest one of the calculated values is used as the final margin value.  
Example The following positions are present:

  * Sell 1 lot at 1.11943
  * Buy 1 lot at 1.11953
  * Sell 1 lot at 1.11943
  * Buy 1 lot at 1.11953
  * Sell 1 lot at 1.11943

Hedged margin size = 100000. Buy margin rate = 2, for Sell = 4. Leverage 1:500. Calculate uncovered volume: Sell volume (3) - Buy volume (2) = 1 Calculate the weighted average Open price for the hedged volume by all positions: (1.11943 * 1+1.11953 * 1+1.11943 * 1+1.11953 * 1+1.11943 * 1)/5 = 5.59735/5= 1.11947 Calculate the weighted average Open price for the non-hedged volume by all positions of the larger leg: (1.11943 * 1 + 1.11943 * 1 + 1.11943 * 1)/3 = 1.11943 Calculate the margin rate for the hedged volume: (buy rate + sell rate)/2 = (2 + 4)/2 = 3 The larger leg (sell) margin rate is used for the non-hedged volume (sell): 4. Calculate the hedged volume margin using the equation: (2.00 lots * 100000 EUR * 1.11947 * 3) / 500 = 1343.36 Calculate the non-hedged volume margin using the equation: (1.00 lot * 100000 EUR * 1.11943 * 4) / 500 = 895.54 The final margin size: 1343.36 + 895.54 = 2238.90 | Example The following positions and orders exist on the account:

  * Buy EURUSD 1.00 lot at 1.16214
  * Buy EURUSD 2.00 lot at 1.16207
  * Sell EURUSD 1.00 lot at 1.16184
  * Sell EURUSD 1.00 lot at 1.16189
  * Buy Limit EURUSD 1.00 lot at 1.16053
  * Sell Stop EURUSD 1.00 lot at 1.15808
  * Sell Stop EURUSD 1.00 lot at 1.16067

The Forex calculation type is used for the instrument, its contract size is 100000, the account leverage is 1:100 and the deposit currency is USD. The margin rate for all types of operations is 1. Calculating the margin for the long side:

  * Calculating the total volume of Buy positions and market orders: 1 + 2 = 3
  * Calculating the average weighted Open price of Buys positions: (1 * 1.16214 + 2 * 1.16207) / (1 + 2) = 1.16209333
  * Calculating margin using the [Forex formula](Basic.md) for the total volume: 3 * 100000 / 100 = 3000 EUR
  * Converting the resulting value to USD using the weighted average conversion rate: 3000 * 1.16209333 = 3486.28
  * Calculating margin for the Buy Limit order using the [Forex formula](Basic.md): 1 * 100000 / 100 = 1000 EUR
  * Converting margin to USD using the rate from the order: 1 000 * 1.16053 = 1160.53 USD
  * Calculating the total margin value for the long side: 3486.28 + 1160.53 = 4646.81

Calculating the margin for the short side:

  * Calculating the total volume of Sell positions and market orders: 1 + 1 = 2
  * Calculating the average weighted Open price of Sell positions: (1 * 1.16184 + 1 * 1.16189) / (1 + 1) = 1.161865
  * Calculating margin using the [Forex formula](Basic.md) for the total volume: 2 * 100000 / 100 = 2000 EUR
  * Converting the resulting value to USD using the weighted average conversion rate: 2000 * 1.161865 = 2323.73
  * Calculating the total volume of Sell Stop orders: 1 + 1 = 2
  * Calculating the average weighted Open price of the orders: (1 * 1.15808 + 1 * 1.16067) / (1 + 1) = 1.159375
  * Calculating margin using the [Forex formula](Basic.md) for the total volume of Sell Stop orders: 2 * 100000 / 100 = 2000 EUR
  * Converting margin to USD using the weighted average order price: 2000 * 1.159375 = 2318.75 USD
  * Calculating the total margin value for the short side: 2323.73 + 2318.75 = 4642.48

The largest one of the calculated values will be used as the final margin: 4646.81.  
  
<a id="floating-margin"></a>
## Application of floating margin rules (#floating-margin)

Additional rates may be applied to the calculated margin value in accordance with the rules configured in the the [Leverages](../../../../Leverages.md) section.

<a id="check"></a>
## Checking Margin (#check)

When placing new orders, a check is performed of whether there is enough free margin on the trader's account for the appropriate order. An additional free margin check can be performed after the execution of pending orders. This depends on [symbol settings](../../Margin.md). Up to 3 checks can be performed in total:

  1. Check during an order placement. The margin is checked according to the [margin rates (#rate)](Retail-Forex-CFD-Futures-—-Netting.md#rate) specified for the symbol. If the margin rate is 0, the margin is not checked.
  2. Check during the pending order activation. If an order is activated by a trade server or a dealer (via the Manager terminal), sufficiency of funds for the deal to be performed according to that order is checked. Such check is not performed if the order is activated by the gateway when activation is actually tracked by the external trading system.
  3. Check after an order is confirmed by a dealer before that order is actually executed. The check is performed if [Additional margin check: check before executing orders](../../Margin.md) option is enabled in the trade symbol settings.



> Check rules:

The orders that have been place but have not yet been accepted for processing or have not yet been executed (in the "started" state) can only increase the margin but not decrease it. Example:

  * The client account has the following position: Sell 0.02 lot USDJPY. The current margin is 6.67 USD. Margin is calculated using the larger leg.
  * Case 1. The client places an order in the opposite direction: Buy 0.03 lot USDJPY. As long as the order is in the "started" state, the client's margin is still equal to 6.67 USD. As soon as the order is executed, the margin will be halved, i.e. 3.33 USD, since the uncovered volume will decrease from 0.02 to 0.01 lots.
  * Case 2. The client places an order in the same direction: Sell 0.03 lot USDJPY. The client's margin will increase immediately after placing the order, even while the order is in the "started" state. The margin value will become 16.67 USD, since the potential uncovered volume may become 0.05 lots.



This prevents clients from placing orders for a total volume larger than the funds allow.
