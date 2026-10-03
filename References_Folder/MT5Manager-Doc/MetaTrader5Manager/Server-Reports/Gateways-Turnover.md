[🏠 Document Start](../README.md) / [Server Reports](README.md) / Gateways Turnover

[Previous](Summary.md) | [Next](Gateways-Profit.md)

# Gateways Turnover Report

Gateways Turnover Report is a report on volumes of the deals processed by gateways.

## Configuration in MetaTrader 5 Manager

Set start and end dates of the period, for which the report will be generated, in the Period field.

## Configuration in MetaTrader 5 Administrator

An additional parameter can be configured in the report configuration in MetaTrader 5 Administrator. It is a currency used for displaying deals volumes processed by a gateway.

## Report data

The following data on each gateway is displayed:

  * Symbol — symbol, for which turnover is displayed;
  * Deals — number of deals processed by a gateway for this symbol;
  * Lots — deals volume (in lots) processed by a gateway for this symbol;
  * Amount — volume of the deals (in base currency) processed by a gateway for this symbol. Calculation is performed according to the equations:


  * for Forex calculation type = Volume (in lots) * Contract Size
  * for Futures, Exchange Futures and FORTS Futures calculation types = [Price * Volume (in lots) * Tick price] / Tick size
  * for CFD, CFD Index, CFD Leverage and Exchange Stocks calculation types = Price * Volume (in lots) * Contract Size;
  * Currency — symbol base currency;
  * Amount Rate — conversion rate of a base currency to the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).
  * Amount, currency — deals volume in the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).



> Volume in the parameters display currency (Amount, currency) is calculated considering exchange rates as of the moment of a report generation and does not reflect an accurate volume at the time of actual deals.
