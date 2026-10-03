[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Gateways Profit

[Previous](Gateways-Turnover.md) | [Next](Gateways-White-Label.md)

# Gateways Profit Report

Gateways Profit Report is a report on volumes of the deals handled by gateways, as well as the profit earned by a broker when handling these deals.

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting the report:

  * Period — starting and ending date of the period, for which the report will be generated.



## Configuration in MetaTrader 5 Administrator

  * Currency — currency used for displaying deals volumes and profit.



The following data on each gateway is displayed in the report:

  * Symbol — symbol, for which turnover and profit are displayed;
  * Deals — number of deals processed by a gateway for this symbol;
  * Lots — deals volume (in lots) processed by a gateway for this symbol;
  * Amount — volume of the deals (in base currency) processed by a gateway for this symbol. Calculation is performed according to the equations:


  * for "Forex" calculation type = Volume (in lots) * Contract Size
  * for "Futures", "Exchange Futures", "FORTS Futures" calculation types = [Price * Volume (in lots) * Tick price] / Tick size
  * for "CFD", "CFD Index", "CFD Leverage" and "Exchange Stocks" calculation types = Price * Volume (in lots) * Contract Size;
  * Currency — symbol base currency;
  * Amount Rate — conversion rate of a base currency to the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator);
  * Amount, currency — deals volume in the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator);
  * Profit, pips — broker's profit in pips. Calculated by the following equations:


  * for BUY deal = Deal price - gateway price
  * for SELL deal = Gateway price - deal price
  * Profit — broker's profit in symbol profit currency. Calculated by the following equations:



> symbols with "Forex", "CFD", "CFD Index", "CFD Leverage" or "Exchange Stocks" calculation types:

  * Currency — symbol profit currency;
  * Profit Rate — conversion rate of a profit currency to the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator);
  * Profit, currency — broker's profit in the currency used for parameters display (specified in report settings in MetaTrader 5 Administrator).



  * Volume in the parameters display currency (Amount, currency) is calculated considering exchange rates as of the moment of a report generation and does not reflect an accurate volume at the time of actual deals.
  * Profit in the parameters display currency (Profit, currency) is calculated considering exchange rates as of the moment of a report generation and does not reflect accurate profit at the time of actual deals. Besides, actual conversion rates from an exchange side may differ from trading server ones. Therefore, an exact profit earned by a broker is displayed only in Profit, pips and Profit columns.

  
---  
  
Total parameters for all gateways are displayed at the bottom of the report.
