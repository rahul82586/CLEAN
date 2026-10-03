[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Gateways Turnover

[Previous](Summary.md) | [Next](Gateways-Profit.md)

# Gateways Turnover Report

Gateways Turnover Report is a report on volumes of the deals handled by gateways.

## Setup in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting the report:

  * Period — starting and ending date of the period, for which the report will be generated.



## Setup in MetaTrader 5 Administrator

  * Currency — currency used for displaying deals volumes processed by a gateway.



The following data on each gateway is displayed in the report:

  * Symbol — symbol, for which turnover is displayed;
  * Deals — number of deals processed by a gateway for this symbol;
  * Lots — deals volume (in lots) processed by a gateway for this symbol;
  * Amount — volume of the deals (in base currency) processed by a gateway for this symbol. Calculation is performed according to the equations:


  * for "Forex" calculation type = Volume (in lots) * Contract Size
  * for "Futures", "Exchange Futures", "FORTS Futures" calculation types = [Price * Volume (in lots) * Tick value] / Tick size
  * for "CFD", "CFD Index", "CFD Leverage" and "Exchange Stocks" calculation types = Price * Volume (in lots) * Contract Size;
  * Currency — symbol base currency;
  * Amount Rate — conversion rate of a base currency to the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator);
  * Amount, currency — deals volume in the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).



> Volume in the parameters display currency (Amount, currency) is calculated considering exchange rates as of the moment of a report generation and does not reflect an accurate volume at the time of actual deals.
