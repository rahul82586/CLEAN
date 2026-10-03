[🏠 Document Start](../README.md) / [Server Reports](README.md) / Gateways White Label

[Previous](Gateways-Profit.md) | [Next](Execution-Type.md)

# Gateways White Label Report

Gateways White Label Report is a report on volumes of deals performed on a trading server by external brokers via MetaTrader 5 Gateway (standard or White Label version).

The algorithm of working with MetaTrader 5 Gateway can be presented the following way: an account for an external brokerage company is opened on a trading server. The company can use this account for performing trade operations. The external brokerage company configures MetaTrader 5 Gateways for connecting to the trading server.

This report allows to view the volume of deals performed by external brokers on a trading server.

## Configuration in MetaTrader 5 Manager

Set start and end dates of the period, for which the report will be generated, in the Period field.

## Configuration in MetaTrader 5 Administrator

An additional parameter can be configured in the report configuration in MetaTrader 5 Administrator: This is a currency, in which the trading volume and profit are displayed.

## Report data

The report is generated on each account, transactions on which are handled via MetaTrader 5 Gateway. The following account data is displayed:

  * Symbol — symbol, for which trading operations data is displayed.
  * Deals — number of deals for this symbol.
  * Lots — deals volume (in lots) for this symbol.
  * Amount — volume of the deals (in base currency) for this symbol. Calculated by the following equations:


  * for Forex calculation type = Volume (in lots) * Contract Size
  * for Futures, Exchange Futures and FORTS Futures calculation types = [Price * Volume (in lots) * Tick price] / Tick size
  * for CFD, CFD Index, CFD Leverage and Exchange Stocks calculation types = Price * Volume (in lots) * Contract Size
  * Currency — symbol base currency.
  * Amount Rate — conversion rate of a base currency to the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).
  * Amount, currency — deals volume in the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).



> Volume in the parameters display currency (Amount, currency) is calculated considering exchange rates as of the moment of a report generation and does not reflect an accurate volume at the time of actual deals.

Total data for all accounts using MetaTrader 5 Gateway for performing transactions are displayed at the bottom of the report.
