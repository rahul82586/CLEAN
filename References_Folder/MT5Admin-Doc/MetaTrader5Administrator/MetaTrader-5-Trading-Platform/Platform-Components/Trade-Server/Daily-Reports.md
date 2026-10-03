[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Trade Server](../Trade-Server.md) / Daily Reports

[Previous](Mail-Templates.md) | [Next](SendMail-Utility.md)

# Daily Reports

At [the end of each working day and month, (#end-of-day)](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#end-of-day) the trade server prepares reports on client deals and places them to [trade server directory]/confirms/YYYYMMDD", where YYYYMMDD is the current date). Each report is an HTML file having the name "login_mail.htm" (for example, "123_mail.htm"). After creating the reports, the trade server sends them using [SendMail](SendMail-Utility.md) utility.

The database of all generated reports is saved in the file [trade server directory]/bases/daily.dat. The data from the database can be requested via the Manager terminal, for example, by using a report from [Daily Report](../../Platform-Setup/Reports/Daily.md) standard delivery.

## Enabling/Disabling Daily Reports

Generation of reports can be enabled/disabled for each [client group (#reports)](../../Platform-Setup/Groups/Group-Settings.md#reports) separately.

![Reports](images/groups_reports.png)

Here you can also configure sending reports to clients and (if necessary) the technical support via email.

## Customizing Report Appearance

Email templates with [daily (#daily)](Mail-Templates.md#daily) and [monthly (#monthly)](Mail-Templates.md#monthly) trading activity reports are located in the /templates/confirmation and /templates/statement folders of the trade server. 

## Configuring Daily Report Generation Time

Daily and monthly report generation time is defined [by the trade server settings (#end-of-day)](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#end-of-day): 

![End of day](images/network_add_eod.png)

The reports are affected by the following parameters:

  * End of day time — report generation start time.
  * End of day schedule — report generation days. The option does not affect monthly reports.
  * Daily statements — daily report generation time: at the end of a trading day (before charging swaps, annual interest, and commissions) or at the start of a trading day (after charging swaps, annual interest, and commissions).
  * Monthly statements — monthly report generation time: at the end of the last day of month (before charging swaps, annual interest, and commissions) or at the start of a first day of the next month (after charging swaps, annual interest, and commissions).



## Report Data

Name | Description  
---|---  
Datetime | Daily report generation date and time.  
Login | Initial key. The login of a client for whom the daily report is generated.  
DatetimePrev | Daily report previous generation date and time.  
Name | The name of a client in a daily report.  
Group | Client group in a daily report.  
Currency | Client's deposit currency in a daily report.  
Company | The company serving the client in a daily report.  
EMail | An email of a client in a daily report.  
Balance | The size of a client's balance in a daily report.  
Credit | The amount of a client's credit funds in a daily report.  
InterestRate | The annual interest rate of a client in a daily report.  
CommissionDaily | The amount of commissions charged from a client for a day in the report.  
CommissionMonthly | The amount of commissions charged from a client for the current month in a report.  
AgentDaily | The size of agent commissions charged for a client's trade operations for a day, from a daily report.  
AgentMonthly | The amount of agent commissions charged for a client's trade operations for the current month.  
BalancePrevDay | Client's balance as of the end of the previous day.  
BalancePrevMonth | Client's balance as of the end of the previous trading month.  
EquityPrevDay | A client's equity as of the end of the previous day.  
EquityPrevMonth | The value of a client's equity as of the end of the previous trading month.  
Margin | Size of a client's margin in a daily report. The report does not contain data on the margin charged for each position or order because in some cases, it is not possible to calculate the margin value for the following reasons:

  * On hedging accounts, multiple oppositely directed positions can exist for the same instrument. If their volumes do not match, the [hedged margin](../../Platform-Setup/Symbols/Symbol-Settings/Trade/Margin-Calculation/Retail-Forex-CFD-Futures-—-Hedging.md) is calculated based on the aggregate positions.
  * If on a netting account the margin is charged for pending orders and there are two oppositely directed orders for the same instrument, it is unknown in which of them the margin should be indicated. It is not known in advance which of the orders will be used to open a position and which one to close it.
  * When using [spreads](../../Platform-Setup/Spreads.md), the margin depends on the aggregate orders and positions.

  
MarginFree | A client's free margin in a daily report.  
MarginLevel | The margin level of a client in the daily report.  
MarginLeverage | The margin leverage of a client in the daily report.  
Profit | The size of the current profit for all open positions of a client in a daily report.  
ProfitStorage | The current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance.  
ProfitEquity | The amount of the current floating equity of a client in a daily report.  
DailyProfit | The amount of a client's daily profit.  
DailyBalance | The amount accrued to a client's balance during the reported day.  
DailyCredit | The amount of credit given to a client during the reported day.  
DailyCharge | The amount of other charges to the client's balance during the reported day.  
DailyCorrection | The amount of corrective balance operations for a reported day.  
DailyBonus | The amount of bonuses added to the client's balance for the reported day.  
DailyStorage | The amount of swaps calculated for the client for the reported day.  
DailyCommInstant | The amount of instant commissions charged from the client for a reported day.  
DailyCommRound | The amount of turnover commissions charged from the client for a reported day.  
DailyCommFee | The fee amount charged for the client's deals for the reported day.  
DailyAgent | The size of agent commissions charged for a client's trade operations for the reported day.  
DailyInterest | The amount accrued to a client as part of the annual interest rate for the reported day.
