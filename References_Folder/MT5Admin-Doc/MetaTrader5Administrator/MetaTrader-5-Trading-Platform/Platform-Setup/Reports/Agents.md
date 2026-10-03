[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Agents

[Previous](Accounts-Lifetime-by-Countries.md) | [Next](Agents-Detailed.md)

# Agents Report

Agents Report is a report on all transactions connected with charging agent commissions.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — groups containing the accounts, on which the report will be created;
  * Period — starting and ending date of the period, the deals for which will be requested.



The following data on agent commissions charging deals is provided:

  * Deal — commission charging deal ticket;
  * Login — number of the account charged by the commission;
  * Name — account holder name;


  * Group — group the account belongs to;
  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Time — commission charging time;
  * Type — deal type;
  * Comment — comments on the deal. The comments contain the number of the account, from which an agent receives commission when performing deals on it;
  * Profit — commission size;
  * Currency — commission currency.


