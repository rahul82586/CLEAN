[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Daily Dealing

[Previous](Daily-Server-Logs.md) | [Next](Daily-Trades.md)

# Daily Dealing Report

Daily Dealing Report is a daily report on dealing activity. The report contains three tables.

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting the report:

  * Period — a day, for which the report must be generated.



## Configuration in MetaTrader 5 Administrator

Additional parameters are specified in the report configuration of MetaTrader 5 Administrator:

  * Currency — the currencies used for displaying dealer's profit in the report;
  * Groups — the groups, for which the report is generated. "*" mask and "!" negation symbol can be used to specify the groups. *,!demo*,!contest* value is assigned to this parameter by default. It means that a report is prepared for all groups except those that begin with "demo" and "contest" words.
  * Dangerous Tick Deviation — the value of a deviation (in pips in either direction) of a price thrown in by a dealer from the current price, above which the throw is deemed to be dangerous. Dangerous Ticks Thrown in by Dealers table is built based on that parameter.
  * Dangerous Profit — the value of the profit (definite currency is specified in Currency field) obtained by a dealer/client after the prices have been thrown in by the dealer, above which the dealer's actions are deemed to be dangerous. Dangerous Actions of Dealers table is built based on that parameter.
  * Max Dangerous Actions Shown — the maximum number of entries displayed in Dangerous Actions of Dealers table. 



## Managers

This table shows the list of managers who have connected the server during a day.

  * Login — manager's account number;
  * Name — manager's name;
  * Connections — number of connections to the server per day;
  * Requests — number of requests received by a dealer per day;
  * Requoted — amount of new prices sent by the dealer in response to a request (requote);
  * Rejected — number of requests rejected by the manager per day;
  * Dealer profit, currency — profit earned by the manager in a specified currency;
  * Dealer profit, pips — profit earned by the manager in pips.



## Dangerous Actions of Dealers

The following table contains the list of suspicious deals confirmed by dealers:

  * Manager — dealer's account number;
  * Name — dealer's name;
  * Dealer profit, currency — profit earned by the dealer in a specified currency;
  * Dealer profit, pips — profit earned by the dealer in pips;
  * Details — server log entry describing dealer's actions.



## Dangerous Ticks Thrown in by Dealers

The following table contains the list of suspicious quotes thrown in by dealers:

  * Manager — dealer's account number;
  * Name — dealer's name;
  * Symbol — the symbol, for which a quote has been thrown in;
  * Bid deviation, Pips — deviation of the thrown in quote Bid price from the market Bid price that was actual during the throw;
  * Ask deviation, Pips — deviation of the thrown in quote Ask price from the market Ask price that was actual during the throw.


