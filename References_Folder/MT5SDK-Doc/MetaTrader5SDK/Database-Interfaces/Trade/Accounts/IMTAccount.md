[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Accounts](../Accounts.md) / IMTAccount

[Previous](../Accounts.md) | [Next](IMTAccount/Enumerations.md)

# IMTAccount

The IMTAccount class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTAccount/Release.md) | Delete the current object.  
[Assign](IMTAccount/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTAccount/Clear.md) | Clear an object.  
[Login](IMTAccount/Login.md) | Get and set the login of the client, to whom the trading account belongs.  
[CurrencyDigits](IMTAccount/CurrencyDigits.md) | Get and set the number of decimal places in the account deposit currency.  
[Balance](IMTAccount/Balance.md) | Get and set the balance of a trading account.  
[Credit](IMTAccount/Credit.md) | Get and set the current amount of credit given to an account.  
[Margin](IMTAccount/Margin.md) | Get and set the current value of the account margin.  
[MarginFree](IMTAccount/MarginFree.md) | Get and set the free margin of an account.  
[MarginLevel](IMTAccount/MarginLevel.md) | Get and set the margin level as a percentage.  
[MarginLeverage](IMTAccount/MarginLeverage.md) | Get and set the margin leverage.  
[MarginInitial](IMTAccount/MarginInitial.md) | Get and set the current size of the initial margin of positions on a trading account.  
[MarginMaintenance](IMTAccount/MarginMaintenance.md) | Get and set the current size of the maintenance margin of positions on a trading account.  
[Profit](IMTAccount/Profit.md) | Get and set the size of the current profit for all open positions.  
[Storage](IMTAccount/Storage.md) | Get and set the current size of swaps charged for open positions on the account.  
[Commission](IMTAccount/Commission.md) | Get and set the size of commissions charged for all transactions on the account. The field is deprecated and is no longer used.  
[Floating](IMTAccount/Floating.md) | Get and set the size of floating profit/loss of open positions on the account.  
[Equity](IMTAccount/Equity.md) | Get and set account equity.  
[SOActivation](IMTAccount/SOActivation.md) | Get and set the account status as per the minimum amount of funds on the account required to maintain trading positions.  
[SOTime](IMTAccount/SOTime.md) | Get and set the time when the Margin Call or Stop Out level was reached.  
[SOLevel](IMTAccount/SOLevel.md) | Get and set the margin level of an account at the time of reaching the Stop Out level.  
[SOEquity](IMTAccount/SOEquity.md) | Get and set the account equity at the time of reaching the Stop Out level.  
[SOMargin](IMTAccount/SOMargin.md) | Get and set the margin amount on an account at the time of reaching the Stop Out level.  
[BlockedCommission](IMTAccount/BlockedCommission.md) | Get and set the amount of the standard commission locked on the account, which has been accumulated during the day/month.  
[BlockedProfit](IMTAccount/BlockedProfit.md) | Get and set the amount of intraday profit locked on the account.  
[Assets](IMTAccount/Assets.md) | Get and set the current total amount of assets on a trading account.  
[Liabilities](IMTAccount/Liabilities.md) | Get and set the current total amount of liabilities on a trading account.  
  
The IMTAccount lass contains one enumeration:

Enumeration | Purpose  
---|---  
[EnSoActivation](IMTAccount/Enumerations.md) | Activation mode.
