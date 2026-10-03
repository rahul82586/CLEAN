[🏠 Document Start](../README.md) / [Server Reports](README.md) / Gateways Profit

[Previous](Gateways-Turnover.md) | [Next](Gateways-White-Label.md)

# Gateways Profit Report

Gateways Profit Report is a report on the volume of trades processed by gateways, as well as the profit obtained by a broker while processing these trades.

## Configuration in MetaTrader 5 Manager

Set start and end dates of the period, for which the report will be generated, in the Period field.

## Configuration in MetaTrader 5 Administrator

An additional parameter can be configured in the report configuration in MetaTrader 5 Administrator. It is a currency, in which the trading volume and profit are displayed.

## Report data

The following data on each gateway is displayed:

  * Symbol — symbol, for which turnover and profit are displayed.
  * Deals — number of deals processed by a gateway for this symbol.
  * Lots — deals volume (in lots) processed by a gateway for this symbol.
  * Amount — volume of the deals (in base currency) processed by a gateway for this symbol. Calculation is performed according to the equations:


  * for Forex calculation type = Volume (in lots) * Contract size
  * for Futures, Exchange Futures and FORTS Futures calculation types = [Price * Volume (in lots) * Tick price] / Tick size
  * for CFD, CFD Index, CFD Leverage and Exchange Stocks calculation types = Price * Volume (in lots) * Contract Size;
  * Currency — symbol base currency;
  * Amount Rate — conversion rate of a base currency to the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).
  * Amount, currency — deals volume in the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).
  * Profit, pips — broker's profit in pips. Calculated by the following equations:


  * for BUY deal = Deal price - gateway price
  * for SELL deal = Gateway price - deal price
  * Profit — broker's profit in symbol profit currency. Calculated by the following equations:



> symbols with Forex, CFD, CFD Index, CFD Leverage or Exchange Stocks calculation types:

  * Currency — symbol profit currency.
  * Profit Rate — conversion rate of a profit currency to the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).
  * Profit, currency — broker's profit in the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).



  * Volume in the parameters display currency (Amount, currency) is calculated considering exchange rates as of the moment of a report generation and does not reflect an accurate volume at the time of actual deals.
  * Profit in the parameters display currency (Profit, currency) is calculated considering exchange rates as of the moment of a report generation and does not reflect accurate profit at the time of actual deals. Besides, actual conversion rates from an exchange side may differ from trading server ones. Therefore, an exact profit earned by a broker is displayed only in Profit, pips and Profit columns.

  
---  
  
Total parameters for all gateways are displayed at the bottom of the report.
