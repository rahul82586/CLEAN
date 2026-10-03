[🏠 Document Start](../../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../../../Platform-Setup.md) / [Symbols](../../../../Symbols.md) / [Symbol Settings](../../../Symbol-Settings.md) / [Trade](../../Trade.md) / [Margin Calculation](../Margin-Calculation.md) / Retail Forex, CFD, Futures — Netting

[Previous](Basic.md) | [Next](Retail-Forex-CFD-Futures-—-Hedging.md)

<a id="retail-forex-cfd-futures-netting"></a>
# Retail Forex, CFD, Futures — Netting (#retail-forex-cfd-futures-netting)

This margin calculation model is used for Retail Forex, CFD and Futures with the [netting position accounting system (#netting)](../../../../Groups/Position-Accounting-Systems.md#netting). Unlike to the same model for hedging accounts, [spreads (#spread)](Retail-Forex-CFD-Futures-—-Netting.md#spread) are additionally taken into account in this calculation method.

The first stage in margin calculation is defining if an account has positions or pending orders for the symbol the deal is performed for.

  * If that account has no positions and orders for the symbol, the margin is calculated using the [formulas](Basic.md).
  * If the account has an open position, and a new order of any type with the volume being less or equal to the current position is placed in the opposite direction, the total margin is equal to the current position's one. Example: we have a 1 lot EURUSD Buy position and place an order to Sell 1 lot EURUSD (similarly for Sell Limit, Sell Stop and Sell Stop Limit).
  * If the account has an open position and an order of any type is placed in the same direction, the total margin is equal to the sum of the current position's and placed order's margins.
  * If the account has an open position, and an order of any type with the volume exceeding the current position is placed in the opposite direction, two margin values are calculated - for the current position and for the placed order. The final margin is taken according to the highest of the two calculated values.
  * If the account has two or more oppositely directed market and limit orders, the margin is calculated for each direction (Buy and Sell). The final margin is taken according to the highest of the two calculated values. For all other order types (Stop and Stop Limit), the margin is summed up (charged for each order).



The margin amount is calculated in several stages:

  * Basic calculation for a certain symbol
  * [Conversion of margin currency into deposit currency (#conversion)](Retail-Forex-CFD-Futures-—-Netting.md#conversion)
  * [Multiplication by rate (#rate)](Retail-Forex-CFD-Futures-—-Netting.md#rate)
  * [Calculations for trading symbols in spread (#spread)](Retail-Forex-CFD-Futures-—-Netting.md#spread)



<a id="main"></a>
## Basic Calculation for a Symbol (#main)

[The basic margin value](Basic.md) in accordance with the symbol type is calculated first. The type is defined by symbol settings in the [Calculation (#calculation)](../../Trade.md#calculation) field.

<a id="conversion"></a>
## Converting into Deposit Currency (#conversion)

This stage is common for all calculation types. Conversion of margin requirements calculated using one of the methods mentioned above is performed in case their currency is different from the [account deposit (#currency)](../../../../Groups/Group-Settings.md#currency) currency.

The current exchange rate of margin currency to deposit currency is used for conversion. The Ask price is used for buy deals, and the Bid price is used for sell deals.

Suppose that the basic size of the margin previously calculated for buying one lot of EURUSD is 1000 EUR. If the account deposit currency is USD, the current Ask price of EURUSD pair is used for conversion. For example, if the current rate is 1.2790, the total margin size is 1279 USD.

The margin to deposit currency conversion rate is shown in the "Margin rate" field in [orders](../../../../Orders.md) and [positions](../../../../Positions.md).

For details, please visit the [Conversion](../Conversion.md) section.

<a id="rate"></a>
## Margin rate (#rate)

You can specify in symbol settings additional multipliers (rates) for the margin requirements depending on the position/order type. This can be done in the [Margin rates](../../Margin-Rates.md) tab. The final size of the margin requirements previously calculated regarding conversion into the deposit currency is additionally multiplied by the appropriate rate. In addition, you can completely disable margin charging for any desired types of trading operations. To do this, set the zero margin ratio.

For example, the previously calculated margin for buying one lot of EURUSD is 1279 USD. This sum is additionally multiplied by long margin rate. For example, if it is equal to 1.15, the final margin is 1279 * 1.15 = 1470.85 USD.

<a id="spread"></a>
## Calculations for Spread Trading (#spread)

The margin can be charged on preferential basis in case trading positions are in spread relative to each other. The spread is defined as the presence of the oppositely directed positions at related symbols. Reduced margin requirements provide traders with more trading opportunities. Configuration of spreads is described in a [separate section](../../../../Spreads.md).

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

  * The client account has the following position: Sell 0.02 lot USDJPY. The current margin is 6.67 USD.
  * Case 1. The client places an order in the opposite direction: Buy 0.03 lot USDJPY. As long as the order is in the "started" state, the client's margin is still equal to 6.67 USD. As soon as the order is executed, the margin will be halved, i.e. 3.33 USD, since the position volume will decrease from 0.02 to 0.01 lots.
  * Case 2. The client places an order in the same direction: Sell 0.03 lot USDJPY. The client's margin will increase immediately after placing the order, even while the order is in the "started" state. The margin value will become 16.67 USD, since the potential total volume may become 0.05 lots.



This prevents clients from placing orders for a total volume larger than the funds allow.
