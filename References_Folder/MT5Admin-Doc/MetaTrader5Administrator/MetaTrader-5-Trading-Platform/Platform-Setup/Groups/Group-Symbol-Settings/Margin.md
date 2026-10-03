[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../Platform-Setup.md) / [Groups](../../Groups.md) / [Group Symbol Settings](../Group-Symbol-Settings.md) / Margin

[Previous](Execution.md) | [Next](Margin-Rates.md)

# Margin

![Margin](images/groups_symbols_settings_margin.png)

This tab allows setting up margin parameters for a group by the symbol (group of symbols) specified on the "Common" tab.

  * Use default margin values/settings — use margin parameters specified for the symbol in the [corresponding section](../../Symbols/Symbol-Settings/Margin.md).
  * Initial margin — amount of money ([margin (#futures)](../../Symbols/Symbol-Settings/Trade/Margin-Calculation/Basic.md#futures)) deposited for futures contracts to ensure performance of the contract to execute a deal with the volume of 1 lot;
  * Maintenance margin — the minimal amount of money ([margin (#futures)](../../Symbols/Symbol-Settings/Trade/Margin-Calculation/Basic.md#futures)) that must be available on a client's account to support a position with the volume of 1 lot;
  * Hedged margin — the amount of margin charged per each hedged lot of a position. If initial margin is set for an instrument, the hedged margin is specified as an absolute value (in margin currency) terms. If the initial margin is not set (equal to 0), the contract size is specified. The margin is calculated by the appropriate formula corresponding to the type of the instrument and using the specified contract size. For more details please see the [special section (#hedged)](../../Symbols/Symbol-Settings/Trade/Margin-Calculation/Retail-Forex-CFD-Futures-—-Hedging.md#hedged).
  * Calculate hedged margin using larger leg — determines the [hedged margin calculation mode (#hedged)](../../Symbols/Symbol-Settings/Trade/Margin-Calculation/Retail-Forex-CFD-Futures-—-Hedging.md#hedged): basic or using larger position leg.
  * Exclude long position PnL from free margin and margin level — the option affects the display of positions purchased with own funds, on accounts with margin trading enabled. If the option is enabled, profit/loss of positions for the symbol will be ignored when calculating free margin, margin level and account equity. Also, [Stop Out (#stopout)](../Group-Settings.md#stopout) will not be applies to such positions.
  * Recalculate margin exchange rate at the End of Day — if this option is enabled, at the end of the trading day, the server will update the position margin conversion rate at current market prices. For further details, please see [Basic Margin Calculation (#recalculate-margin)](../../Symbols/Symbol-Settings/Trade/Margin-Calculation/Basic.md#recalculate-margin).
  * Additional margin check — on default, the margin is checked when any order is placed and when a pending orders triggers. This parameter allows enabling additional margin checks:


  * check before executing orders — in this mode, another check of margin is added to those described above: the margin is checked before executing an order after it is confirmed (checked) by the server (at automated execution), by a dealer or by a gateway.
  * check on SL-TP trigger — enables an additional check of margin before a position is closed by stop loss or take profit. If the position close results in reducing the margin to a level insufficient to maintain open positions and orders, the stop loss/take profit will not trigger, the position will stay open. This check must be enabled in case the trade operations are transmitted to an external system (exchange).



  * If the initial margin is specified, then no calculations by formulas specified in the ["Calculation" (#calculation)](../../Symbols/Symbol-Settings/Trade.md#calculation) field are performed.
  * If the maintenance margin value is not specified, the value of the initial margin is used for it.


  * If the [exchange risk management model (#margin)](../Group-Settings.md#margin) is used for the client group, and a symbol has 0 margin rates, then the margin is not charged for operations by that symbol.

  
---  
  
The margin calculation is described in details in a [separate section](../../Symbols/Symbol-Settings/Trade/Margin-Calculation.md).
