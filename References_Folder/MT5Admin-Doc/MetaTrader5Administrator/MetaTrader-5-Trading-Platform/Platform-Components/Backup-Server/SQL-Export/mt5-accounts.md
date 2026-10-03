[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_accounts

[Previous](mt5-deals/Enumerations.md) | [Next](mt5-prices.md)

# mt5_accounts

Data on the state of trading accounts is exported to the table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Primary key. The login of the client, to whom the trading account belongs.  
CurrencyDigits | Integer | The number of digits after the decimal point in the account deposit currency.  
Balance | Float | The balance of a trade account.  
Credit | Float | The current amount of credit given to an account.  
Margin | Float | The current margin of the account.  
MarginFree | Float | The free margin of an account.  
MarginLevel | Float | The margin level as a percentage. It is calculated as a percentage of the current account equity (Equity) to the margin volume (Margin);  
MarginLeverage | Integer | Margin leverage.  
MarginInitial | Float | The current size of the initial margin of positions on a trading account.  
MarginMaintenance | Float | The current size of the maintenance margin of positions on a trading account.  
Profit | Float | The size of the current profit for all open positions.  
Storage | Float | The current size of swaps charged for open positions on the account.  
Floating | Float | The size of floating profit/loss of open positions on the account. The floating profit/loss is calculated as the sum of Profit, Storage and Commission of open positions on the account.  
Equity | Float | The account equity calculated as a sum of Balance, Credit and Floating.  
BlockedCommission | Float | The amount of the standard commission locked on the account, which has been accumulated during the day/month.  
BlockedProfit | Float | The amount of intraday profit locked on the account.  
Assets | Float | The current total amount of assets on a trading account.  
Liabilities | Float | The current total amount of liabilities on a trading account.
