[🏠 Document Start](../README.md) / [Report API](README.md) / Ready-made Examples

[Previous](Multithreading.md) | [Next](Ready-made-Examples/Accounts-Groups.md)

# Ready-made Examples

MetaTrader 5 Report API installation packet contains several ready-made examples of reports in source codes. Their analysis allows a developer to quickly learn the details of using Report API and start creating custom reports.

Report examples can be found in the [/Examples (#exmaples)](../Getting-Started/Files-and-Folders.md#exmaples) folder of the directory where MetaTrader 5 Report API is installed.

  * Accounts.Standard.Reports — this example demonstrates possibilities for [HTML reports](HTML-Reports.md) generation using a custom template and also for realization of graphic expression in the form of SVG chart It includes the following reports:


  * [Accounts Groups](Ready-made-Examples/Accounts-Groups.md) — statistical report on accounts in groups on a server.
  * [Accounts Grow](Ready-made-Examples/Accounts-Growth.md) — report on the growth of the number of accounts in groups on a server.
  * [Accounts Lifetime by Countries](Ready-made-Examples/Accounts-Lifetime-by-Countries.md) — lifetime of accounts with a distribution by countries.


  * Capital.Standard.Reports — example of financial reports on clients:


  * [Money Flow Daily](Ready-made-Examples/Money-Flow-Daily.md) — a group of reports presenting the movement of funds on client accounts.
  * [Money Flow Weekly](Ready-made-Examples/Money-Flow-Weekly.md) — a group of reports representing the weekly movement of funds on client accounts.
  * [Lifetime Value](Ready-made-Examples/Lifetime-Value.md) — a group of reports concerning client LTVs.
  * [First Time Deposit](Ready-made-Examples/First-Time-Deposit.md) — a group of reports on first-time deposits on client accounts.
  * [Retention of Clients](Ready-made-Examples/Retention-of-Clients.md) — new client retention report.
  * [Retention of Trading Accounts](Ready-made-Examples/Retention-of-Trading-Accounts.md) — new client retention report by individual accounts.


  * Trades.Standard.Reports — the source code that contains [tabular reports](Tabular-Reports.md) generation examples included into the MetaTrader 5 platform:


  * [Agent](Ready-made-Examples/Agents.md) — report on all transactions connected with charging agent commissions.


  * [Agents Detailed](Ready-made-Examples/Agents-Detailed.md) — detailed report on agent commissions.


  * [Credit Facility](Ready-made-Examples/Credit-Facility.md) — credit operations report for the selected period.
  * [Daily Report](Ready-made-Examples/Daily.md) — report on the financial state of the requested accounts as of the end of a day.
  * [Daily Detailed](Ready-made-Examples/Daily-Detailed.md) — detailed report on the financial state of the one selected account as of the end of the day.
  * [Deals History](Ready-made-Examples/Deals-History.md) — summary report on the deals for the selected period.
  * [Deals Profit](Ready-made-Examples/Deals-Profit.md) — detailed report on deals for the selected period.
  * [Deals Initiators](Ready-made-Examples/Deals-Initiators.md) — deal initiators (reasons) report.
  * [Deals Geography](Ready-made-Examples/Deals-Geography.md) — trading activity distribution by country.
  * [Deals Weekly](Ready-made-Examples/Deals-Weekly.md) — trader activity report.
  * [Deposit and Withdrawal](Ready-made-Examples/Deposit-and-Withdrawal.md) — report on deposit and withdrawal operations for the selected period.
  * [Equity](Ready-made-Examples/Equity.md) — report on the financial state of the requested accounts as at the end of the day. The accounts are grouped according to their "Comment" field value. This report allows to generate reports on clients' accounts grouping them by custom criteria.


  * [Execution Types](Ready-made-Examples/Execution-Types.md) — report on the number, volume and type of executed trades.


  * [Margin Calls](Ready-made-Examples/Margin-Calls.md) — report on the state of margin call or stop out accounts.
  * [Orders History](Ready-made-Examples/Orders-History.md) — summary report on the orders for the selected period.


  * [Positions History](Ready-made-Examples/Positions-History.md) — summary report on positions for the selected period.


  * [Risk Appetite](Ready-made-Examples/Risk-Appetite.md) — a report reflecting the risk level accepted by traders.
  * [Segregated](Ready-made-Examples/Segregated.md) — summary report on the change of financial state of the requested accounts for the specified period.
  * [Summary](Ready-made-Examples/Summary.md) — summary motion of funds and funds cycles for the selected period.


  * [Trade Accounts](Ready-made-Examples/Trade-Accounts.md) — report on the current trading statuses of client accounts.


  * [Trade Modifications](Ready-made-Examples/Trade-Modifications.md) — report on trade operations manually changed by an administrator, manager or API.
  * [Trade Performance Summary](Ready-made-Examples/Trade-Performance-Summary.md) — detailed trading statistics of trading accounts.
  * [Trade Group Statistics](Ready-made-Examples/Trade-Group-Statistics.md) — detailed statistics of groups: the number of accounts, commission amounts, share of trades by type, and more.


  * [StopOut Compensations](Ready-made-Examples/StopOut-Compensations.md) — report on operations associated with the compensation of a negative balance in the situation of Stop out. All trades with the "so compensation" type are included into this report.
  * [Fast Profit Deals](Ready-made-Examples/Fast-Profit-Deals.md) — this report is designed to detect traders exploiting arbitrage opportunities through quote delays


  * Daily.Standard.Reports — the source code that contains daily reports generation examples included into the MetaTrader 5 platform:


  * [Daily Dealing](Ready-made-Examples/Daily-Dealing.md) — daily report on the activity of dealers.
  * [Daily Server Logs](Ready-made-Examples/Daily-Server-Logs.md) — statistical report on the operation of the platform for the specified day.
  * [Daily Trades](Ready-made-Examples/Daily-Trades.md) — report on trade operations for the specified day.


  * [Daily Orders](Ready-made-Examples/Daily-Orders.md) — report on client orders open at the end of the selected day.
  * [Daily Positions](Ready-made-Examples/Daily-Positions.md) — report on client positions open at the end of the selected day.


  * [Daily Expert Advisors](Ready-made-Examples/Daily-Expert-Advisors.md) — report on trading operations performed by Expert Advisors of clients.


  * Gateway.Standard.Reports — the source code that contains examples of several reports on gateways:


  * [Gateways Turnover](Ready-made-Examples/Gateways-Turnover.md) — report on volumes of the deals handled by gateways.
  * [Gateways Profit](Ready-made-Examples/Gateways-Profit.md) — report on volumes of the deals handled by gateways, as well as the profit earned by a broker when handling these deals.
  * [Gateways White Label](Ready-made-Examples/Gateways-White-Label.md) — report on volumes of the deals performed on a trading server by external brokers via MetaTrader 5 Gateway (standard or White Label version).


  * Trades.Transaction.Reports — the source code that contains an example of the trade transaction report:


  * [Trade Transactions](Ready-made-Examples/Trade-Transactions.md) — provides detailed data on trading operations on MetaTrader 5 servers.


  * [NFA](Ready-made-Examples/NFA.md) — the source code that contains an example of reports to be submitted to NFA regulator.


  * [EMIR](Ready-made-Examples/EMIR.md) — the source code that contains an example of a report to be submitted to regulator according to EMIR.


  * [Fund Overview](Ready-made-Examples/Fund-Overview.md) — a report reflecting the key characteristics of a hedge fund.


