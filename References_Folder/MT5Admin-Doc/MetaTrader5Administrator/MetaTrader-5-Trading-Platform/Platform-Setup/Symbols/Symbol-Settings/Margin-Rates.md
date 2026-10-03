[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../Platform-Setup.md) / [Symbols](../../Symbols.md) / [Symbol Settings](../Symbol-Settings.md) / Margin Rates

[Previous](Margin.md) | [Next](Swaps.md)

# Margin Rates

![Margin rates](images/symbols_margin_rates.png)

This section contains margin rates for various order types. The rates are set for the initial and maintenance margin individually. If there is no rate for the maintenance margin (equal to zero), the initial margin value is used instead.

  * Market buy order — multiplier for calculating margin requirements for long positions relative to the [main amount of margin](Trade/Margin-Calculation.md);
  * Market sell order — multiplier for calculating margin requirements for short positions relative to the main amount of margin;
  * Buy limit order — multiplier for calculating margin requirements for Buy Limit orders relative to the main amount of margin;
  * Sell limit order — multiplier for calculating margin requirements for Sell Limit orders relative to the main amount of margin;
  * Buy stop order — multiplier for calculating margin requirements for Buy Stop orders relative to the main amount of margin;
  * Sell stop order — multiplier for calculating margin requirements for Sell Stop orders relative to the main amount of margin;
  * Buy stop limit order — multiplier for calculating margin requirements for Buy Stop Limit orders relative to the main amount of margin;
  * Sell stop limit order — multiplier for calculating margin requirements for Sell Stop Limit orders relative to the main amount of margin.



Liquidity margin rate — in the [exchange risk management model (#assets)](Trade/Margin-Calculation/Stock-Exchange.md#assets), clients can use their own assets as collateral for open positions. The liquidity margin rate determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity). If the value is set to 0, the instrument cannot be used as collateral.

Currency margin rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures (#forts)](Trade/Margin-Calculation/Basic.md#forts)) traded on Moscow Exchange ([calculating variation margin and security deposit using the current USD exchange rate](https://fs.rts.micex.ru/files/644 "Variation margin and security deposit calculation using the current US Dollar exchange rate") \- in Russian). The values are sent by the Moscow Exchange when using the gateway [MetaTrader 5 to MOEX Derivatives](../../../Platform-Components/Gateways/MOEX-Derivatives.md).

> If the [exchange risk management model (#margin)](../../Groups/Group-Settings.md#margin) is used for the client group, and a symbol has 0 margin rates, then the margin is not charged for operations by that symbol.

The margin calculation is described in details in a [separate section](Trade/Margin-Calculation.md).
