[🏠 Document Start](../../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../../../Platform-Setup.md) / [Symbols](../../../../Symbols.md) / [Symbol Settings](../../../Symbol-Settings.md) / [Trade](../../Trade.md) / [Margin Calculation](../Margin-Calculation.md) / Basic

[Previous](../Margin-Calculation.md) | [Next](Retail-Forex-CFD-Futures-—-Netting.md)

<a id="basic-margin-calculation"></a>
# Basic Margin Calculation (#basic-margin-calculation)

The trading platform provides several margin requirement calculation types depending on the financial instrument. You can select the calculation type in [Calculation (#calculation)](../../Trade.md#calculation) field of Trade tab. Margin calculation formula for each instrument depends on the [risk management formula (#risk)](../../../../Groups/Group-Settings.md#risk) used for the client group.

The basic calculation is only the first stage in the calculation of the final margin value. The value calculated by formulas is always converted to the deposit currency, after which the margin rate and other parameters are additionally applied. A detailed calculation scheme is provided in separate sections for each risk management system:

  * [Retail Forex, CFD, Futures — Netting](Retail-Forex-CFD-Futures-—-Netting.md)
  * [Retail Forex, CFD, Futures — Hedging](Retail-Forex-CFD-Futures-—-Hedging.md)
  * [Exchange Model](Stock-Exchange.md)



> If the [Initial Margin (#initial)](../../Margin.md#initial) parameter value is specified in symbol settings, this value will be used. The formulas described in this section will not be applied.

<a id="forex"></a>
## Forex (#forex)

The margin for Forex market symbols is calculated using the following equation:

All modes: Volume in lots * Contract size / Leverage

For example, let's calculate the margin requirements for buying one lot of EURUSD, while [the size of one contract (#contract-size)](../../Trade.md#contract-size) is 100,000 and the leverage is 1:100. After placing the appropriate values to the equation, we will obtain the following result:

1 * 100000 / 100 = EUR 1000

So, now we have the margin requirements value in [base currency (#base-currency)](../../Currency.md#base-currency) (or [margin currency (#margin-currency)](../../Currency.md#margin-currency)) of the symbol.

  * Generally, margin requirements currency and symbol's base currency are the same. If the margin currency is different, calculation results are displayed in that currency instead of the symbol's base one.
  * In this mode, a client leverage is taken into account even if a [fixed margin (#fixed)](Basic.md#fixed) is set.

  
---  
  
<a id="noleverage"></a>
## Forex No Leverage (#noleverage)

This type of calculation is also used for Forex symbols. But unlike the previous one, it does not take into account the client's leverage:

All modes: Volume in lots * Contract size

For example, let's calculate the margin requirements for buying one lot of EURUSD, while [the size of one contract (#contract-size)](../../Trade.md#contract-size) is 100,000 and the leverage is 1:100. After placing the appropriate values to the equation, we will obtain the following result:

1 * 100,000 = EUR 100,000

So, now we have the margin requirements value in base currency (or margin currency) of the symbol.

> Generally, margin requirements currency and symbol's base currency are the same. If the margin currency is different, calculation results are displayed in that currency instead of the symbol's base one.

<a id="cfd"></a>
## CFDs (#cfd)

The margin requirements for CFDs are calculated using the following equation:

All modes: Volume in lots * Contract size * Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell ones.

For example, let's calculate the margin requirements for buying one lot of oil, the size of the contract is 100 barrels, the current Ask price is USD 80. After placing the appropriate values to the equation, we will obtain the following result:

1 * 100 * 80 = USD 8,000

So, now we have the margin value in base currency (or margin currency) of the symbol.

<a id="cfd-leverage"></a>
## CFD Leverage (#cfd-leverage)

The leverage is also considered in this type of margin requirement calculation for CFDs:

All modes: Volume in lots * Contract size * Open market price / Leverage

<a id="cfd-index"></a>
## CFD Index (#cfd-index)

For index CFDs, the margin requirements are calculated according to the following equation:

All modes: Volume in lots * Contract size * Open market price * Tick value / Tick size

In addition to the usual calculation for CFDs, the formula takes into account the tick [value (#tick-price)](../../Trade.md#tick-price) to tick [size (#tick-size)](../../Trade.md#tick-size) ratio. 

<a id="futures"></a>
## Futures, Exchange Futures (#futures)

There are two types of the margin requirements for futures contracts:

  * Initial margin is the amount that must be available on the account at the moment of attempting to enter the market. Further maintenance of the same sum may not be obligatory.
  * Maintenance margin is the minimum amount that must be available on the account for holding a position open.



Both values are specified in [Margin](../../Margin.md) tab of the symbol settings. The final size of the margin depends on the volume:

Volume in lots * Initial margin

Volume in lots * Maintenance margin

The calculation is the same in all risk management modes.

> If the amount of the maintenance margin is not specified, the initial margin value will be used instead.

<a id="options"></a>
## Exchange Options (#options)

There are two types of margin requirements for futures contracts:

  * Initial margin is the amount that must be available on the account at the moment of attempting to enter the market. Further maintenance of the same amount may not be obligatory.
  * Maintenance margin is the minimum amount that must be available on the account for holding a position open.



Both values are specified in [Margin](../../Margin.md) tab of the symbol settings. The final size of the margin depends on the volume:

Volume in lots * Initial margin

Volume in lots * Maintenance margin

If the amount of the maintenance margin is not specified, the initial margin value will be used instead. If neither the initial nor the maintenance margin is specified, the appropriate value will be calculated according to the following formula:

Volume in lots * Contract size * Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell deals.

The same calculation method is applied for all risk management modes.

<a id="stocks"></a>
## Exchange Stocks, Exchange MOEX Stocks (#stocks)

The margin requirements for stocks are calculated using the following equation:

Retail Forex, CFD, Futures: Volume in lots * Contract size * Open market price

Retail Forex, CFD, Futures with hedged position: Volume in lots * Contract size * Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell ones.

For example, let's calculate the margin requirements for buying one lot of oil, the size of the contract is 100 barrels, the current Ask price is USD 80. After placing the appropriate values to the equation, we will obtain the following result:

1 * 100 * 80 = USD 8,000

So, now we have the margin value in base currency (or margin currency) of the symbol.

In the "Stock Exchange, based on margin discount rates" mode, margin for stocks is calculated as an indicative value, for assessing the trading account state relative to available positions. In this case, the margin amount is not blocked on the account and therefore does not reduce available funds. For details, please see the [appropriate section](Stock-Exchange.md).

> The only difference for the Exchange Stocks and Exchange MOEX Stocks modes is the [calculation of the adjusted initial margin (#corrected)](Stock-Exchange.md#corrected) when using the exchange model for risk management.

<a id="bonds"></a>
## Exchange Bonds, Exchange MOEX Bonds (#bonds)

The bond margin is calculated as part of the position value. Bond prices are provided as a face value percentage, so the position value is calculated as follows:

Retail Forex, CFD, Futures: Volume in lots * Contract size * Face value * Open price / 100

Retail Forex, CFD, Futures with hedged position: Volume in lots * Contract size * Face value * Open price / 100

The part of the position value to be reserved for maintenance is determined by [margin rates](../../Margin-Rates.md).

In the "Stock Exchange, based on margin discount rates" mode, bond margin is calculated as an indicative value, for assessing the trading account state relative to available positions. In this case, the margin amount is not blocked on the account and therefore does not reduce available funds. For details, please see the [appropriate section](Stock-Exchange.md).

  * The position value is calculated in the [symbol's base currency (#base-currency)](../../Currency.md#base-currency) (not in the profit currency).


  * The only difference for the Exchange Bonds and Exchange MOEX Bonds modes is the [calculation of the adjusted initial margin (#corrected)](Stock-Exchange.md#corrected) when using the exchange model for risk management.

  
---  
  
<a id="forts"></a>
## Exchange FORTS Futures (#forts)

The margin for the futures contracts of the Moscow Exchange derivative section is calculated separately for each symbol: First, the margin is calculated for the open position and all Buy orders. Then the margin for the same position and all Sell orders is calculated. The calculation is the same in all risk management modes.

MarginBuy = MarginPos + Sum(MarginBuyOrder)

MarginSell = MarginPos + Sum(MarginSellOrder))

The largest one of the calculated values is used as the final margin value for the symbol.

Thus, the same position is used in the calculation of both values. In the first formula (which includes Buy orders), the position margin is calculated as follows:

MarginPos = Volume * (InitialMarginBuy + (Open Price - SettlementPrice) * Tick Value / Tick Size * (1 + 0.01 * Margin Currency Rate))

The volume is used with a positive sign for long positions and with a negative sign for short positions.

In the second formula (which includes Sell orders), the position margin is calculated as follows:

MarginPos = Volume * (InitialMarginSell + (SettlementPrice - Open Price) * Tick Value / Tick Size * (1 + 0.01 * Margin Currency Rate))

The volume is used with a positive sign for short positions and with a negative sign for long positions.

This approach provides the trader a discount on margin, when there is an open position in the opposite direction with respect to the orders placed (the position acts as collateral for orders).

Margin on orders is calculated by the following formulas:

MarginBuyOrder = Volume * (InitialMarginBuy + (Price - SettlementPrice) * Tick value / Tick size * (1 + 0.01 * Margin currency rate))

MarginSellOrder = Volume * (InitialMarginSell + (SettlementPrice - Price) * Tick value / Tick size * (1 + 0.01 * Margin currency rate))

'Price' here depends on the order time and can be equal to:

  * The [Highest (#prices)](../../Trade.md#prices) and the [Lowest price (#prices)](../../Trade.md#prices) of the contract for the current session is used for not yet executed market or stop Buy and Sell orders, respectively. Since the price is not specified in market orders, the trader is charged the maximum possible margin. Once triggered, stop orders behave similar to market orders.
  * The order price is used for limit orders.
  * The Stop Limit price is used for stop limit orders.



Other parameters in the formulas:

  * InitialMarginBuy — the initial margin for the Buy operation.
  * InitialMarginSell — the initial margin for the Sell operation.
  * Currency margin rate is the rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble
  * SettlementPrice — [settlement price (#prices)](../../Trade.md#prices) of an instrument for the current session.



All these parameters for calculation are provided by the Moscow Exchange.

> InitialMarginBuy is written to the "Initial margin" field, InitialMarginSell is written to the "Maintenance Margin" field in [symbol properties](../../Margin.md).

Calculation example

The below example shows the calculation of margin requirements for the following trading account state:

  * Position Buy 3.00 Si-6.18 at 73640
  * Order Buy Limit 2.00 Si-6.18 at 73000
  * Order Sell Limit 10.00 Si-6.18 at 74500



Current session parameters

  * Clearing price = 73638
  * InitialMarginBuy = 7665.41
  * InitialMarginSell = 7739.59
  * Tick value = 1
  * Tick size = 1
  * Margin currency rate = 0



We substitute the values ​​in the formulas

MarginBuy = 3 * (7665.41 + (73640 - 73638) * 1/1) + 2 * (7665.41 + (73000-73638) * 1/1) = 37057.05

MarginSell = -3 * (7739.59 + (73638-73640) * 1/1) +10.0 * (7739.59 + (73638-74500) * 1/1) = 45563.13

Margin = Max(37057.05, 45563.13) = 45563.13

The resulting margin for the Si-6.18 symbol is 45563.13.

> The Exchange FORTS Futures mode must only be used together with the [MOEX Derivatives Gateway](../../../../../Platform-Components/Gateways/MOEX-Derivatives.md). Otherwise the margin requirements calculation results may be unpredictable.

<a id="collateral"></a>
## Collateral (#collateral)

Non-tradable instruments of this type are used as trader's assets to provide the [required margin for open positions (#collateral)](../../../../Accounts/Editing-Account.md#collateral) of other instruments. For these instruments the margin is not calculated.

<a id="fixed"></a>
## Fixed Margin (#fixed)

If a non-zero value is specified in the ["Initial margin" (#initial)](../../Margin.md#initial) field, then no calculations by formulas specified in the "Calculation" field are performed (except for the calculation of [futures](Retail-Forex-CFD-Futures-—-Netting.md), which is not affected). In this case, for all types of calculations (except for Forex and CFD Leverage), the margin is obtained as if "Futures" option is selected:

Volume in lots * Initial margin

Volume in lots * Maintenance margin

For Forex and CFD Leverage calculation types, the leverage is additionally considered:

Volume in lots * Initial margin / Leverage

Volume in lots * Maintenance margin / Leverage

The calculation is the same in all risk management modes.

> If the amount of the maintenance margin is not specified, the initial margin value will be used instead.

<a id="recalculate-margin"></a>
## End-of-day margin conversion rate recalculation (#recalculate-margin)

This option assists brokers in meeting regulatory requirements (in particular, NFA requirements), which limit the maximum allowed leverage for different symbol types.

In currency pair trading, the margin determined in the symbol's base currency is converted into the account deposit currency. For example, when trading EURUSD with a contract size of 100,000 and a leverage of 1:100, the margin will be EUR 1,000 per lot. If the trader's deposit currency is USD, the margin will be converted from EUR to USD at the current rate. The conversion rate is registered in the position's [Margin rate (#margin-rate)](../../../../Positions.md#margin-rate) field.

The EURUSD exchange rate will change over time, and the USD equivalent of EUR 1,000 will change accordingly. Thus, the trader's actual leverage may become greater or less than the original one.

To prevent this from happening, the trading platform provides a mechanism for updating margin conversions. It is activated by the "Recalculate margin exchange rate at the end of day" option in [common symbol settings (#recalculate-margin)](../../Margin.md#recalculate-margin) or in [group-specific symbol settings (#recalculate-margin)](../../../../Groups/Group-Symbol-Settings/Margin.md#recalculate-margin).

![End-of-day margin conversion rate recalculation](images/margin_rate_recalculation.png)

At the [end of the trading day (#end-of-day)](../../../../Network-cluster/Configuring-Servers/Trade-Server.md#end-of-day), the server will update the "Margin rate" field in all positions for the instruments with the recalculation enabled. The new value will be calculated using the current market prices for the relevant client groups (similar procedures performed during trade execution).

Please note the following features:

  * The margin rate is not recalculated on the days marked as non-working in the platform (according to the [Time section settings](../../../../Time.md))
  * The margin rate is recalculated after swaps calculations (if no swaps are charged, the rate is recalculated too)
  * If the required price is not available (zero) at the time of recalculation, no recalculation is performed



The recalculation process can be tracked in the trade server log. It will show the following records:

margin rates update started   
...   
margin rates update finished   
---  
  
The recalculation is carried out only when a symbol margin currency is different from the account deposit currency. If the margin currency and the deposit currency are the same, then no recalculation is actually carried out. However, a record on updating the margin ratio value is still sent to the server journal. In this case, it will always be equal to 1.00000. For example:

margin rates for 'EURUSD' positions updated - buy: 1.00000000, sell: 1.00000000  
---
