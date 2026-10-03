[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / Enumerations

[Previous](../IMTConAutomation.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConAutomation](../IMTConAutomation.md) class contains the following enumerations:

  * [IMTConAutomation::EnFlags (#enflags)](Enumerations.md#enflags)
  * [IMTConAutomation::EnTriggers (#entriggers)](Enumerations.md#entriggers)
  * [IMTConAutomation::EnTriggerWeekdays (#entriggerweekdays)](Enumerations.md#entriggerweekdays)
  * [IMTConAutomation::EnTriggerMonths (#entriggermonths)](Enumerations.md#entriggermonths)
  * [IMTConAutomation::EnTriggerMonthDays (#entriggermonthdays)](Enumerations.md#entriggermonthdays)



<a id="enflags"></a>
## IMTConAutomation::EnFlags (#enflags)

The IMTConAutomation::EnFlags enumeration contains automation task setup flags.

ID number | Value | Description  
FLAG_NONE | 0x00000000 | No flags.  
FLAG_ENABLED | 0x00000001 | The automation task is enabled. If the flag is not set, trigger conditions will not be checked and the task will not be executed.  
FLAG_FOLDER | 0x00000002 | The configuration object is not a task, but is a subdirectory where automation tasks are located.  
FLAG_FIRST |  | Beginning of enumeration. Corresponds to FLAG_NONE.  
FLAG_ALL |  | End of enumeration. Corresponds to enabling of all flags.  
  
The enumeration is used in the [IMTConAutomation::Flags](Flags.md) method.

<a id="entriggers"></a>
## IMTConAutomation::EnTriggers (#entriggers)

The IMTConAutomation::EnFlags enumeration contains [triggers](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_trigger) — events in the platform upon the occurrence of which the automation task should be executed.

ID number | Value | Description  
TRIGGER_SCHEDULE_SCHEDULE | 0 | Schedule-based execution of actions.  
TRIGGER_SCHEDULE_ACCOUNTS | 1 | Schedule-based maintenance of the entire account database on the trading server.  
TRIGGER_SCHEDULE_POSITIONS | 2 | Schedule-based maintenance of the entire position database on the trading server.  
TRIGGER_SCHEDULE_ORDERS | 3 | Schedule-based maintenance of the entire order database on the trading server.  
TRIGGER_SCHEDULE_FIRST | 0 | Beginning of enumeration of time-based triggers.  
TRIGGER_SCHEDULE_LAST | 1000 | End of enumeration of time-based triggers.  
TRIGGER_CONNECTIONS_LOGIN | 1001 | Account connection to the server.  
TRIGGER_CONNECTIONS_LOGIN_FIRST | 1002 | First account connection to the server.  
TRIGGER_CONNECTIONS_LOGOUT | 1003 | Disconnection of an account from the server.  
TRIGGER_CONNECTIONS_AUTHORIZE_FAIL | 1004 | Failed attempt to connect to an account, for instance, because of an invalid password.  
TRIGGER_CONNECTIONS_FIRST | 1001 | Beginning of enumeration of triggers related to account connection and disconnection.  
TRIGGER_CONNECTIONS_LAST | 2000 | End of enumeration of triggers related to account connection and disconnection.  
TRIGGER_ACCOUNT_CREATE | 2001 | Trading account creation.  
TRIGGER_ACCOUNT_DELETE | 2002 | Deleting a trading account.  
TRIGGER_ACCOUNT_ARCHIVE | 2003 | Moving a trading account to an archive.  
TRIGGER_ACCOUNT_RESTORE | 2004 | Restoring a trading account from an archive or backup database.  
TRIGGER_ACCOUNT_CHANGE_GROUP | 2005 | Moving a trading account from one group to another.  
TRIGGER_ACCOUNT_CHANGE_PASSWORD | 2006 | Changing any of the [trading account passwords (#enuserspasswords)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enuserspasswords).  
TRIGGER_ACCOUNT_FIRST | 2001 | Beginning of enumeration of triggers related to a change in the database of accounts.  
TRIGGER_ACCOUNT_LAST | 3000 | End of enumeration of triggers related to a change in the database of accounts.  
TRIGGER_FINANCE_DEPOSIT_IN | 3001 | Depositing to account.  
TRIGGER_FINANCE_DEPOSIT_IN_FIRST | 3002 | First account deposit.  
TRIGGER_FINANCE_DEPOSIT_OUT | 3003 | Withdrawal from account.  
TRIGGER_FINANCE_DEPOSIT_OUT_FIRST | 3004 | First account withdrawal. The value is currently not used.  
TRIGGER_FINANCE_CREDIT_IN | 3005 | Add credit funds to the account.  
TRIGGER_FINANCE_CREDIT_IN_FIRST | 3006 | First adding of credit funds to the account.  
TRIGGER_FINANCE_CREDIT_OUT | 3007 | Account credit funds out.  
TRIGGER_FINANCE_CREDIT_OUT_FIRST | 3008 | First credit-out operation on the account.  
TRIGGER_FINANCE_OPERATION | 3009 | Performing service operations on the account. These include balance, credit and correction operations performed by managers or API applications, as well as negative balance compensation and credit write-off operations.  
TRIGGER_FINANCE_FIRST | 3001 | Beginning of enumeration of triggers related to account balance operations.  
TRIGGER_FINANCE_LAST | 4000 | End of enumeration of triggers related to account balance operations.  
TRIGGER_TRADE_MARGIN_CALL | 4001 | Account entering the Margin Cal mode.  
TRIGGER_TRADE_STOP_OUT | 4002 | Account entering the Stop Out mode.  
TRIGGER_TRADE_POSITION_OPEN | 4003 | Position opening on the account.  
TRIGGER_TRADE_POSITION_INCREASE | 4004 | Volume increase of an existing position in the account.  
TRIGGER_TRADE_POSITION_DECREASE | 4005 | Volume decrease (partial closing) of an existing position in the account.  
TRIGGER_TRADE_POSITION_CLOSE | 4006 | Position closing on the account.  
TRIGGER_TRADE_POSITION_REVERSE | 4007 | Position reversal on the account.  
TRIGGER_TRADE_REQUEST_TIMEOUT | 4008 | Deleting a trade request upon the expiration of the maximum allowable processing time (3 minutes).  
TRIGGER_TRADE_FIRST | 4001 | Beginning of enumeration of triggers related to account trading operations.  
TRIGGER_TRADE_LAST | 5000 | End of enumeration of triggers related to account trading operations.  
TRIGGER_PRICES_GAP_STARTED | 5001 | The emergence of a gap on a trading instrument.  
TRIGGER_PRICES_GAP_FINISHED | 5002 | Canceling a gap mode for a financial instrument.  
TRIGGER_PRICES_DELAYED | 5003 | A delay in the delivery of symbol quotes exceeding the allowed delay specified in [IMTConSymbol::QuotesTimeout](../../Symbols/IMTConSymbol/QuotesTimeout.md).  
TRIGGER_PRICES_RESUMED | 5004 | Resumed delivery of symbol quotes after a delay.  
TRIGGER_PRICES_FIRST | 5001 | Beginning of enumeration of triggers related to trading instrument prices.  
TRIGGER_PRICES_LAST | 6000 | End of enumeration of triggers related to trading instrument prices.  
TRIGGER_PLATFORM_MONITOR | 6001 | Platform performance measurement.  
TRIGGER_PLATFORM_CONNECT | 6002 | Connection of any of the platform servers to the main trade server.  
TRIGGER_PLATFORM_DISCONNECT | 6003 | Disconnection of any of the platform servers from the main trade server.  
TRIGGER_PLATFORM_FAILOVER | 6004 | Automatic switching of any of the cluster components to a backup server.  
TRIGGER_PLATFORM_FIRST | 6001 | Beginning of enumeration of triggers related to platform and hardware operation.  
TRIGGER_PLATFORM_LAST | 7000 | End of enumeration of triggers related to platform and hardware operation.  
TRIGGER_EXTERNAL_API | 7001 | API event. This trigger allows setting up the execution of automation tasks based on custom events. Create a plugin, which will call the special [IMTServerAPI::AtuomationTrigger](../../../Server-API/Main-API-Interface/Configuration-Databases/Automation/Trigger.md) function according to the specified algorithm.  
TRIGGER_EXTERNAL_WEBCALLBACK | 7002 | This trigger enables the running of automation tasks using [Web Callback requests (#webcallback)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_trigger#webcallback).  
TRIGGER_EXTERNAL_FIRST | 7001 | Beginning of enumeration of triggers related to external events.  
TRIGGER_EXTERNAL_LAST | 8000 | End of enumeration of triggers related to external events.  
TRIGGER_MESSAGE_CLIENT_SEND | 8001 | The client has sent an email via the internal mail system.  
TRIGGER_MESSAGE_CLIENT_READ | 8002 | The client has read the email which was received via the internal mail system.  
TRIGGER_MESSAGE_SMS_FAIL | 8003 | Failed to send message via the [SMS provider](../../Messengers/IMTConMessenger.md).  
TRIGGER_MESSAGE_EMAIL_FAIL | 8004 | Failed to send message via the [instant messenger](../../Messengers/IMTConMessenger.md).  
TRIGGER_MESSAGE_MESSENGER_FAIL | 8005 | Failed to send [email](../../Mail-Servers/IMTConEmail.md).  
TRIGGER_MESSAGE_FIRST | 8001 | Beginning of enumeration of triggers related to email sending.  
TRIGGER_MESSAGE_LAST | 9000 | End of enumeration of triggers related to email sending.  
TRIGGER_GATEWAY_CONNECT | 9001 | The gateway has connected to the trading platform.  
TRIGGER_GATEWAY_DISCONNECT | 9002 | The gateway has disconnected from the trading platform.  
TRIGGER_GATEWAY_FIRST | 9001 | Beginning of enumeration of triggers related to gateway operation.  
TRIGGER_GATEWAY_LAST | 10000 | End of enumeration of triggers related to gateway operation.  
TRIGGER_DATAFEED_CONNECT | 10001 | The datafeed has connected to the trading platform.  
TRIGGER_DATAFEED_DISCONNECT | 10002 | The datafeed has disconnected from the trading platform.  
TRIGGER_DATAFEED_FIRST | 10001 | Beginning of enumeration of triggers related to datafeed operation.  
TRIGGER_DATAFEED_LAST | 11000 | End of enumeration of triggers related to datafeed operation.  
TRIGGER_KYC_START | 11001 | Launch KYC check.  
TRIGGER_KYC_CONFIRM | 11002 | Client confirmed by the KYC service.  
TRIGGER_KYC_REJECT | 11003 | Client rejected by the KYC service.  
TRIGGER_KYC_FIRST | 11001 | Beginning of enumeration of triggers related to [KYC checks](../../KYC/IMTCon.md).  
TRIGGER_KYC_LAST | 12000 | End of enumeration of triggers related to KYC checks.  
TRIGGER_MANAGER_ORDER_MODIFY | 12001 | Trade order modified.  
TRIGGER_MANAGER_ORDER_DELETE | 12002 | Trade order deleted.  
TRIGGER_MANAGER_ORDER_HISTORY | 12003 | Trade order moved to history.  
TRIGGER_MANAGER_ORDER_REOPEN | 12004 | Trade order reopened from history.  
TRIGGER_MANAGER_ORDER_RESTORE | 12005 | Trade order restored from backup.  
TRIGGER_MANAGER_DEAL_MODIFY | 12006 | Trade deal modified.  
TRIGGER_MANAGER_DEAL_DELETE | 12007 | Trade deal deleted.  
TRIGGER_MANAGER_DEAL_RESTORE | 12008 | Trade deal restored from backup.  
TRIGGER_MANAGER_POSITION_MODIFY | 12009 | Trade position modified.  
TRIGGER_MANAGER_POSITION_DELETE | 12010 | Trade position deleted.  
TRIGGER_MANAGER_POSITION_RESTORE | 12011 | Trade position restored from backup.  
TRIGGER_MANAGER_ACCOUNT_POSITIONS_FIX | 12012 | Account position fixed based on the account's deal history.  
TRIGGER_MANAGER_ACCOUNT_BALANCE_FIX | 12013 | Account balance fixed based on the account's deal history.  
TRIGGER_MANAGER_EXPORT_ACCOUNTS | 12014 | Saving account data to a file from the Manager terminal (pressing the "Export" command).  
TRIGGER_MANAGER_EXPORT_CLIENTS | 12015 | Saving client data to a file from the Manager terminal (pressing the "Export" command).  
TRIGGER_MANAGER_EXPORT_ORDERS | 12016 | Saving order data to a file from the Manager terminal (pressing the "Export" command).  
TRIGGER_MANAGER_EXPORT_POSITIONS | 12017 | Saving position data to a file from the Manager terminal (pressing the "Export" command).  
TRIGGER_MANAGER_EXPORT_DEALS | 12018 | Saving data on deals to a file from the Manager terminal (pressing the "Export" command).  
TRIGGER_MANAGER_EXPORT_REPORTS | 12019 | Saving a report to a file from the Manager terminal (pressing the "Save Report" command).  
TRIGGER_MANAGER_FIRST | 12001 | Beginning of enumeration of triggers related to [manager actions](../../Managers/IMTConManager.md).  
TRIGGER_MANAGER_LAST | 13000 | End of enumeration of triggers related to manager actions.  
TRIGGER_PAYMENT_REQUEST | 13001 | Payment request through the [integrated payment system](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments) in the client terminal: the user has entered the required details and submitted a request to the broker or payment provider. The event is called before the request is sent to an external provider or manager for verification (if provided by the [processing rules](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments/payments_rules)).  
TRIGGER_PAYMENT_REJECT | 13002 | Request rejected due to incorrect parameters or according to processing rules (either automatically or manually by a manager).  
TRIGGER_PAYMENT_CONFIRM | 13003 | [Manual request confirmation](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments/payments_processing) by a manager.  
TRIGGER_PAYMENT_DONE | 13004 | Successful payment completion. This event is called after a confirmation notification is received from the payment provider and the funds are credited to or debited from the account.  
TRIGGER_PAYMENT_FAIL | 13005 | Payment failed due to internal errors on the MetaTrader 5 server (e.g., missing conversion rates, provider unavailability, etc.).  
TRIGGER_PAYMENT_FIRST | 13001 | Beginning of enumeration of triggers related to transactions in the [integrated payment system](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments).  
TRIGGER_PAYMENT_LAST | 14000 | End of enumeration of triggers related to transactions in the integrated payment system.  
TRIGGER_FIRST |  | Beginning of enumeration. Corresponds to TRIGGER_TIME_FIRST.  
TRIGGER_LAST |  | End of enumeration. Corresponds to TRIGGER_MANAGER_LAST.  
  
The enumeration is used in the [IMTConAutomation::Trigger](Trigger.md) method.

<a id="entriggerweekdays"></a>
## IMTConAutomation::EnTriggerWeekdays (#entriggerweekdays)

IMTConAutomation::EnTriggerWeekdays is an enumeration of days on which task triggers can fire.

ID number | Value | Description  
TRIGGER_WEEKDAY_SUN | 0x00000001 | Sunday.  
TRIGGER_WEEKDAY_MON | 0x00000002 | Monday.  
TRIGGER_WEEKDAY_TUE | 0x00000004 | Tuesday.  
TRIGGER_WEEKDAY_WED | 0x00000008 | Wednesday.  
TRIGGER_WEEKDAY_THU | 0x00000010 | Thursday.  
TRIGGER_WEEKDAY_FRI | 0x00000020 | Friday.  
TRIGGER_WEEKDAY_SAT | 0x00000040 | Saturday.  
TRIGGER_WEEKDAY_NONE | 0 | No day.  
TRIGGER_WEEKDAY_ALL |  | All days.  
TRIGGER_WEEKDAY_FIRST |  | Beginning of enumeration. Corresponds to TRIGGER_WEEKDAY_SUN.  
TRIGGER_WEEKDAY_LAST |  | End of enumeration. Corresponds to TRIGGER_WEEKDAY_SAT.  
  
The enumeration is used in the [IMTConAutomation::TimeWeekdays](TimeWeekdays.md) method.

<a id="entriggermonths"></a>
## IMTConAutomation::EnTriggerMonths (#entriggermonths)

IMTConAutomation::EnTriggerMonths is an enumeration of months in which task triggers can fire.

ID number | Value | Description  
TRIGGER_MONTHS_JAN | 0x00000001 | January.  
TRIGGER_MONTHS_FEB | 0x00000002 | February.  
TRIGGER_MONTHS_MAR | 0x00000004 | March.  
TRIGGER_MONTHS_APR | 0x00000008 | April.  
TRIGGER_MONTHS_MAY | 0x00000010 | May.  
TRIGGER_MONTHS_JUN | 0x00000020 | June.  
TRIGGER_MONTHS_JUL | 0x00000040 | July.  
TRIGGER_MONTHS_AUG | 0x00000080 | August.  
TRIGGER_MONTHS_SEP | 0x00000100 | September.  
TRIGGER_MONTHS_OCT | 0x00000200 | October.  
TRIGGER_MONTHS_NOV | 0x00000400 | November.  
TRIGGER_MONTHS_DEC | 0x00000800 | December.  
TRIGGER_MONTHS_NONE | 0 | No month.  
TRIGGER_MONTHS_ALL |  | All months.  
TRIGGER_MONTHS_FIRST |  | Beginning of enumeration. Corresponds to TRIGGER_MONTHS_JAN.  
TRIGGER_MONTHS_LAST |  | End of enumeration. Corresponds to TRIGGER_MONTHS_DEC.  
  
The enumeration is used in the [IMTConAutomation::TimeMonths](TimeMonths.md) method.

<a id="entriggermonthdays"></a>
## IMTConAutomation::EnTriggerMonthDays (#entriggermonthdays)

IMTConAutomation::EnTriggerMonthDays is an enumeration of days of the month on which task triggers can fire.

ID number | Value | Description  
TRIGGER_MONTHDAY_1 | 0x00000001 | Day 1.  
TRIGGER_MONTHDAY_2 | 0x00000002 | Day 2.  
TRIGGER_MONTHDAY_3 | 0x00000004 | Day 3.  
TRIGGER_MONTHDAY_4 | 0x00000008 | Day 4.  
TRIGGER_MONTHDAY_5 | 0x00000010 | Day 5.  
TRIGGER_MONTHDAY_6 | 0x00000020 | Day 6.  
TRIGGER_MONTHDAY_7 | 0x00000040 | Day 7.  
TRIGGER_MONTHDAY_8 | 0x00000080 | Day 8.  
TRIGGER_MONTHDAY_9 | 0x00000100 | Day 9.  
TRIGGER_MONTHDAY_10 | 0x00000200 | Day 10.  
TRIGGER_MONTHDAY_11 | 0x00000400 | Day 11.  
TRIGGER_MONTHDAY_12 | 0x00000800 | Day 12.  
TRIGGER_MONTHDAY_13 | 0x00001000 | Day 13.  
TRIGGER_MONTHDAY_14 | 0x00002000 | Day 14.  
TRIGGER_MONTHDAY_15 | 0x00004000 | Day 15.  
TRIGGER_MONTHDAY_16 | 0x00008000 | Day 16.  
TRIGGER_MONTHDAY_17 | 0x00010000 | Day 17.  
TRIGGER_MONTHDAY_18 | 0x00020000 | Day 18.  
TRIGGER_MONTHDAY_19 | 0x00040000 | Day 19.  
TRIGGER_MONTHDAY_20 | 0x00080000 | Day 20.  
TRIGGER_MONTHDAY_21 | 0x00100000 | Day 21.  
TRIGGER_MONTHDAY_22 | 0x00200000 | Day 22.  
TRIGGER_MONTHDAY_23 | 0x00400000 | Day 23.  
TRIGGER_MONTHDAY_24 | 0x00800000 | Day 24.  
TRIGGER_MONTHDAY_25 | 0x01000000 | Day 25.  
TRIGGER_MONTHDAY_26 | 0x02000000 | Day 26.  
TRIGGER_MONTHDAY_27 | 0x04000000 | Day 27.  
TRIGGER_MONTHDAY_28 | 0x08000000 | Day 28.  
TRIGGER_MONTHDAY_29 | 0x10000000 | Day 29.  
TRIGGER_MONTHDAY_30 | 0x20000000 | Day 30.  
TRIGGER_MONTHDAY_31 | 0x40000000 | Day 31.  
TRIGGER_MONTHS_NONE | 0 | No day.  
TRIGGER_MONTHS_ALL | 0x7FFFFFFF | All days.  
TRIGGER_MONTHS_FIRST |  | Beginning of enumeration. Corresponds to TRIGGER_MONTHDAY_1.  
TRIGGER_MONTHS_LAST |  | End of enumeration. Corresponds to TRIGGER_MONTHDAY_31.  
  
The enumeration is used in the [IMTConAutomation::TimeMonthdays](TimeMonthdays.md) method.
