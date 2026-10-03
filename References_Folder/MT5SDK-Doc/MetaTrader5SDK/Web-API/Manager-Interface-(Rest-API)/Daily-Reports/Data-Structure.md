[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Daily Reports](../Daily-Reports.md) / Data Structure

[Previous](../Daily-Reports.md) | [Next](Get.md)

# Data Structure

Daily reports are passed in JSON format in response to the [/api/daily_get](Get.md) and [/api/daily_get_light](Get-Light.md) requests.

Method | Type | Purpose  
Timestamp | Integer | Daily report generation date and time. The date is specified in the [FILETIME](https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime) format.  
DatetimePrev | Integer | Previous daily report generation date and time. The date is specified in seconds that have since 01.01.1970.  
Login | Integer | Client login for which the daily report is generated.  
Name | String | Client name in a daily report.  
Group | String | Client group in a daily report.  
Currency | String | Client's deposit currency in a daily report.  
CurrencyDigits | Integer | The number of decimal places in the client's deposit currency in the daily report.  
Company | String | The company serving the client in a daily report.  
EMail | String | An email of a client in a daily report.  
Balance | Float | Client's balance in a daily report.  
Credit | Float | Client's credit funds in a daily report.  
InterestRate | Float | The amount of accumulated annual interest. Annual interest is calculated every day in accordance with the group settings ([IMTConGroup::TradeInterestrate](../../../Configuration-Interfaces/Groups/IMTConGroup/TradeInterestrate.md)) and is accumulated in a separate account field. At the end of each month, the accumulated amount is credited to the account balance using an [IMTDeal::DEAL_INTERESTRATE (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) operation, and the InterestRate value is reset to zero.  
CommissionDaily | Float | The amount of commissions charged from a client for a day in the report.  
CommissionMonthly | Float | The total amount of commissions charged from a client for the current month in the report.  
AgentDaily | Float | The size of agent commissions charged for the client's trading operations for a day.  
AgentMonthly | Float | The amount of agent commissions charged for the client's trade operations for the current month.  
BalancePrevDay | Float | Client's balance at the end of the previous day.  
BalancePrevMonth | Float | Client's balance at the end of the previous trading month.  
EquityPrevDay | Float | Client's equity at the end of the previous day.  
EquityPrevMonth | Float | Client's equity at the end of the previous trading month.  
Margin | Float | Client's margin in a daily report.  
MarginFree | Float | Client's free margin in a daily report.  
MarginLevel | Float | Client's margin level in the daily report.  
MarginLeverage | Float | Client's margin leverage in the daily report.  
Profit | Float | Current profit amount for all open positions of the client in the daily report.  
ProfitStorage | Float | The current amount of swaps charged for a client's open positions for a day, but not yet reflected in the balance.  
ProfitEquity | Float | Client's current floating equity in the daily report.  
ProfitAssets | Float | Client's current assets in the daily report.  
ProfitLiabilities | Float | Client's current liabilities in a daily report.  
DailyProfit | Float | The amount of a client's recorded daily profit.  
DailyBalance | Float | The amount accrued to a client's balance during the reported day.  
DailyCredit | Float | The amount of credit given to a client during the reported day.  
DailyCharge | Float | The amount of other charges to the client's balance during the reported day.  
DailyCorrection | Float | The amount of corrective balance operations for a reported day.  
DailyBonus | Float | The amount of bonuses added to the client's balance for the reported day.  
DailyStorage | Float | The amount of swaps charged to the client for a reported day.  
DailyCommInstant | Float | The amount of instant commissions charged from the client for a reported day.  
DailyCommFee | Float | The amount of fees charged to the client for a reported day.  
DailyCommRound | Float | The amount of turnover commissions charged from the client for the reported day.  
DailyAgent | Float | The size of agent commissions charged for a client's trade operations for the reported day.  
DailyInterest | Float | The amount accrued to a client as part of the annual interest rate for the reported day.  
PositionAdd | Array | Array of [account positions](../Trading/Positions/Data-Structure.md) at the report generation time.  
OrderAdd | Array | Array of [account orders](../Trading/Orders/Data-Structure.md) at the report generation time.
