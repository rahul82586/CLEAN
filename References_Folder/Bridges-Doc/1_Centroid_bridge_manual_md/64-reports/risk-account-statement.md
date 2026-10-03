[🏠 Document Start](..\README.md) / [MT5 Reports](README.md) / Risk Account Statement

# Risk Account Statement

Overview
The Risk Account Statement offers Brokers and Traders (Risk Users) a comprehensive view of Risk Accounts, allowing them to review
both Trade and Account information. Moreover, the Risk Account Statement is categorized into three tabs, providing access to historical
reports, statements, as well as real-time trade and account details.
Request Risk Account Statement
To request a Risk Account Statement
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Click the “Search” button
4. Export the statement to HTML
Note: Use the Reset button to clear the pre-defined filters
Display Risk Account Statement
After generating the Risk Account Statement, you can perform the following actions
The Risk Account Statement is divided into three components: Closed Transactions, Positions and Account Balance
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval
Risk
Account
Choose a specific Risk Account from the array of Risk Accounts configured in the Centroid Bridge.
Field Description


Closed Transactions
The Closed Transactions Report, positioned at the top, displays all balance transactions impacting the Risk Account Balance.
This includes transactions like Deposits, Withdrawals, Realized Profit/Loss, Swaps, Commissions, and more.
Ticket The unique ID of the balance transactions
Open Time The Date and Time at which the balance transaction request was sent to the Centroid Bridge
Volume This is relevant only if the balance transaction is a PL in FIFO mode where the closed Volume is shown. In case it
corresponds to another type of balance transaction not related to trading such as Deposit or Withdrawal the value
would be 0
Amt The amount in USD deposited into or deducted from the Risk Account.
Type The category of the balance transaction is identified by the following types:
PL [Profit & Loss]: Represents a closed order in FIFO mode.
Commission: Signifies the commission deducted from the Risk Account.
Swaps: Denotes swaps applied to the Risk Account.
Deposit: Indicates a transaction involving a deposit into the Risk Account.
Withdraw: Represents a withdrawal from the Risk Account.
Credit: Refers to a credit transaction, either in or out.
Other: Encompasses other types of in/out balance operations that may be conducted for balance adjustment
purposes.
Symbol The Symbol involved in the event of a balance transaction representing a closed trade. Otherwise, the field will display
an empty value.
Cur Currency of the Risk Account, USD
Open Price The Open Price of the Order being closed, if Balance Transaction is a PL. For other Balance Transactions, this column
will show 0
Open Cen
Order
The Order ID of the Open Position if Balance Transaction is a PL resulting from a partial or full closing of a Position.
For other Balance Transactions, this column will show an empty value
Close Time The Close Time of the Position if Balance Transaction is a PL resulting from partial or full Position closure. For other
Balance Transactions, this column will show an empty value
Close Price The Close Price of the Order being closed, if the balance transaction is a PL. Otherwise, this column will show 0
Field Description

Open Positions
The Open Positions tab displays the comprehensive view of all net open positions within the Risk Account, consolidated on a per-Symbol
basis.
Closed Cen
Order
The Order ID for closing a Position is indicated in the case of a PL, Commission, or Swaps balance transaction. For
other balance transactions, this column will display 0.
Transaction
Time
The Time at which the amount resulting from Balance Transaction was added or deducted from the Account
Comment The Comment field is either automatically generated or manually entered:
Manual: For non-trade-related transactions like Deposits, Withdrawals, Credits, and Adjustments, it will exhibit the
value manually input by the user into the Comment field during the execution of account balance operations.
Automatic: For trade-related transactions such as realized PL, commissions, and Swaps, the comment is
automatically populated, revealing the open and closed price of the Order. This is particularly applicable when
closing two Orders against each other.
Total
Commission
s
The aggregate of all incurred Commissions within the specified time frame.
Total Swaps The cumulative total of all accrued/paid Swaps within the designated time period.
Total
Realized PL
The cumulative total of all Realized Profit and Loss (PL) arising from Trades throughout the chosen time period.
Total
Deposits
The total accumulation of all Deposits executed in the Account within the specified time frame.
Total
Withdrawal
The aggregate of all Withdrawals subtracted from the Account within the specified time frame.
Total Credit The cumulative amount of Net Credits (in or out) within the specified time interval.
Pos ID The ID number of the Position
Symbol The Open Position Symbol
Risk
Account
The name of the selected Risk Account
Field Description

Account Balance
The Account Balance tab provides live updates on key Account Balance details for the Risk Account, including information on Balance,
Equity, Margin, floating Profit/Loss (PL), and more.
Liquidity
Model
The Liquidity Model assigned to the Risk Account which defines the pool of Makers
Net Volume The Notional Volume of the Position in USD
ANet
Volume
The Notional Volume of the STP Position in USD
BNet
Volume
The Notional Volume of the B Book Position in USD
Avg Price The Weighted Average Price of the orders comprising the position.
AAvg Price The Weighted Average Price of the STP orders forming the position.
BAvg Price The Weighted Average Price of the B-Book orders forming the position.
Last Time The Last Time the real-time data of the Position were updated
Close Price The current market price of the symbol.
PL The floating Profit/Loss of the symbol determined by the open positions.
Margin The existing Utilized or Blocked Margin associated with the open positions of the symbol. This reflects the margin
amount currently allocated or reserved for the symbol's open positions.
Swaps The cumulative unrealized Swap charges applied to the open positions. This represents the total accrued swap fees on
the currently active positions.
Commission
s
The commissions incurred upon the initiation of the positions. This refers to the total commission charges associated
with the opening of the positions.
Total
Unrealized
Swaps
The total of all unrealized swaps associated with open positions across all symbols. This includes the collective amount
of swap charges that have accrued but not yet been realized for open positions.
Total
Unrealized
PL
The overall unrealized Profit/Loss (PL) of the Risk Account. This encompasses the total unrealized financial gain or
loss across all open positions within the account.


To Export the Risk Account Statement
Click on “Export to HTML” to export the statement
Name The Name of the selected Risk Account
Margin
Blocked
The utilized Margin amount in the Account Currency (USD). This represents the extent of Margin that has been
employed in USD within the account.
Balance The accessible balance within the Risk Account. This denotes the remaining funds that are available for trading or
withdrawal after considering existing positions and any reserved margin.
Available to
Withdraw
The available withdrawal amount, equivalent to the Free Margin, is calculated as follows:
Available Withdraw=Equity−Margin Blocked−Credit
This represents the amount that can be withdrawn, factoring in the current Equity, blocked margin, and credit in the
Risk Account.
Equity The Equity of the Risk Account signifies the total current value of the account, encompassing both the open positions
and available balance
PL The floating Profit/Loss (PL) of the Risk Account represents the unrealized gains or losses associated with open
positions.
Margin Level The Margin Level Percentage for the Risk Account is calculated as follows:
Margin Level=Equity/Margin Blocked × 100
This percentage indicates the relationship between the account's Equity and the blocked Margin, serving as a crucial
measure of risk exposure and available margin for trading.
Commission The total unrealized Commission charged in USD on all Open Positions
Note: These Commissions remain unrealized (only affect Equity) until the Position or part of the Position is closed, and
then it will affect the Balance based on the closed Volume
Swaps The total unrealized Swaps charged in USD on the Risk Account on a per Symbol basis for keeping positions
overnight, if any.
Note: These Swaps remain unrealized (only affect Equity) until the Position or part of the Position is closed, and then it
will affect the Balance based on the closed Volume
Notional The aggregated USD exposure of the Risk Account in Notional Volume represents the total financial commitment of
the account across all positions.
Credit The available credit extended to the Risk Account in USD, if applicable. This signifies the amount of credit that the
account is currently eligible to utilize.
Trading
State
The Trading State of the Risk Account is as follows:
STOPPED OUT: The Risk Account is either flat or negative, possibly resulting from a stop-out or an imbalance in
the account.
MARGIN CALL: The Risk Account is under a Margin Call when the Margin Level reaches or falls below the
percentage specified in the Warn Level set for the Account.
NEUTRAL: The Risk Account is adequately funded and in a neutral state.
Field Description



