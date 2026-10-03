[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Reports](../Reports.md) / Trade Accounts

[Previous](Execution-Types.md) | [Next](Trade-Transactions.md)

# Trade Accounts Report

Trade Accounts Report — a report on the current trading state of client accounts. 

## Configuration in MetaTrader 5 Manager

The following parameters must be set in the manager terminal before requesting the report:

  * Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.



## Report Data

The report is divided into four units that provide information on modified open orders, history orders, deals and positions:

  * Login — client account number.
  * Name — account holder's name.


  * Group — group the account belongs to.
  * Country — client's country of residence.
  * Account comment — comment to the trading account.


  * Balance — the current account balance.
  * Credit — credit funds on the account.
  * Equity — current account equity.
  * Margin — margin required to maintain open positions on the account.
  * Free Margin — the amount of free margin on the account.
  * Margin Level — the margin level on the account. It corresponds to the account equity or equity percentage to the margin volume (Equity / Margin * 100) depending on the group settings on the server.
  * Blocked Comm. — commission by orders and positions accumulated during a day/month. Depending on the [settings](../Groups/Commission-Settings/Commission-Calculation.md), preliminary commission calculation is performed during a day/month and the appropriate amount of money is blocked in the account and displayed here. The final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account in a balance operation (a separate deal of the 'Daily/Monthly commission' type), and the blocked amount is unblocked.
  * Blocked Profit — if a client group is configured to only include [floating loss (#margin)](../Groups/Group-Settings.md#margin) into free margin calculation, the amount of profit received by a client during a trading day will be recorded in a separate field 'Blocked Profit'. At the end of the trading day, the accumulated profits is released (reset) and is reflected on the user's balance (included into free margin calculation).
  * Profit — profit on the account.
  * Swap — the value of swaps on current client positions.
  * Floating P/L — amount of current floating profit or loss.
  * Currency — client's deposit currency.


