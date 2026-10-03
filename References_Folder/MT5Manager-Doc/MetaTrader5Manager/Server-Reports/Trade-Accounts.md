[🏠 Document Start](../README.md) / [Server Reports](README.md) / Trade Accounts

[Previous](Execution-Type.md) | [Next](Trade-Transactions.md)

# Trade Accounts Report

Trade Accounts Report — a report on the current trading state of client accounts. 

## Configuration in MetaTrader 5 Manager

The report features sorting the requested data. Set the following parameters before a request:

  * Groups — groups containing the accounts, on which the report should be created. You can specify one or several accounts separating them by commas.



## Report data

The report is divided into four units that provide information on modified open orders, history orders, deals and positions:

  * Login — client account number.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Balance — current account balance.
  * Credit — credit funds on the account.
  * Equity — current account equity.
  * Margin — margin required to maintain open positions on an account.
  * Free Margin — amount of free margin on an account.
  * Margin Level — margin level on an account. It corresponds to the account equity or equity percentage to the margin volume (Equity / Margin * 100) depending on the group settings on the server.
  * Blocked Comm. — commission by orders and positions accumulated during a day/month. Depending on the [settings (#commission)](../Managing-Trade-Server-Settings/Spread-Commission-and-Swap.md#commission), preliminary commission calculation is performed during a day/month and the appropriate amount of money is blocked in the account and displayed here. The final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account in a balance operation (a separate deal of the 'Daily/Monthly commission' type), and the blocked amount is unblocked.
  * Blocked Profit — if a client group is configured to only include floating loss into free margin calculation, the amount of profit received by a client during a trading day will be recorded in a separate Blocked Profit field. At the end of the trading day, the accumulated profits are released (reset) and reflected on the user's balance (included into free margin calculation).
  * Profit — profit on the account.
  * Swap — value of swaps on current client positions.
  * Floating P/L — amount of current floating profit or loss.
  * Currency — client's deposit currency.


