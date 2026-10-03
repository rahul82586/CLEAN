[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Daily Reports](../Daily-Reports.md) / IMTDaily

[Previous](../Daily-Reports.md) | [Next](IMTDaily/Release.md)

# \IMTDaily

The IMTDaily class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDaily/Release.md) | Delete the current object.  
[Assign](IMTDaily/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDaily/Clear.md) | Clear an object.  
[Datetime](IMTDaily/Datetime.md) | Get and set the date and time of the daily report generation.  
[DatetimePrev](IMTDaily/DatetimePrev.md) | Get and set the date and time of the previous daily report generation.  
[Login](IMTDaily/Login.md) | Get the login of the client for whom the daily report is generated.  
[Name](IMTDaily/Name.md) | Get and set the name of a client in the daily report  
[Group](IMTDaily/Group.md) | Get and set the group of a client in a daily report.  
[Currency](IMTDaily/Currency.md) | Get and set the client's deposit currency in a daily report.  
[CurrencyDigits](IMTDaily/CurrencyDigits.md) | Get the number of digits after the decimal point in the client's deposit currency in a daily report.  
[Company](IMTDaily/Company.md) | Get and set the company serving the client in a daily report.  
[EMail](IMTDaily/EMail.md) | Get and set an email of a client in a daily report.  
[Balance](IMTDaily/Balance.md) | Get and set the size of a client's balance in a daily report.  
[Credit](IMTDaily/Credit.md) | Get and set the amount of a client's credit funds in a daily report.  
[InterestRate](IMTDaily/InterestRate.md) | Get and set the size of the annual interest rate of a client in a daily report.  
[CommissionDaily](IMTDaily/CommissionDaily.md) | Get and set the amount of a client's commissions for a day in a report.  
[CommissionMonthly](IMTDaily/CommissionMonthly.md) | Get and set the total amount of a client's commissions for the current month in a report.  
[AgentDaily](IMTDaily/AgentDaily.md) | Get and set the amount of agent commission charged for a client's trade operations for a reported day.  
[AgentMonthly](IMTDaily/AgentMonthly.md) | Get and set the amount of agent commission charged for a client's trade operations for the current month.  
[BalancePrevDay](IMTDaily/BalancePrevDay.md) | Get and set the value of a client's balance as of the end of the previous day.  
[BalancePrevMonth](IMTDaily/BalancePrevMonth.md) | Get and set the value of a client's balance as of the end of the current month.  
[EquityPrevDay](IMTDaily/EquityPrevDay.md) | Get and set the value of a client's equity as of the end of the previous day.  
[EquityPrevMonth](IMTDaily/EquityPrevMonth.md) | Get and set the value of a client's equity as of the end of the previous trading month.  
[Margin](IMTDaily/Margin.md) | Get and set the size of a client's margin in a daily report.  
[MarginFree](IMTDaily/MarginFree.md) | Get and set a client's free margin in a daily report.  
[MarginLevel](IMTDaily/MarginLevel.md) | Get and set the margin level of a client in a daily report.  
[MarginLeverage](IMTDaily/MarginLeverage.md) | Get and set the margin leverage of a client in a daily report.  
[Profit](IMTDaily/Profit.md) | Get and set the size of the current profit for all open positions of a client in a daily report.  
[ProfitStorage](IMTDaily/ProfitStorage.md) | Get and set the current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance.  
[ProfitCommission](IMTDaily/ProfitCommission.md) | Get and set the current unfixed commission of a client in a daily report. The field is deprecated and is no longer used.  
[ProfitEquity](IMTDaily/ProfitEquity.md) | Get and set the amount of the current floating equity of a client in a daily report.  
[ProfitAssets](IMTDaily/ProfitAssets.md) | Get and set the current amount of client assets in a daily report.  
[ProfitLiabilities](IMTDaily/ProfitLiabilities.md) | Get and set the current amount of client liabilities in a daily report.  
[DailyProfit](IMTDaily/DailyProfit.md) | Get and set the amount of a client's daily profit.  
[DailyBalance](IMTDaily/DailyBalance.md) | Get and set the amount accrued to a client's balance during the reported day.  
[DailyCredit](IMTDaily/DailyCredit.md) | Get and set the amount of credit given to a client during the reported day.  
[DailyCharge](IMTDaily/DailyCharge.md) | Get and set the amount of other charges from the client's balance during the reported day.  
[DailyCorrection](IMTDaily/DailyCorrection.md) | Get and set the amount of corrective balance operations for a reported day.  
[DailyBonus](IMTDaily/DailyBonus.md) | Gets and sets the amount of bonuses added to the client's balance for the reported day.  
[DailyStorage](IMTDaily/DailyStorage.md) | Get and set the amount of swaps calculated for the client for a reported day.  
[DailyCommInstant](IMTDaily/DailyCommInstant.md) | Get and set the amount of instant commissions charged from the client for a reported day.  
[DailyCommRound](IMTDaily/DailyCommRound.md) | Get and set the amount of turnover commissions charged from the client for a reported day.  
[DailyCommFee](IMTDaily/DailyCommFee.md) | Get and set the fee amount charged for the client's deals for the reported day.  
[DailyDividend](IMTDaily/DailyDividend.md) | Get and set the amount of dividends accrued to the client for a reported day.  
[DailyTaxes](IMTDaily/DailyTaxes.md) | Get and set the amount of taxes withheld from the client's funds for the reported day.  
[DailySOCompensation](IMTDaily/DailySOCompensation.md) | Get and set the amount of negative balance compensation accrued to the client for a reported day.  
[DailySOCompensationCredit](IMTDaily/DailySOCompensationCredit.md) | Get and set the amount of credit funds withdrawn from the account during the reported day as a result of a negative balance compensation operation.  
[DailyAgent](IMTDaily/DailyAgent.md) | Get and set the amount of agent commission charged for a client's trade operations for a reported day.  
[DailyInterest](IMTDaily/DailyInterest.md) | Get and set the amount accrued to a client as part of the annual interest rate for the reported day.  
[PositionAdd](IMTDaily/PositionAdd.md) | Add a trade position to the daily report.  
[PositionUpdate](IMTDaily/PositionUpdate.md) | Modify a trade position in a daily report by its index.  
[PositionDelete](IMTDaily/PositionDelete.md) | Delete a trade position from a daily report by its index.  
[PositionClear](IMTDaily/PositionClear.md) | Clear the list of positions in a daily report.  
[PositionShift](IMTDaily/PositionShift.md) | Move a trade position in the list.  
[PositionTotal](IMTDaily/PositionTotal.md) | Get the umber of trade position in the daily report.  
[PositionNext](IMTDaily/PositionNext.md) | Get a trade position by the index.  
[PositionGet](IMTDaily/PositionGet.md) | Get a trade position by the symbol name.  
[OrderAdd](IMTDaily/OrderAdd.md) | Add a trade order to the daily report.  
[OrderUpdate](IMTDaily/OrderUpdate.md) | Modify a trade order in a daily report by its index.  
[OrderDelete](IMTDaily/OrderDelete.md) | Delete a trade order from a daily report by its index.  
[OrderClear](IMTDaily/OrderClear.md) | Clear the list of orders in a daily report.  
[OrderShift](IMTDaily/OrderShift.md) | Move a trade order in the list.  
[OrderTotal](IMTDaily/OrderTotal.md) | Get the umber of trade orders in the daily report.  
[OrderNext](IMTDaily/OrderNext.md) | Get a trade order by the index.  
[OrderGet](IMTDaily/OrderGet.md) | Get a trade order by a ticket.
