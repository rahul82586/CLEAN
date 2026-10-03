[🏠 Document Start](../README.md) / [Server API](README.md) / Interface of End-of-Day Events

[Previous](Interface-of-Trade-Events/HookTradeSplit.md) | [Next](Interface-of-End-of-Day-Events/OnEODStart.md)

# Interface of End-of-Day Events IMTEndOfDaySink

This interface allows to monitor events associated with operations performed on a trade server at the end of the trading day/month. The interface includes the following methods:

Method | Purpose  
---|---  
[OnEODStart](Interface-of-End-of-Day-Events/OnEODStart.md) | A handler of the event of start of operations associated with the end of the trading day.  
[OnEODGroupStart](Interface-of-End-of-Day-Events/OnEODGroupStart.md) | A handler of the event of start of operations associated with the end of the trading day for the specified group.  
[OnEODGroupCommission](Interface-of-End-of-Day-Events/OnEODGroupCommissions.md) | A handler of the event of start of commission charging for the specified group at the end of the trading day.  
[OnEODGroupInterest](Interface-of-End-of-Day-Events/OnEODGroupInterest.md) | A handler of the event of start of annual interest charging for the specified group at the end of the trading day.  
[OnEODGroupStatements](Interface-of-End-of-Day-Events/OnEODGroupStatements.md) | A handler of the event of start of daily report generation for the specified group at the end of the trading day.  
[OnEODGroupRollovers](Interface-of-End-of-Day-Events/OnEODGroupRollovers.md) | A handler of the event of start of rollover charging for the specified group at the end of the trading day.  
[OnEODGroupFinish](Interface-of-End-of-Day-Events/OnEODGroupFinish.md) | A handler of the event of completion of operations associated with the end of the trading day for the specified group.  
[OnEODFinish](Interface-of-End-of-Day-Events/OnEODFinish.md) | A handler of the event of completion of operations associated with the end of the trading day.  
[OnEOMStart](Interface-of-End-of-Day-Events/OnEOMStart.md) | A handler of the event of start of operations associated with the end of the trading month.  
[OnEOMGroupStart](Interface-of-End-of-Day-Events/OnEOMGroupStart.md) | A handler of the event of start of operations associated with the end of the trading month for the specified group.  
[OnEOMGroupCommission](Interface-of-End-of-Day-Events/OnEOMGroupCommissions.md) | A handler of the event of start of commission charging for the specified group at the end of the trading month.  
[OnEOMGroupInterest](Interface-of-End-of-Day-Events/OnEOMGroupInterest.md) | A handler of the event of start of annual interest charging for the specified group at the end of the trading month.  
[OnEOMGroupStatements](Interface-of-End-of-Day-Events/OnEOMGroupStatements.md) | A handler of the event of start of daily report generation for the specified group at the end of the trading month.  
[OnEOMGroupFinish](Interface-of-End-of-Day-Events/OnEOMGroupFinish.md) | A handler of the event of completion of operations associated with the end of the trading month for the specified group.  
[OnEOMFinish](Interface-of-End-of-Day-Events/OnEOMFinish.md) | A handler of the event of completion of operations associated with the end of the trading month.  
  
  * It is not guaranteed, that the end-of-day/month events occur in the order shown here.
  * At the time of operations associated with the end of a trading day/month, the trading state of the group (accounts in it) is blocked.

  
---  
  
## The order of end-of-day/month service operations

The order of operations depends on the report generation mode: at the end or at the beginning of the day ([IMTConServerTrade::EnOvernightMode (#enovernightmode)](../Configuration-Interfaces/Network/IMTConServerTrade/Enumerations.md#enovernightmode)). The performed actions also depend on whether the end of the trading day (as determined by the schedule [IMTConServerTrade::OvernightDays](../Configuration-Interfaces/Network/IMTConServerTrade/OvernightDays.md)) and end of month (as determined by the actual end of month) fall on this day.

When generating reports at the end of the day:

Condition | Operation  
---|---  
If there is end of the trading day | 1\. Beginning of the 'end of day' at the time of [IMTConServerTrade::OvernightTime](../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md), the [IMTEndOfDaySink::OnEODStart](Interface-of-End-of-Day-Events/OnEODStart.md) event call  
If there is end of the month | 2\. Beginning of the 'end of month' at the time of [IMTConServerTrade::OvernightTime](../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md), the [IMTEndOfDaySink::OnEOMStart](Interface-of-End-of-Day-Events/OnEOMStart.md) event call  
| 3\. Beginning of operations for each group:  
If there is end of the trading day | 4\. [IMTEndOfDaySink::OnEODGroupStart](Interface-of-End-of-Day-Events/OnEODGroupStart.md) event call  
If there is end of the trading day | 5\. Calculation and settlement of commissions (including agent commission) with the [IMTConCommission::COMM_CHARGE_DAILY (#encommchargemode)](../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommchargemode) calculation mode  
If there is end of the trading day | 6\. [IMTEndOfDaySink::OnEODGroupCommissions](Interface-of-End-of-Day-Events/OnEODGroupCommissions.md) event call  
If there is end of the month | 7\. [IMTEndOfDaySink::OnEOMGroupStart](Interface-of-End-of-Day-Events/OnEOMGroupStart.md) event call  
If there is end of the month | 8\. Calculation and settlement of commissions (including agent commission) with the [IMTConCommission::COMM_CHARGE_MONTHLY (#encommchargemode)](../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommchargemode) calculation mode  
If there is end of the month | 9\. [IMTEndOfDaySink::OnEOMGroupCommissions](Interface-of-End-of-Day-Events/OnEOMGroupCommissions.md) event call  
If there is end of the trading day | 10\. Calculation of interest on available funds and saving them in the client record  
If there is end of the trading day | 11\. [IMTEndOfDaySink::OnEODGroupInterest](Interface-of-End-of-Day-Events/OnEODGroupInterest.md) event call  
If there is end of the month | 12\. Calculation and of the accumulated interest on available funds and depositing it to the balance  
If there is end of the month | 13\. [IMTEndOfDaySink::OnEOMGroupInterest](Interface-of-End-of-Day-Events/OnEOMGroupInterest.md) event call  
If there is end of the trading day | 14\. Daily report generation, [IMTDailySink::OnDailyAdd](../Database-Interfaces/Trade/Daily-Reports/IMTDailySink/OnDailyAdd.md) event call, if record generation was performed  
If there is end of the trading day | 15\. [IMTEndOfDaySink::OnEODGroupStatements](Interface-of-End-of-Day-Events/OnEODGroupStatements.md) event call  
If there is end of the trading day | 16\. Updating of the previous day balances (used in daily/monthly reports)  
If there is end of the trading day | 17\. [IMTEndOfDaySink::OnEODGroupFinish](Interface-of-End-of-Day-Events/OnEODGroupFinish.md) event call  
If there is end of the month | 18\. Generation of monthly reports  
If there is end of the month | 19\. [IMTEndOfDaySink::OnEOMGroupStatements](Interface-of-End-of-Day-Events/OnEOMGroupStatements.md) event call  
If there is end of the month | 20\. Update of previous month balances (used in daily/monthly reports)  
If there is end of the month | 21\. [IMTEndOfDaySink::OnEOMGroupFinish](Interface-of-End-of-Day-Events/OnEOMGroupFinish.md) event calls  
If there is end of the trading day | 22\. Calculation of swaps  
If there is end of the trading day | 23\. [IMTEndOfDaySink::OnEODGroupRollovers](Interface-of-End-of-Day-Events/OnEODGroupRollovers.md) event call  
| 24\. End of operations for each group  
If there is end of the trading day | 25\. [IMTEndOfDaySink::OnEODFinish](Interface-of-End-of-Day-Events/OnEODFinish.md) event call  
If there is end of the month | 26\. [IMTEndOfDaySink::OnEOMFinish](Interface-of-End-of-Day-Events/OnEOMFinish.md) event call  
  
When generating reports at the beginning of the day:

Condition | Operation  
---|---  
If there is end of the trading day | 1\. Beginning of the 'end of day' at the time of [IMTConServerTrade::OvernightTime](../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md), the [IMTEndOfDaySink::OnEODStart](Interface-of-End-of-Day-Events/OnEODStart.md) event call  
If there is end of the month | 2\. Beginning of the 'end of month' at the time of [IMTConServerTrade::OvernightTime](../Configuration-Interfaces/Network/IMTConServerTrade/OvernightTime.md), the [IMTEndOfDaySink::OnEOMStart](Interface-of-End-of-Day-Events/OnEOMStart.md) event call  
| 3\. Beginning of operations for each group:  
If there is end of the trading day | 4\. [IMTEndOfDaySink::OnEODGroupStart](Interface-of-End-of-Day-Events/OnEODGroupStart.md) event call  
If there is end of the trading day | 5\. Calculation and settlement of commissions (including agent commission) with the [IMTConCommission::COMM_CHARGE_DAILY (#encommchargemode)](../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommchargemode) calculation mode  
If there is end of the trading day | 6\. [IMTEndOfDaySink::OnEODGroupCommissions](Interface-of-End-of-Day-Events/OnEODGroupCommissions.md) event call  
If there is end of the month | 7\. [IMTEndOfDaySink::OnEOMGroupStart](Interface-of-End-of-Day-Events/OnEOMGroupStart.md) event call  
If there is end of the month | 8\. Calculation and settlement of commissions (including agent commission) with the [IMTConCommission::COMM_CHARGE_MONTHLY (#encommchargemode)](../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommchargemode) calculation mode  
If there is end of the month | 9\. [IMTEndOfDaySink::OnEOMGroupCommissions](Interface-of-End-of-Day-Events/OnEOMGroupCommissions.md) event call  
If there is end of the trading day | 10\. Calculation of interest on available funds and saving them in the client record  
If there is end of the trading day | 11\. [IMTEndOfDaySink::OnEODGroupInterest](Interface-of-End-of-Day-Events/OnEODGroupInterest.md) event call  
If there is end of the month | 12\. Calculation and of the accumulated interest on available funds and depositing it to the balance  
If there is end of the month | 13\. [IMTEndOfDaySink::OnEOMGroupInterest](Interface-of-End-of-Day-Events/OnEOMGroupInterest.md) event call  
If there is end of the trading day | 14\. Calculation of swaps  
If there is end of the trading day | 15\. [IMTEndOfDaySink::OnEODGroupRollovers](Interface-of-End-of-Day-Events/OnEODGroupRollovers.md) event call  
If there is end of the trading day | 16\. Daily report generation, [IMTDailySink::OnDailyAdd](../Database-Interfaces/Trade/Daily-Reports/IMTDailySink/OnDailyAdd.md) event call, if record generation was performed  
If there is end of the trading day | 17\. [IMTEndOfDaySink::OnEODGroupStatements](Interface-of-End-of-Day-Events/OnEODGroupStatements.md) event call  
If there is end of the trading day | 18\. Updating of the previous day balances (used in daily/monthly reports)  
If there is end of the trading day | 19\. [IMTEndOfDaySink::OnEODGroupFinish](Interface-of-End-of-Day-Events/OnEODGroupFinish.md) event call  
If there is end of the month | 20\. Generation of monthly reports  
If there is end of the month | 21\. [IMTEndOfDaySink::OnEOMGroupStatements](Interface-of-End-of-Day-Events/OnEOMGroupStatements.md) event call  
If there is end of the month | 22\. Update of previous month balances (used in daily/monthly reports)  
If there is end of the month | 23\. [IMTEndOfDaySink::OnEOMGroupFinish](Interface-of-End-of-Day-Events/OnEOMGroupFinish.md) event calls  
| 24\. End of operations for each group  
If there is end of the trading day | 25\. [IMTEndOfDaySink::OnEODFinish](Interface-of-End-of-Day-Events/OnEODFinish.md) event call  
If there is end of the month | 26\. [IMTEndOfDaySink::OnEOMFinish](Interface-of-End-of-Day-Events/OnEOMFinish.md) event call
