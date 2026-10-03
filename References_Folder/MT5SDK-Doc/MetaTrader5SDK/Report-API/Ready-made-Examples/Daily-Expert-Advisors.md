[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Ready-made Examples](../Ready-made-Examples.md) / Daily Expert Advisors

[Previous](Daily-Positions.md) | [Next](Deals-History.md)

# Daily Expert Report

Daily Expert Report is a report on trading operations performed by clients' Expert Advisors. The report is generated for seven days.

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report will be created;
  * Period — reports are generated for seven days preceding the specified day.



## Configuration in MetaTrader 5 Administrator

Additional parameters are specified in the report configuration of MetaTrader 5 Administrator:

  * Group — a group or several groups (separated by commas) having the accounts used for reports generation. "*" mask and "!" negation symbol can be used when specifying the groups. For example, if *,!demo*,!contest* are specified, the groups with the names beginning from demo and contest symbols will not be considered in generated reports.
  * Currency — the currency used when displaying various parameters in the report (Balance, Profit, etc.).



## Diagrams

The report contains several diagrams:

  * Deals of Clients — total number of deals performed by clients, as well as the number of deals performed by Expert Advisors.
  * Orders of Clients — total number of orders placed by clients, as well as the number of orders placed by Expert Advisors.
  * Profit and Loss of Clients — total profit (Profit)/loss (Loss) gained by clients, as well as profit/loss obtained by Expert Advisors.



## Tables

The report contains the following tables:

### Users with the highest number of deals performed by Expert Advisors

The report contains 10 users having the highest number of deals performed by their Expert Advisors for a specified day. The table displays only profitable accounts (for a specified day).

The following data is displayed in the table:

  * Login — account number;
  * Name — account holder name;


  * Group — group the account belongs to;


  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Balance, currency — account balance at the time of the report request;
  * Floating P/L, currency — floating profit/loss on the account at the time of the report request;
  * Experts profit, currency — profit made by an Expert Advisor for a specified day in a specified currency;
  * Total profit, currency — total profit/loss for a specified day in a specified currency;
  * Experts deals — number of deals performed by Expert Advisors for a specified day;
  * Total deals — total number of deals performed by a user for a specified day.



### Users with the highest number of orders placed by Expert Advisors

The report contains 10 users having the highest number of orders placed by their Expert Advisors for a specified day. The table displays only profitable accounts (for a specified day).

The following data is displayed in the table:

  * Login — account number;
  * Name — account holder name;


  * Group — group the account belongs to;


  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Balance, currency — account balance at the time of the report request;
  * Floating P/L, currency — floating profit/loss on the account at the time of the report request;
  * Experts profit, currency — profit made by an Expert Advisor for a specified day in a specified currency;
  * Total profit, currency — total profit/loss for a specified day in a specified currency;
  * Experts orders — number of orders placed by Expert Advisors for a specified day;
  * Total orders — total number of orders placed by a user for a specified day.



### Users with the highest profit earned by Expert Advisors

The report contains 10 users having the highest profit as a result of their Expert Advisors' operation for a specified day. The table displays only profitable accounts (for a specified day).

The following data is displayed in the table:

  * Login — account number;
  * Name — account holder name;


  * Group — group the account belongs to;


  * Country — client's country of residence;
  * Account comment — comment to the trading account;


  * Balance, currency — account balance at the time of the report request;
  * Floating P/L, currency — floating profit/loss on the account at the time of the report request;
  * Experts deals — number of deals performed by Expert Advisors for a specified day;
  * Experts orders — number of orders placed by Expert Advisors for a specified day;
  * Experts profit, currency — profit made by an Expert Advisor for a specified day in a specified currency;
  * Total profit, currency — total profit/loss for a specified day in a specified currency.


