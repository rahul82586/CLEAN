[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_daily

[Previous](mt5-prices.md) | [Next](mt5-daily-orders.md)

# mt5_daily

Daily reports generated for clients are exported to the table. The table contains the following fields:

Name | Type | Description  
Datetime | DateTime | The date and time of the daily report generation.  
Login | Integer | The login of the client for whom the daily report is generated.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
DatetimePrev | DateTime | Date and time of the previous daily report generation in the YYYY-MM-DD HH:MM:SS.  
Name | String | The name of a client in the daily report  
Group | String | The group of a client in a daily report.  
Currency | String | The client's deposit currency in a daily report.  
Company | String | The company serving the client in a daily report.  
EMail | String | An email of a client in a daily report.  
Balance | Float | The size of a client's balance in a daily report.  
Credit | Float | The amount of a client's credit funds in a daily report.  
InterestRate | Float | The amount of accumulated annual interest. Annual interest is calculated every day in accordance with the [group settings (#interest)](../../../Platform-Setup/Groups/Group-Settings.md#interest) and is accumulated in a separate account field. At the end of each month, the accumulated amount is credited to the account balance using an [Interest rate (#action)](../../../Platform-Setup/Deals.md#action) operation, and the InterestRate value is reset to zero.  
CommissionDaily | Float | The amount of a client's commissions for a day in a report.  
CommissionMonthly | Float | The total amount of a client's commissions for the current month in a report.  
AgentDaily | Float | The amount of agent commission charged for a client's trade operations for a reported day.  
AgentMonthly | Float | The amount of agent commission charged for a client's trade operations for the current month.  
BalancePrevDay | Float | The value of a client's balance as of the end of the previous day.  
BalancePrevMonth | Float | The value of a client's balance as of the end of the current month.  
EquityPrevDay | Float | The value of a client's equity as of the end of the previous day.  
EquityPrevMonth | Float | The value of a client's equity as of the end of the previous trading month.  
Margin | Float | The size of a client's margin in a daily report.  
MarginFree | Float | A client's free margin in a daily report.  
MarginLevel | Float | The margin level of a client in a daily report.  
MarginLeverage | Integer | The margin leverage of a client in a daily report.  
Profit | Float | The size of the current profit for all open positions of a client in a daily report.  
ProfitStorage | Float | The current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance.  
ProfitEquity | Float | The amount of the current floating equity of a client in a daily report.  
ProfitAssets | Float | The current amount of a client's assets in a daily report. It is only used for the [Exchange risk management model (#risk)](../../../Platform-Setup/Groups/Group-Settings.md#risk).  
ProfitLiabilities | Float | The current amount of a client's liabilities in a daily report. It is only used for the [Exchange risk management model (#risk)](../../../Platform-Setup/Groups/Group-Settings.md#risk).  
DailyProfit | Float | The amount of a client's daily profit.  
DailyBalance | Float | The amount accrued to a client's balance during the reported day.  
DailyCredit | Float | The amount of credit given to a client during the reported day.  
DailyCharge | Float | The amount of other charges to the client's balance during the reported day.  
DailyCorrection | Float | The amount of corrective balance operations for a reported day.  
DailyBonus | Float | The amount of bonuses added to the client's balance for the reported day.  
DailyStorage | Float | The amount of swaps calculated for the client for a reported day.  
DailyCommInstant | Float | The amount of instant commissions charged from the client for a reported day.  
DailyCommRound | Float | The amount of turnover commissions charged from the client for a reported day.  
DailyCommFee | Float | The [fee](../../../Platform-Setup/Groups/Commission-Settings.md) amount charged for the client's deals for the reported day.  
DailyDividend | Float | The amount of dividends accrued to the client for a reported day.  
DailyTaxes | Float | The amount of taxes withheld from the client for the reported day.  
DailySOCompensation | Float | The amount of negative balance compensation accrued to the client for a reported day.  
DailyAgent | Float | The amount of agent commission charged for a client's trade operations for a reported day.  
DailyInterest | Float | The amount accrued to a client as part of the annual interest rate for the reported day.
