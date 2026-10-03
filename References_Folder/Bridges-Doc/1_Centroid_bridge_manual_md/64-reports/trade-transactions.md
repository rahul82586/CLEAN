[🏠 Document Start](..\README.md) / [Risk Account Statement](README.md) / Trade Transactions

# Trade Transactions

Overview
The Trade Transaction Report serves as a comprehensive account statement, enabling Brokers to review a detailed history of all balance
transactions impacting the Risk Account Balance.
This report provides valuable insights into the various financial activities that have influenced the overall balance of the account.
Request Trade Transaction
To request a Trade Transaction Report:
1. Complete the Wizard as detailed below.
2. Click the “Search” button
Display Trade Transaction
After generating the Trade Transaction, you can perform the following actions
Upon requesting the Trade Transaction, you gain visibility into a range of Balance Transactions that occurred, influencing the Risk Account
throughout the chosen time interval. This feature allows you to examine and understand the diverse financial activities impacting the
account during the specified duration.
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval
Risk Account Choose a specific Risk Account from the array of Risk Accounts configured in the Centroid Bridge.
Field Description
Ticket The unique ID of the balance transactions
Open Time The Date and Time at which the balance transaction request was sent to the Centroid Bridge
Volume This information is applicable specifically to balance transactions involving PL in FIFO mode, where the closed
Volume is displayed. If the transaction corresponds to another type, unrelated to trading, such as Deposit or
Field Description

Withdrawal, the value will be 0.
Amt The USD amount either deposited into or deducted from the Risk Account. This value reflects the financial impact of
transactions involving deposits or withdrawals in USD.
Type The category of the balance transaction is identified by the following types:
PL [Profit & Loss]: Represents a closed order in FIFO mode.
Commission: Signifies the commission deducted from the Risk Account.
Swaps: Denotes swaps applied to the Risk Account.
Deposit: Indicates a transaction involving a deposit into the Risk Account.
Withdraw: Represents a withdrawal from the Risk Account.
Credit: Refers to a credit transaction, either in or out.
Other: Encompasses other types of in/out balance operations that may be conducted for balance adjustment
purposes.
Symbol The Symbol involved in the event of a balance transaction representing a closed trade. Otherwise, the field will
display an empty value.
Cur Currency of the Risk Account, USD
Open Price The Open Price of the Order being closed, if Balance Transaction is a PL. For other Balance Transactions, this
column will show 0
Open Cen
Order
The Order ID of the Open Position if Balance Transaction is a PL resulting from a partial or full closing of a Position.
For other Balance Transactions, this column will show an empty value
Close Time The Close Time column indicates the closing time of the position if the balance transaction is a Profit/Loss (PL)
resulting from partial or full position closure. For other balance transactions, this column will display an empty value.
Close Price The Close Price column indicates the closing price of the order if the balance transaction is a Profit/Loss (PL).
Otherwise, this column will display a value of 0.
Closed Cen
Order
The Order ID for closing a position is displayed if the balance transaction corresponds to a Profit/Loss (PL),
Commission, or Swaps. For other balance transactions, this column will indicate 0. This differentiation helps identify
the specific order involved in the closure process for relevant transactions and highlights instances where the column
remains inactive for other types of balance transactions.
Transaction
Time
The timestamp indicating when the amount resulting from the balance transaction was added or deducted from the
account.
Comment The Comment field is either automatically generated or manually entered:
Manual: For non-trade-related transactions like Deposits, Withdrawals, Credits, and Adjustments, it will exhibit
the value manually input by the user into the Comment field during the execution of account balance operations.
Automatic: For trade-related transactions such as realized PL, commissions, and Swaps, the comment is
automatically populated, revealing the open and closed price of the Order. This is particularly applicable when
closing two Orders against each other.
Total
Commissions
The aggregate of all incurred Commissions within the specified time frame.
Total Swaps The cumulative total of all accrued/paid Swaps within the designated time period.
Total Realized
PL
The cumulative total of all Realized Profit and Loss (PL) arising from Trades throughout the chosen time period.

To Export the Trade Transaction Report
Click “Export” and select “Export to Excel” or “Export to CSV”

Total
Deposits
The total accumulation of all Deposits executed in the Account within the specified time frame.
Total
Withdrawal
The aggregate of all Withdrawals subtracted from the Account within the specified time frame.
Total Credit The cumulative amount of Net Credits (in or out) within the specified time interval.


