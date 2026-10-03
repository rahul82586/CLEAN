[🏠 Document Start](..\README.md) / [Account Groups](README.md) / Balance Transaction

# Balance Transaction

Overview
The Balance Transaction component allows one to make a variety of Balance Transactions into a Risk Account in addition to viewing the
list of all available Risk Accounts along with their information such as balance, P/L and margin details in real-time. Balance Transactions
can be manual if they come from Balance Operations (deposits, withdrawals, credits, etc) or automatic if they result from Trades (realized
P/L, Commissions, Swaps, etc).
Within this module, you have the capability to:
Balance Transaction on Risk Account: Adjust account balances for risk management.
View Real-Time Risk Accounts: See up-to-date information on Risk Accounts.
List Flat and Stopped Out Risk Accounts: Identify accounts in a flat state or stopped out.
Export Risk Accounts Data (Excel/CSV): Save Risk Accounts details for analysis.
Export Margin Call or Stopped Out Accounts (Excel/CSV): Specifically export accounts in Margin Call or stopped out status.
Balance Transaction Operations
In this component, you can make a variety of Balance Transaction operations into or out of Risk Accounts.
To make a balance transaction:
1. Fill out the wizard as explained below
2. Click the “Submit” buttons to submit the changes


Account Balance
The Account Balance table displays the list of all available Risk Accounts along with their account information in real-time.
Name The name of the Risk Account
Currency The currency of the Risk Account into which all transactions are translated.
Balance The available balance of the Risk Account
Balance = Deposit + Realized P/L
Available
Withdraw
The available amount for withdrawal which is equivalent to the Free Margin
Available Withdraw = Equity – Margin Blocked - Credit
Equity The real-time Equity of the Risk Account
Equity = Balance + running PL
PL The real-time floating PL of the Risk Account
Blocked Margin The amount of used Margin in Account Currency (USD)
Blocked Margin = Volume * (margin/100) * avg price
Margin Level The Margin Level Percentage of the Risk Account
Margin Level = Equity/Margin blocked x 100
Commission The Commission charged in USD on the Risk Account on a per Symbol basis, if any. Commissions remain
unrealized (only affect Equity) until the Position is partially or fully closed, which will affect the Balance based on
the closed Volume.
Swap The Swap charged in USD on the Risk Account on a per Symbol basis for keeping positions overnight, if any.
Swaps remain unrealized (only affect Equity) until the Position is partially or fully closed, which will affect the
Balance based on the closed Volume
Field Description

Notional The total USD exposure of the Risk Account in Notional Volume
Credit The available credit granted to the Risk Account in USD, if any
Trading State The Trading State of the Risk Account.
STOPPED OUT: Risk Account is flat or negative which could be due to stop out or Account out of balance
MARGIN CALL: Risk Account is on Margin Call when the Margin Level hits or drops below the percentage
defined in Warn Level set for the Account
NEUTRAL: Risk Account has enough balance

