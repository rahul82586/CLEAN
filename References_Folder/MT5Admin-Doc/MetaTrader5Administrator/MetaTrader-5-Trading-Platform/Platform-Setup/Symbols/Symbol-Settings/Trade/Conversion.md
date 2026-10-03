[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../../Platform-Setup.md) / [Symbols](../../../Symbols.md) / [Symbol Settings](../../Symbol-Settings.md) / [Trade](../Trade.md) / Conversion

[Previous](Profit-Calculation.md) | [Next](../Futures.md)

# Conversion

The calculated value of the [margin](Margin-Calculation.md) or [profit](Profit-Calculation.md) (loss) is always converted to the [account deposit currency (#currency)](../../../Groups/Group-Settings.md#currency). Conversion is based on the following principles:

Forex and Forex No Leverage instruments | Other instruments  
---|---  
  
  * Profit/loss conversion rate depends on whether the position is profitable or not.
  * During the profit conversion, a trader sells the profit currency for the deposit currency (at Bid price). During the loss conversion, a trader should buy the loss currency for the deposit currency (at Ask price). The worst price is always used during the conversion.
  * To perform conversion, the system searches for a Forex symbol (symbol with the [Forex/Forex No leverage calculation type (#calculation)](../Trade.md#calculation)) with the base and quoted currency coinciding with the profit (margin) and deposit currency. For example, USDCHF symbol is used to convert USD to CHF.
  * If there is no such a symbol, the attempt is made to convert via USD. Suppose that the profit currency is XYZ, while the deposit one is ABC. If the server has no XYZABC or ABCXYZ symbol, two symbols (XYZUSD and ABCUSD) are used for conversion. Thus, the conversion is performed in two stages. The worst rate for a client is used at each stage (Bid or Ask price).


  * If a postfix is used in the name of the trading symbol participating in the deal (for example, EURUSDx), the server will try to use currency pairs with the same postfix during direct conversion and conversion via USD.


  1. The server tries to find the conversion rate with the postfix matching the postfix of the original trading instrument. Symbol visibility for the client group is taken into account. If the instrument is found and its prices are available, this instrument will be used. For example, to convert GBPCHF.xyz profit to USD, the server will try to use GBPUSD.xyz and USDCHF.xyz.
  2. Otherwise, the server will search for currency pairs among those available to the client group in accordance with its [settings (#symbols)](../../../Groups/Group-Settings.md#symbols). The presence of a postfix in the instrument name is ignored. For example, to convert USD to CHF the system can use either USDCHF or USDCHFx.
  3. If several symbols suitable for conversion are available to a client group, the one, which is earlier alphabetically, will be used. For example, among "GBPUSD.xyz, GBPUSD.abc, GBPUSD" GBPUSD will be selected; GBPUSD.abc will be selected among "GBPUSD.xyz, GBPUSD.abc".
  4. If no suitable instrument is found among the symbols available to the client group, the system will continue search among all the symbols in the platform. If several suitable symbols are found, the alphabetically earlier symbol will be used. Please note that in this case conversion will only be performed on the platform side, while in terminal the floating profit and margin will have zero values. The appropriate values are calculated by terminals using incoming quotes. Accordingly, if the required instruments are not available to the terminals, they will not be able to calculate profit and margin.

| 

  * Profit/loss conversion rate depends on whether the position is profitable or not.
  * During the profit conversion, a trader sells the profit currency for the deposit currency (at Bid price). During the loss conversion, a trader should buy the loss currency for the deposit currency (at Ask price). The worst price is always used during the conversion.
  * To perform conversion, the system searches for a Forex symbol (symbol with the [Forex/Forex No leverage calculation type (#calculation)](../Trade.md#calculation)) with the base and quoted currency coinciding with the profit (margin) and deposit currency. For example, USDCHF symbol is used to convert USD to CHF. The following search orders is applied when selecting an appropriate symbol:


  1. A symbol is searched among all the symbols available to a client group in accordance with the [group settings (#symbols)](../../../Groups/Group-Settings.md#symbols). The presence of a postfix in the instrument name is ignored. For example, to convert USD to CHF the system can use either USDCHF or USDCHFx.
  2. If several symbols suitable for conversion are available to a client group, the one, which is earlier alphabetically, will be used. For example, among "GBPUSD.xyz, GBPUSD.abc, GBPUSD" GBPUSD will be selected; GBPUSD.abc will be selected among "GBPUSD.xyz, GBPUSD.abc".
  3. If no suitable instrument is found among the symbols available to the client group, the system will continue search among all the symbols in the platform. If several suitable symbols are found, the alphabetically earlier symbol will be used. Please note that in this case conversion will only be performed on the platform side, while in terminal the floating profit and margin will have zero values. The appropriate values are calculated by terminals using incoming quotes. Accordingly, if the required instruments are not available to the terminals, they will not be able to calculate profit and margin.


  * If there is no such a symbol, the attempt is made to convert via USD. Suppose that the profit currency is XYZ, while the deposit one is ABC. If the server has no XYZABC or ABCXYZ symbol, two symbols (XYZUSD and ABCUSD) are used for conversion. Thus, the conversion is performed in two stages. The worst rate for a client is used at each stage (Bid or Ask price).

  
  
The above principles are applied both when converting the profit and when converting the margin. The features of each case are described below:

  * Profit conversion: select the profit calculation mode for Forex type symbols: [by deal or by market (#conversion)](Profit-Calculation.md#conversion).
  * Margin conversion: if the deal's currency pair is used to convert the margin currency to the deposit one, the deal execution price is always used to calculate the margin. For example, in case of EURUSD deal and USD deposit currency, conversion is conducted at EURUSD price, at which the deal is performed.



  * The floating profit and margin values on the terminal side are calculated using incoming quotes. To ensure the correct display of these variable, the currency pairs that are used for the conversion should be available to the group of the account, for which the calculation is being performed.
  * Additionally, to be able to view profit on a client account via a Manager or Administrator terminal, the manager account must also have access to the currency pairs used for conversion (they must be available for the manager group).

  
---
